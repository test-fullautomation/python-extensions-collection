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
# test_01_CFILE_GOODCASE.py
#
# XC-CT/ECA3-Queckenstedt
#
# 07.08.2023 - 16:19:07
#
# --------------------------------------------------------------------------------------------------------------

import pytest
from pytestlibs.CExecute import CExecute

# --------------------------------------------------------------------------------------------------------------

class Test_CFILE_GOODCASE:

# --------------------------------------------------------------------------------------------------------------
   # Expected: Teststring is written to file and read from this file
   @pytest.mark.parametrize(
      "Description", ["Write and Read with explicit Close",]
   )
   def test_PEC_0001(self, Description):
      nReturn = CExecute.Execute("PEC_0001")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Teststring is written to file and read from this file
   @pytest.mark.parametrize(
      "Description", ["Write and Read without explicit Close",]
   )
   def test_PEC_0002(self, Description):
      nReturn = CExecute.Execute("PEC_0002")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: File is deleted
   @pytest.mark.parametrize(
      "Description", ["Delete a file",]
   )
   def test_PEC_0003(self, Description):
      nReturn = CExecute.Execute("PEC_0003")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Lines are appended and read
   @pytest.mark.parametrize(
      "Description", ["Append and Read with explicit Close",]
   )
   def test_PEC_0004(self, Description):
      nReturn = CExecute.Execute("PEC_0004")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Lines are appended and read
   @pytest.mark.parametrize(
      "Description", ["Append and Read without explicit Close",]
   )
   def test_PEC_0005(self, Description):
      nReturn = CExecute.Execute("PEC_0005")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Lines are read depending on filter settings
   @pytest.mark.parametrize(
      "Description", ["Write to new file; repeated ReadLines with filter",]
   )
   def test_PEC_0006(self, Description):
      nReturn = CExecute.Execute("PEC_0006")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Lines are read depending on filter settings
   @pytest.mark.parametrize(
      "Description", ["ReadLines; skip blank lines",]
   )
   def test_PEC_0007(self, Description):
      nReturn = CExecute.Execute("PEC_0007")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Lines are read depending on previous Write or Append
   @pytest.mark.parametrize(
      "Description", ["Write, Append and ReadLines combinations",]
   )
   def test_PEC_0008(self, Description):
      nReturn = CExecute.Execute("PEC_0008")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Content of composite data is resolved and written to file line by line separately
   @pytest.mark.parametrize(
      "Description", ["Write and ReadLines of composite data types: list, tuple, set and dict",]
   )
   def test_PEC_0009(self, Description):
      nReturn = CExecute.Execute("PEC_0009")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Prefix and additional vertical space are added to written content
   @pytest.mark.parametrize(
      "Description", ["Write: Prefix and additional vertical space",]
   )
   def test_PEC_0010(self, Description):
      nReturn = CExecute.Execute("PEC_0010")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: File is copied, moved and file info is correct
   @pytest.mark.parametrize(
      "Description", ["CopyTo, MoveTo and GetFileInfo",]
   )
   def test_PEC_0011(self, Description):
      nReturn = CExecute.Execute("PEC_0011")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returns True or False depending on deletion has to be confirmed or not
   @pytest.mark.parametrize(
      "Description", ["ConfirmDelete",]
   )
   def test_PEC_0012(self, Description):
      nReturn = CExecute.Execute("PEC_0012")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
