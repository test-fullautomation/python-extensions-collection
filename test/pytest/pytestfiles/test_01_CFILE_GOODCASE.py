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
# 03.08.2023 - 18:07:22
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
