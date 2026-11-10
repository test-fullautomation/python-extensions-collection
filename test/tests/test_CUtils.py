#  Copyright 2020-2026 Robert Bosch GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# --------------------------------------------------------------------------------------------------------------
#
# test_CUtils.py
#
# XC-HWP/ESW3-Queckenstedt
#
# 10.11.2026
#
# --------------------------------------------------------------------------------------------------------------
#
# Self tests for the improved dotdict/mapping type detection in CUtils (``_IsDotDictLike`` and the
# ``[DOTDICT]``/``[MAPPING]`` branches of ``CTypePrint.TypePrint``/``PrettyPrint``).
#
# These tests reproduce the review findings that drove the detection logic through three
# implementation rounds (see C:\RobotTest\documentation\docs\pretty_print_type_detection.md
# for the full narrative):
#
# 1. the original instance-key-sampling check missed dotdicts with purely numeric/space-only
#    keys, or with no keys at all (empty dotdict);
# 2. the class-based "hasattr(type(oData), '__getattr__')" check that fixed (1) in turn missed
#    dotdicts that forward attribute access via "self.__dict__ = self" (no __getattr__ override
#    at all, just the default __getattribute__ mechanism);
# 3. the behavioral probe that fixed (2) by comparing "getattr(oData, key) == oData[key]" was
#    itself dependent on the probed value's own equality semantics: a first value of
#    float('nan') (never equal to itself) produced a false negative, and a first value of
#    decimal.Decimal('sNaN') made the "==" raise InvalidOperation, aborting PrettyPrint entirely.
#
# --------------------------------------------------------------------------------------------------------------

# -- import standard Python modules
import os, sys, decimal, collections.abc, pytest

# -- import own Python modules (containing the code to be tested)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))) # to make sure to hit the package relative to this file at first
from PythonExtensionsCollection.Utils.CUtils import PrettyPrint, _IsDotDictLike

# --------------------------------------------------------------------------------------------------------------

class CGetAttrDotDict(dict):
   """A classic dotdict: attribute access is forwarded via an explicit ``__getattr__`` override."""
   def __getattr__(self, sKey):
      try:
         return self[sKey]
      except KeyError:
         raise AttributeError(sKey)

class CSelfDictDotDict(dict):
   """A dotdict that forwards attribute access via ``self.__dict__ = self`` instead of
``__getattr__`` (uses the default ``__getattribute__`` mechanism)."""
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.__dict__ = self

class CPlainMapping(collections.abc.Mapping):
   """A ``Mapping`` that does not forward attribute access to its keys at all (a plain,
non-dotdict Mapping implementation)."""
   def __init__(self, dData):
      self._dData = dData
   def __getitem__(self, sKey):
      return self._dData[sKey]
   def __iter__(self):
      return iter(self._dData)
   def __len__(self):
      return len(self._dData)

# --------------------------------------------------------------------------------------------------------------

