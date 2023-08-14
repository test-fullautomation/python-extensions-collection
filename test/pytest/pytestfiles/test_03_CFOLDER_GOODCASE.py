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
# test_03_CFOLDER_GOODCASE.py
#
# XC-CT/ECA3-Queckenstedt
#
# 11.08.2023 - 16:41:27
#
# --------------------------------------------------------------------------------------------------------------

import pytest
from pytestlibs.CExecute import CExecute

# --------------------------------------------------------------------------------------------------------------

class Test_CFOLDER_GOODCASE:

# --------------------------------------------------------------------------------------------------------------
   # Expected: New folder is created, but existing folder is not overwritten
   @pytest.mark.parametrize(
      "Description", ["Create a folder, bOverwrite=False",]
   )
   def test_PEC_0100(self, Description):
      nReturn = CExecute.Execute("PEC_0100")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: New folder is created, existing folder is overwritten
   @pytest.mark.parametrize(
      "Description", ["Create a folder, bOverwrite=True",]
   )
   def test_PEC_0101(self, Description):
      nReturn = CExecute.Execute("PEC_0101")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Entire path to folder is created; folder is deleted
   @pytest.mark.parametrize(
      "Description", ["Create and delete a folder, bRecursive=True",]
   )
   def test_PEC_0102(self, Description):
      nReturn = CExecute.Execute("PEC_0102")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Write protection is removed, folder is deleted
   @pytest.mark.parametrize(
      "Description", ["Delete a folder with content write protected",]
   )
   def test_PEC_0103(self, Description):
      nReturn = CExecute.Execute("PEC_0103")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Folder is copied
   @pytest.mark.parametrize(
      "Description", ["Copy a folder",]
   )
   def test_PEC_0104(self, Description):
      nReturn = CExecute.Execute("PEC_0104")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Destination folder is overwritten or not, depending on bOverwrite
   @pytest.mark.parametrize(
      "Description", ["Copy a folder, destination folder already exists",]
   )
   def test_PEC_0105(self, Description):
      nReturn = CExecute.Execute("PEC_0105")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
