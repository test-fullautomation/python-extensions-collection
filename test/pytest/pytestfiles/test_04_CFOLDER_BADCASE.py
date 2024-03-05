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
# test_04_CFOLDER_BADCASE.py
#
# XC-HWP/ESW3-Queckenstedt
#
# 11.08.2023 - 16:41:27
#
# --------------------------------------------------------------------------------------------------------------

import pytest
from pytestlibs.CExecute import CExecute

# --------------------------------------------------------------------------------------------------------------

class Test_CFOLDER_BADCASE:

# --------------------------------------------------------------------------------------------------------------
   # Expected: Nothing is copied; error message
   @pytest.mark.parametrize(
      "Description", ["Copy a folder, source and destination are same folder",]
   )
   def test_PEC_0150(self, Description):
      nReturn = CExecute.Execute("PEC_0150")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Nothing is copied; error message
   @pytest.mark.parametrize(
      "Description", ["Copy a folder, destination path does not exist",]
   )
   def test_PEC_0151(self, Description):
      nReturn = CExecute.Execute("PEC_0151")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Nothing is copied; error message
   @pytest.mark.parametrize(
      "Description", ["Copy a folder, destination folder already in use by another instance",]
   )
   def test_PEC_0152(self, Description):
      nReturn = CExecute.Execute("PEC_0152")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Nothing is copied; error message
   @pytest.mark.parametrize(
      "Description", ["Copy a folder, source folder does not exist",]
   )
   def test_PEC_0153(self, Description):
      nReturn = CExecute.Execute("PEC_0153")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Windows: Access violation; not possible to delete the folder (BADCASE) / Linux: Folder is deleted (GOODCASE)
   @pytest.mark.parametrize(
      "Description", ["Create a folder, bOverwrite=True, open file handle",]
   )
   def test_PEC_0154(self, Description):
      nReturn = CExecute.Execute("PEC_0154")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Error message
   @pytest.mark.parametrize(
      "Description", ["Multiple CFolder instances of same folder",]
   )
   def test_PEC_0155(self, Description):
      nReturn = CExecute.Execute("PEC_0155")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