class Test_IsDotDictLike:
   """Tests of CUtils function '_IsDotDictLike'."""

   # --------------------------------------------------------------------------------------------------------------

   @pytest.mark.parametrize(
      "Description", ["A plain 'dict' is not dotdict-like.",]
   )
   def test_PlainDict(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = {"K1": 4}
      assert _IsDotDictLike(oData) is False

   @pytest.mark.parametrize(
      "Description", ["A Mapping without attribute forwarding is not dotdict-like.",]
   )
   def test_PlainMapping(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CPlainMapping({"K1": 4})
      assert _IsDotDictLike(oData) is False

   @pytest.mark.parametrize(
      "Description", ["A dotdict implemented via '__getattr__' is detected.",]
   )
   def test_GetAttrDotDict(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CGetAttrDotDict({"K1": 4})
      assert _IsDotDictLike(oData) is True

   @pytest.mark.parametrize(
      "Description", ["A dotdict implemented via 'self.__dict__ = self' is detected (2nd review finding).",]
   )
   def test_SelfDictDotDict(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CSelfDictDotDict({"K1": 4})
      assert _IsDotDictLike(oData) is True

   @pytest.mark.parametrize(
      "Description", ["A dotdict ('__getattr__' style) with purely numeric keys is still detected (1st review finding).",]
   )
   def test_NumericKeysGetAttrStyle(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CGetAttrDotDict({1: "A", 2: "B"})
      assert _IsDotDictLike(oData) is True

   @pytest.mark.parametrize(
      "Description", ["An empty dotdict ('__getattr__' style) is still detected via the class-level fallback.",]
   )
   def test_EmptyGetAttrStyle(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CGetAttrDotDict({})
      assert _IsDotDictLike(oData) is True

   @pytest.mark.parametrize(
      "Description", ["An empty dotdict ('self.__dict__ = self' style) is a documented, known limitation (no key left to probe).",]
   )
   def test_EmptySelfDictStyle_KnownLimitation(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CSelfDictDotDict({})
      # no key available to behaviorally probe, and there is no '__getattr__' override to fall
      # back on either -> this specific combination is a documented, known limitation.
      assert _IsDotDictLike(oData) is False

   @pytest.mark.parametrize(
      "Description", ["A key colliding with a class attribute/method name (e.g. 'keys') is skipped in favor of a usable key.",]
   )
   def test_KeyCollisionWithClassMethod(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CGetAttrDotDict({"keys": 1, "K2": 2})
      assert _IsDotDictLike(oData) is True

   @pytest.mark.parametrize(
      "Description", ["A first value of float('nan') is detected via object identity, not value equality (3rd review finding).",]
   )
   def test_NaNFirstValue(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CGetAttrDotDict({"K1": float("nan"), "K2": 2})
      assert _IsDotDictLike(oData) is True

   @pytest.mark.parametrize(
      "Description", ["A first value of Decimal('sNaN') does not raise InvalidOperation and is still detected (3rd review finding).",]
   )
   def test_SignalingNaNFirstValue_DoesNotRaise(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CGetAttrDotDict({"K1": decimal.Decimal("sNaN"), "K2": 2})
      assert _IsDotDictLike(oData) is True

   @pytest.mark.parametrize(
      "Description", ["A Mapping with a first value of float('nan') that does not forward attributes stays 'not dotdict-like' (no new false positive).",]
   )
   def test_NaNFirstValue_PlainMapping_NotAffected(self, Description):
      """pytest '_IsDotDictLike'"""
      oData = CPlainMapping({"K1": float("nan"), "K2": 2})
      assert _IsDotDictLike(oData) is False

# eof class Test_IsDotDictLike

# --------------------------------------------------------------------------------------------------------------

class Test_PrettyPrint_TypeDetection:
   """Tests of CUtils function 'PrettyPrint' regarding dotdict/mapping type detection."""

   # --------------------------------------------------------------------------------------------------------------

   @pytest.mark.parametrize(
      "Description", ["A '__getattr__'-style dotdict is rendered as '[DOTDICT]'.",]
   )
   def test_PrettyPrint_GetAttrDotDict(self, Description):
      """pytest 'PrettyPrint'"""
      oData = CGetAttrDotDict({"K1": 4, "K2": "ABC"})
      listOutLines = PrettyPrint(oData, bToConsole=False)
      sRet = "\n".join(listOutLines)
      listExpected = []
      listExpected.append("[DOTDICT] (2/1) > {K1} [INT]  :  4")
      listExpected.append("[DOTDICT] (2/2) > {K2} [STR]  :  'ABC'")
      sExp = "\n".join(listExpected)
      assert sRet == sExp

   @pytest.mark.parametrize(
      "Description", ["A 'self.__dict__ = self'-style dotdict is rendered as '[DOTDICT]'.",]
   )
   def test_PrettyPrint_SelfDictDotDict(self, Description):
      """pytest 'PrettyPrint'"""
      oData = CSelfDictDotDict({"K1": 4, "K2": "ABC"})
      listOutLines = PrettyPrint(oData, bToConsole=False)
      sRet = "\n".join(listOutLines)
      listExpected = []
      listExpected.append("[DOTDICT] (2/1) > {K1} [INT]  :  4")
      listExpected.append("[DOTDICT] (2/2) > {K2} [STR]  :  'ABC'")
      sExp = "\n".join(listExpected)
      assert sRet == sExp

   @pytest.mark.parametrize(
      "Description", ["A Mapping without attribute forwarding is rendered as '[MAPPING]', not '[DOTDICT]'.",]
   )
   def test_PrettyPrint_PlainMapping(self, Description):
      """pytest 'PrettyPrint'"""
      oData = CPlainMapping({"K1": 4, "K2": "ABC"})
      listOutLines = PrettyPrint(oData, bToConsole=False)
      sRet = "\n".join(listOutLines)
      listExpected = []
      listExpected.append("[MAPPING] (2/1) > {K1} [INT]  :  4")
      listExpected.append("[MAPPING] (2/2) > {K2} [STR]  :  'ABC'")
      sExp = "\n".join(listExpected)
      assert sRet == sExp

   @pytest.mark.parametrize(
      "Description", ["An 'OrderedDict' (a generic Mapping, not a plain dict) is rendered as '[MAPPING]'.",]
   )
   def test_PrettyPrint_OrderedDict(self, Description):
      """pytest 'PrettyPrint'"""
      import collections
      oData = collections.OrderedDict()
      oData["K1"] = 4
      oData["K2"] = "ABC"
      listOutLines = PrettyPrint(oData, bToConsole=False)
      sRet = "\n".join(listOutLines)
      listExpected = []
      listExpected.append("[MAPPING] (2/1) > {K1} [INT]  :  4")
      listExpected.append("[MAPPING] (2/2) > {K2} [STR]  :  'ABC'")
      sExp = "\n".join(listExpected)
      assert sRet == sExp

   @pytest.mark.parametrize(
      "Description", ["A dotdict with a first value of float('nan') is rendered correctly and still classified as '[DOTDICT]'.",]
   )
   def test_PrettyPrint_NaNFirstValue(self, Description):
      """pytest 'PrettyPrint'"""
      oData = CGetAttrDotDict({"K1": float("nan"), "K2": 2})
      listOutLines = PrettyPrint(oData, bToConsole=False)
      sRet = "\n".join(listOutLines)
      assert sRet.startswith("[DOTDICT] (2/1) > {K1} [FLOAT]  :  nan")
      assert "[DOTDICT] (2/2) > {K2} [INT]  :  2" in sRet

   @pytest.mark.parametrize(
      "Description", ["A dotdict with a first value of Decimal('sNaN') is printed without raising InvalidOperation.",]
   )
   def test_PrettyPrint_SignalingNaNFirstValue_DoesNotRaise(self, Description):
      """pytest 'PrettyPrint'"""
      oData = CGetAttrDotDict({"K1": decimal.Decimal("sNaN"), "K2": 2})
      listOutLines = PrettyPrint(oData, bToConsole=False) # must not raise decimal.InvalidOperation
      sRet = "\n".join(listOutLines)
      assert sRet.startswith("[DOTDICT] (2/1) > {K1}")
      assert "[DOTDICT] (2/2) > {K2} [INT]  :  2" in sRet

   @pytest.mark.parametrize(
      "Description", ["An empty dotdict ('__getattr__' style) is rendered as '[DOTDICT]  :  {}'.",]
   )
   def test_PrettyPrint_EmptyGetAttrDotDict(self, Description):
      """pytest 'PrettyPrint'"""
      oData = CGetAttrDotDict({})
      listOutLines = PrettyPrint(oData, bToConsole=False)
      sRet = "\n".join(listOutLines)
      assert sRet == "[DOTDICT]  :  {}"

# eof class Test_PrettyPrint_TypeDetection

# --------------------------------------------------------------------------------------------------------------
