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
# test_08_CUTILS_GOODCASE.py
#
# XC-HWP/ESW3-Queckenstedt
#
# 08.09.2023 - 17:36:34
#
# --------------------------------------------------------------------------------------------------------------

import pytest
from pytestlibs.CExecute import CExecute

# --------------------------------------------------------------------------------------------------------------

class Test_CUTILS_GOODCASE:

# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'int'",]
   )
   def test_PEC_0700(self, Description):
      nReturn = CExecute.Execute("PEC_0700")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'float'",]
   )
   def test_PEC_0701(self, Description):
      nReturn = CExecute.Execute("PEC_0701")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'str'",]
   )
   def test_PEC_0702(self, Description):
      nReturn = CExecute.Execute("PEC_0702")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'bool'",]
   )
   def test_PEC_0703(self, Description):
      nReturn = CExecute.Execute("PEC_0703")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'None'",]
   )
   def test_PEC_0704(self, Description):
      nReturn = CExecute.Execute("PEC_0704")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'list'",]
   )
   def test_PEC_0705(self, Description):
      nReturn = CExecute.Execute("PEC_0705")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'tuple'",]
   )
   def test_PEC_0706(self, Description):
      nReturn = CExecute.Execute("PEC_0706")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'set'",]
   )
   def test_PEC_0707(self, Description):
      nReturn = CExecute.Execute("PEC_0707")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'dict'",]
   )
   def test_PEC_0708(self, Description):
      nReturn = CExecute.Execute("PEC_0708")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'dotdict'",]
   )
   def test_PEC_0709(self, Description):
      nReturn = CExecute.Execute("PEC_0709")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of nested types",]
   )
   def test_PEC_0710(self, Description):
      nReturn = CExecute.Execute("PEC_0710")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'list'; output indented by 5 blanks",]
   )
   def test_PEC_0711(self, Description):
      nReturn = CExecute.Execute("PEC_0711")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of type 'list'; output indented by 2 blanks and with prefix",]
   )
   def test_PEC_0712(self, Description):
      nReturn = CExecute.Execute("PEC_0712")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Input parameter is pretty printed
   @pytest.mark.parametrize(
      "Description", ["PrettyPrint: Input parameter of nested types; output indented by 2 blanks and with prefix; strings in hexadecimal format",]
   )
   def test_PEC_0713(self, Description):
      nReturn = CExecute.Execute("PEC_0713")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: List of installed Python packages created
   @pytest.mark.parametrize(
      "Description", ["GetInstalledPackages: Default usage",]
   )
   def test_PEC_0800(self, Description):
      nReturn = CExecute.Execute("PEC_0800")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: List of installed Python packages created and written to output file
   @pytest.mark.parametrize(
      "Description", ["GetInstalledPackages: List written to output file",]
   )
   def test_PEC_0801(self, Description):
      nReturn = CExecute.Execute("PEC_0801")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
