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
# test_02_CFILE_BADCASE.py
#
# XC-CT/ECA3-Queckenstedt
#
# 07.08.2023 - 16:19:07
#
# --------------------------------------------------------------------------------------------------------------

import pytest
from pytestlibs.CExecute import CExecute

# --------------------------------------------------------------------------------------------------------------

class Test_CFILE_BADCASE:

# --------------------------------------------------------------------------------------------------------------
   # Expected: Source file not written, not deleted, not copied, not moved
   @pytest.mark.parametrize(
      "Description", ["Path to source file does not exist",]
   )
   def test_PEC_0050(self, Description):
      nReturn = CExecute.Execute("PEC_0050")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Source file not copied and not moved to destination
   @pytest.mark.parametrize(
      "Description", ["Path to destination file does not exist",]
   )
   def test_PEC_0051(self, Description):
      nReturn = CExecute.Execute("PEC_0051")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Source file not copied and not moved to destination
   @pytest.mark.parametrize(
      "Description", ["source file == destination file",]
   )
   def test_PEC_0052(self, Description):
      nReturn = CExecute.Execute("PEC_0052")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Existing files are not overwritten, if not allowed; no multiple class instances pointing to the same file
   @pytest.mark.parametrize(
      "Description", ["bOverwrite and access violations",]
   )
   def test_PEC_0053(self, Description):
      nReturn = CExecute.Execute("PEC_0053")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
