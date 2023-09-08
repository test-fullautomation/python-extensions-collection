# **************************************************************************************************************
#  Copyright 2020-2023 Robert Bosch GmbH
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
# test_06_CCOMPARISON_GOODCASE.py
#
# XC-CT/ECA3-Queckenstedt
#
# 08.09.2023 - 13:42:17
#
# --------------------------------------------------------------------------------------------------------------

import pytest
from pytestlibs.CExecute import CExecute

# --------------------------------------------------------------------------------------------------------------

class Test_CCOMPARISON_GOODCASE:

# --------------------------------------------------------------------------------------------------------------
   # Expected: Result: Files have same content
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with same content; no pattern)",]
   )
   def test_PEC_0600(self, Description):
      nReturn = CExecute.Execute("PEC_0600")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Result: Files have different content
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with different content; no pattern)",]
   )
   def test_PEC_0601(self, Description):
      nReturn = CExecute.Execute("PEC_0601")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Result: Files have same content
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with same content; with pattern)",]
   )
   def test_PEC_0602(self, Description):
      nReturn = CExecute.Execute("PEC_0602")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Result: Files have different content
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with different content; with pattern)",]
   )
   def test_PEC_0603(self, Description):
      nReturn = CExecute.Execute("PEC_0603")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Result: Files have same content (because the different lines are ignored)
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with different content; with pattern and ignore pattern)",]
   )
   def test_PEC_0604(self, Description):
      nReturn = CExecute.Execute("PEC_0604")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
