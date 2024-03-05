# **************************************************************************************************************
#  Copyright 2020-2024 Robert Bosch GmbH
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
# test_07_CCOMPARISON_BADCASE.py
#
# XC-HWP/ESW3-Queckenstedt
#
# 08.09.2023 - 13:42:17
#
# --------------------------------------------------------------------------------------------------------------

import pytest
from pytestlibs.CExecute import CExecute

# --------------------------------------------------------------------------------------------------------------

class Test_CCOMPARISON_BADCASE:

# --------------------------------------------------------------------------------------------------------------
   # Expected: No comparison; error message instead
   @pytest.mark.parametrize(
      "Description", ["Compare two files (with same path and name)",]
   )
   def test_PEC_0650(self, Description):
      nReturn = CExecute.Execute("PEC_0650")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: No comparison; error message instead
   @pytest.mark.parametrize(
      "Description", ["Compare two files (first file not given)",]
   )
   def test_PEC_0651(self, Description):
      nReturn = CExecute.Execute("PEC_0651")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: No comparison; error message instead
   @pytest.mark.parametrize(
      "Description", ["Compare two files (second file not given)",]
   )
   def test_PEC_0652(self, Description):
      nReturn = CExecute.Execute("PEC_0652")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: No comparison; error message instead
   @pytest.mark.parametrize(
      "Description", ["Compare two files (first file not existing)",]
   )
   def test_PEC_0653(self, Description):
      nReturn = CExecute.Execute("PEC_0653")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: No comparison; error message instead
   @pytest.mark.parametrize(
      "Description", ["Compare two files (second file not existing)",]
   )
   def test_PEC_0654(self, Description):
      nReturn = CExecute.Execute("PEC_0654")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: No comparison; error message instead
   @pytest.mark.parametrize(
      "Description", ["Compare two files (pattern file not existing)",]
   )
   def test_PEC_0655(self, Description):
      nReturn = CExecute.Execute("PEC_0655")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: No comparison; error message instead
   @pytest.mark.parametrize(
      "Description", ["Compare two files (ignore pattern file not existing)",]
   )
   def test_PEC_0656(self, Description):
      nReturn = CExecute.Execute("PEC_0656")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
