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
# test_05_CSTRING_GOODCASE.py
#
# XC-CT/ECA3-Queckenstedt
#
# 14.08.2023 - 14:52:59
#
# --------------------------------------------------------------------------------------------------------------

import pytest
from pytestlibs.CExecute import CExecute

# --------------------------------------------------------------------------------------------------------------

class Test_CSTRING_GOODCASE:

# --------------------------------------------------------------------------------------------------------------
   # Expected: String with resolved environment variable is not expected to be the same as the input string
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Resolve environment variables",]
   )
   def test_PEC_0200(self, Description):
      nReturn = CExecute.Execute("PEC_0200")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: String with environment variable is returned unresolved
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Resolving of environment variables deactivated",]
   )
   def test_PEC_0201(self, Description):
      nReturn = CExecute.Execute("PEC_0201")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: All backslashes replaced by single slashes
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Convert backslashes",]
   )
   def test_PEC_0202(self, Description):
      nReturn = CExecute.Execute("PEC_0202")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Surrounding quotes and spaces are removed
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Strip surrounding quotes and spaces",]
   )
   def test_PEC_0203(self, Description):
      nReturn = CExecute.Execute("PEC_0203")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Redundant path separators removed; all backslashes replaced by single slashes
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Path with redundant path separators",]
   )
   def test_PEC_0204(self, Description):
      nReturn = CExecute.Execute("PEC_0204")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Redundant path separators removed; remaining separators are masked backslashes
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Path with redundant path separators; bWin=True",]
   )
   def test_PEC_0205(self, Description):
      nReturn = CExecute.Execute("PEC_0205")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: All backslashes replaced by single slashes; up-level references resolved
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Path with up-level references",]
   )
   def test_PEC_0206(self, Description):
      nReturn = CExecute.Execute("PEC_0206")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: All slashes replaced by double (masked) backslashes; up-level references resolved
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Path with up-level references; bWin=True",]
   )
   def test_PEC_0207(self, Description):
      nReturn = CExecute.Execute("PEC_0207")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: All slashes replaced by single (unmasked) backslashes; up-level references resolved
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Path with up-level references; bWin=True; bMask=False",]
   )
   def test_PEC_0208(self, Description):
      nReturn = CExecute.Execute("PEC_0208")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Resulting absolute path is a merge of the absolute reference path and the relative input path; single slashes as separator
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Relative input path with absolute reference path",]
   )
   def test_PEC_0209(self, Description):
      nReturn = CExecute.Execute("PEC_0209")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Resulting absolute path is a merge of the absolute reference path and the relative input path; masked backslashes as separator
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Relative input path with absolute reference path; bWin=True; bMask=True",]
   )
   def test_PEC_0210(self, Description):
      nReturn = CExecute.Execute("PEC_0210")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Paths with blanks inside are encapsulated in quotes; single slashes as separator; up-level references resolved
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Path with blanks inside; bConsiderBlanks=True",]
   )
   def test_PEC_0211(self, Description):
      nReturn = CExecute.Execute("PEC_0211")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Paths without blanks inside are not encapsulated in quotes; single slashes as separator
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Path without blanks inside; bConsiderBlanks=True",]
   )
   def test_PEC_0212(self, Description):
      nReturn = CExecute.Execute("PEC_0212")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Resulting local network resource path contains single slashes as separator
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Local network resource paths",]
   )
   def test_PEC_0213(self, Description):
      nReturn = CExecute.Execute("PEC_0213")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Resulting local network resource path (web browser format) contains single slashes as separator; bWin has no effect
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Local network resource paths in web browser format",]
   )
   def test_PEC_0214(self, Description):
      nReturn = CExecute.Execute("PEC_0214")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Resulting internet address contains single backslashes as separator; bWin has no effect
   @pytest.mark.parametrize(
      "Description", ["NormalizePath: Internet addresses",]
   )
   def test_PEC_0215(self, Description):
      nReturn = CExecute.Execute("PEC_0215")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
