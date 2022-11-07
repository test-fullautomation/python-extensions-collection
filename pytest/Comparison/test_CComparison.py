#  Copyright 2020-2022 Robert Bosch GmbH
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
# test_CComparison.py
#
# XC-CT/ECA3-Queckenstedt
#
# 25.10.2022
#
# --------------------------------------------------------------------------------------------------------------

# -- import standard Python modules
import os, sys, time, platform, pytest

# -- import own Python modules (containing the code to be tested)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))) # to make sure to hit the package relative to this file at first
from PythonExtensionsCollection.String.CString import CString
from PythonExtensionsCollection.Comparison.CComparison import CComparison

# --------------------------------------------------------------------------------------------------------------

class Test_CComparison:
   """Tests of module CComparison."""

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with same content; no pattern)",]
   )
   def test_Compare_1(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/01.File_1.A.txt")
      sFile_2        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/02.File_2.A.txt")
      print(f"sFile_1: '{sFile_1}'")
      print(f"sFile_2: '{sFile_2}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is True
      assert bSuccess is True
   # eof def test_Compare_1(self, Description):

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with different content; no pattern)",]
   )
   def test_Compare_2(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/03.File_1.B.txt")
      sFile_2        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/04.File_2.B.txt")
      print(f"sFile_1: '{sFile_1}'")
      print(f"sFile_2: '{sFile_2}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is False
      assert bSuccess is True
   # eof def test_Compare_2(self, Description):

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with same content; with pattern)",]
   )
   def test_Compare_3(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/03.File_1.B.txt")
      sFile_2        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/04.File_2.B.txt")
      sPatternFile   = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/10.PatternFile.txt")
      print(f"sFile_1     : '{sFile_1}'")
      print(f"sFile_2     : '{sFile_2}'")
      print(f"sPatternFile: '{sPatternFile}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is True
      assert bSuccess is True
   # eof def test_Compare_3(self, Description):

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with different content; with pattern)",]
   )
   def test_Compare_4(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/03.File_1.B.txt")
      sFile_2        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/05.File_2.C.txt")
      sPatternFile   = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/10.PatternFile.txt")
      print(f"sFile_1     : '{sFile_1}'")
      print(f"sFile_2     : '{sFile_2}'")
      print(f"sPatternFile: '{sPatternFile}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is False
      assert bSuccess is True
   # eof def test_Compare_4(self, Description):

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with same path and name) - bad case",]
   )
   def test_Compare_5(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/03.File_1.B.txt")
      sFile_2        = sFile_1
      sPatternFile   = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/10.PatternFile.txt")
      print(f"sFile_1     : '{sFile_1}'")
      print(f"sFile_2     : '{sFile_2}'")
      print(f"sPatternFile: '{sPatternFile}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is None
      assert bSuccess is False
   # eof def test_Compare_5(self, Description):

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (first file not given) - bad case",]
   )
   def test_Compare_6(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = None
      sFile_2        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/02.File_2.A.txt")
      sPatternFile   = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/10.PatternFile.txt")
      print(f"sFile_1     : '{sFile_1}'")
      print(f"sFile_2     : '{sFile_2}'")
      print(f"sPatternFile: '{sPatternFile}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is None
      assert bSuccess is False
   # eof def test_Compare_6(self, Description):

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (second file not given) - bad case",]
   )
   def test_Compare_7(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/01.File_1.A.txt")
      sFile_2        = None
      sPatternFile   = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/10.PatternFile.txt")
      print(f"sFile_1     : '{sFile_1}'")
      print(f"sFile_2     : '{sFile_2}'")
      print(f"sPatternFile: '{sPatternFile}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is None
      assert bSuccess is False
   # eof def test_Compare_7(self, Description):

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (first file not existing) - bad case",]
   )
   def test_Compare_8(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/IAmNotExisting.txt")
      sFile_2        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/02.File_2.A.txt")
      sPatternFile   = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/10.PatternFile.txt")
      print(f"sFile_1     : '{sFile_1}'")
      print(f"sFile_2     : '{sFile_2}'")
      print(f"sPatternFile: '{sPatternFile}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is None
      assert bSuccess is False
   # eof def test_Compare_8(self, Description):

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (second file not existing) - bad case",]
   )
   def test_Compare_9(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/01.File_1.A.txt")
      sFile_2        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/IAmNotExisting.txt")
      sPatternFile   = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/10.PatternFile.txt")
      print(f"sFile_1     : '{sFile_1}'")
      print(f"sFile_2     : '{sFile_2}'")
      print(f"sPatternFile: '{sPatternFile}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is None
      assert bSuccess is False
   # eof def test_Compare_9(self, Description):

   # --------------------------------------------------------------------------------------------------------------
   #TM***
   @pytest.mark.parametrize(
      "Description", ["Compare two files (pattern file not existing) - bad case",]
   )
   def test_Compare_10(self, Description):
      """pytest 'CComparison'"""

      sReferencePath = os.path.dirname(os.path.dirname(CString.NormalizePath(__file__)))
      sFile_1        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/01.File_1.A.txt")
      sFile_2        = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/02.File_2.A.txt")
      sPatternFile   = CString.NormalizePath(f"{sReferencePath}/testfiles/Comparison/IAmNotExisting.txt")
      print(f"sFile_1     : '{sFile_1}'")
      print(f"sFile_2     : '{sFile_2}'")
      print(f"sPatternFile: '{sPatternFile}'")

      oComparison = CComparison()
      bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
      del oComparison
      print(f"bIdentical: '{bIdentical}'")
      print(f"bSuccess  : '{bSuccess}'")
      print(f"sResult   : '{sResult}'")
      assert bIdentical is None
      assert bSuccess is False
   # eof def test_Compare_10(self, Description):

# eof class Test_CComparison

# --------------------------------------------------------------------------------------------------------------
