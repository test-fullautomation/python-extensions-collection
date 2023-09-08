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
# 08.09.2023 - 13:42:17
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
   # Expected: Path to folder found within start path
   @pytest.mark.parametrize(
      "Description", ["DetectParentPath: Search for a single folder",]
   )
   def test_PEC_0300(self, Description):
      nReturn = CExecute.Execute("PEC_0300")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Expected paths detected one and two levels up
   @pytest.mark.parametrize(
      "Description", ["DetectParentPath: Search for two folders",]
   )
   def test_PEC_0301(self, Description):
      nReturn = CExecute.Execute("PEC_0301")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Expected path to existing folder detected one level up
   @pytest.mark.parametrize(
      "Description", ["DetectParentPath: Search for two folders; with one folder does not exist",]
   )
   def test_PEC_0302(self, Description):
      nReturn = CExecute.Execute("PEC_0302")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: No path detected
   @pytest.mark.parametrize(
      "Description", ["DetectParentPath: Search for two folders; both folders do not exist",]
   )
   def test_PEC_0303(self, Description):
      nReturn = CExecute.Execute("PEC_0303")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Expected path to folder detected one level up; one file found
   @pytest.mark.parametrize(
      "Description", ["DetectParentPath: Search for a single folder; additionally search for a file",]
   )
   def test_PEC_0304(self, Description):
      nReturn = CExecute.Execute("PEC_0304")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Expected path to folder detected one level up; file not found
   @pytest.mark.parametrize(
      "Description", ["DetectParentPath: Search for a single folder; additionally search for a file",]
   )
   def test_PEC_0305(self, Description):
      nReturn = CExecute.Execute("PEC_0305")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Skip blank strings",]
   )
   def test_PEC_0400(self, Description):
      nReturn = CExecute.Execute("PEC_0400")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Blank strings not skipped",]
   )
   def test_PEC_0401(self, Description):
      nReturn = CExecute.Execute("PEC_0401")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String commented out (1)",]
   )
   def test_PEC_0402(self, Description):
      nReturn = CExecute.Execute("PEC_0402")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String commented out (2)",]
   )
   def test_PEC_0403(self, Description):
      nReturn = CExecute.Execute("PEC_0403")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String commented out (3)",]
   )
   def test_PEC_0404(self, Description):
      nReturn = CExecute.Execute("PEC_0404")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String commented out (4)",]
   )
   def test_PEC_0405(self, Description):
      nReturn = CExecute.Execute("PEC_0405")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String commented out (5)",]
   )
   def test_PEC_0406(self, Description):
      nReturn = CExecute.Execute("PEC_0406")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String commented out (6)",]
   )
   def test_PEC_0407(self, Description):
      nReturn = CExecute.Execute("PEC_0407")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String starts with ...",]
   )
   def test_PEC_0408(self, Description):
      nReturn = CExecute.Execute("PEC_0408")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String ends with ...",]
   )
   def test_PEC_0409(self, Description):
      nReturn = CExecute.Execute("PEC_0409")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String starts not with ...",]
   )
   def test_PEC_0410(self, Description):
      nReturn = CExecute.Execute("PEC_0410")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String ends not with ...",]
   )
   def test_PEC_0411(self, Description):
      nReturn = CExecute.Execute("PEC_0411")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String contains ... (1)",]
   )
   def test_PEC_0412(self, Description):
      nReturn = CExecute.Execute("PEC_0412")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String contains ... (2)",]
   )
   def test_PEC_0413(self, Description):
      nReturn = CExecute.Execute("PEC_0413")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String contains ... and contains not ...",]
   )
   def test_PEC_0414(self, Description):
      nReturn = CExecute.Execute("PEC_0414")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: String contains not ...",]
   )
   def test_PEC_0415(self, Description):
      nReturn = CExecute.Execute("PEC_0415")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations; case sensitive",]
   )
   def test_PEC_0416(self, Description):
      nReturn = CExecute.Execute("PEC_0416")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations; not case sensitive",]
   )
   def test_PEC_0417(self, Description):
      nReturn = CExecute.Execute("PEC_0417")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Inclusive by regular expression (1)",]
   )
   def test_PEC_0418(self, Description):
      nReturn = CExecute.Execute("PEC_0418")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Inclusive by regular expression (2)",]
   )
   def test_PEC_0419(self, Description):
      nReturn = CExecute.Execute("PEC_0419")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations (1)",]
   )
   def test_PEC_0420(self, Description):
      nReturn = CExecute.Execute("PEC_0420")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations (2)",]
   )
   def test_PEC_0421(self, Description):
      nReturn = CExecute.Execute("PEC_0421")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations (3)",]
   )
   def test_PEC_0422(self, Description):
      nReturn = CExecute.Execute("PEC_0422")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations (4)",]
   )
   def test_PEC_0423(self, Description):
      nReturn = CExecute.Execute("PEC_0423")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Exclusive by regular expression (1)",]
   )
   def test_PEC_0424(self, Description):
      nReturn = CExecute.Execute("PEC_0424")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Exclusive by regular expression (2)",]
   )
   def test_PEC_0425(self, Description):
      nReturn = CExecute.Execute("PEC_0425")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations (5)",]
   )
   def test_PEC_0426(self, Description):
      nReturn = CExecute.Execute("PEC_0426")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations (6)",]
   )
   def test_PEC_0427(self, Description):
      nReturn = CExecute.Execute("PEC_0427")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations (7)",]
   )
   def test_PEC_0428(self, Description):
      nReturn = CExecute.Execute("PEC_0428")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter combinations (8)",]
   )
   def test_PEC_0429(self, Description):
      nReturn = CExecute.Execute("PEC_0429")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Handling of blanks (1)",]
   )
   def test_PEC_0430(self, Description):
      nReturn = CExecute.Execute("PEC_0430")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Handling of blanks (2)",]
   )
   def test_PEC_0431(self, Description):
      nReturn = CExecute.Execute("PEC_0431")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter string lists (1)",]
   )
   def test_PEC_0432(self, Description):
      nReturn = CExecute.Execute("PEC_0432")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter string lists (2)",]
   )
   def test_PEC_0433(self, Description):
      nReturn = CExecute.Execute("PEC_0433")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter string lists (3)",]
   )
   def test_PEC_0434(self, Description):
      nReturn = CExecute.Execute("PEC_0434")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter string lists (4)",]
   )
   def test_PEC_0435(self, Description):
      nReturn = CExecute.Execute("PEC_0435")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter string lists (5)",]
   )
   def test_PEC_0436(self, Description):
      nReturn = CExecute.Execute("PEC_0436")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: False
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter string lists (6)",]
   )
   def test_PEC_0437(self, Description):
      nReturn = CExecute.Execute("PEC_0437")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Returned: True
   @pytest.mark.parametrize(
      "Description", ["StringFilter: Filter string lists (7)",]
   )
   def test_PEC_0438(self, Description):
      nReturn = CExecute.Execute("PEC_0438")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Message formatted as success, with method
   @pytest.mark.parametrize(
      "Description", ["FormatResult: Success (1)",]
   )
   def test_PEC_0500(self, Description):
      nReturn = CExecute.Execute("PEC_0500")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Message formatted as success, without method
   @pytest.mark.parametrize(
      "Description", ["FormatResult: Success (2)",]
   )
   def test_PEC_0501(self, Description):
      nReturn = CExecute.Execute("PEC_0501")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Message formatted as error, with method
   @pytest.mark.parametrize(
      "Description", ["FormatResult: Error (1)",]
   )
   def test_PEC_0502(self, Description):
      nReturn = CExecute.Execute("PEC_0502")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Message formatted as error, without method
   @pytest.mark.parametrize(
      "Description", ["FormatResult: Error (2)",]
   )
   def test_PEC_0503(self, Description):
      nReturn = CExecute.Execute("PEC_0503")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Message formatted as exception, with method
   @pytest.mark.parametrize(
      "Description", ["FormatResult: Exception (1)",]
   )
   def test_PEC_0504(self, Description):
      nReturn = CExecute.Execute("PEC_0504")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
   # Expected: Message formatted as exception, without method
   @pytest.mark.parametrize(
      "Description", ["FormatResult: Exception (2)",]
   )
   def test_PEC_0505(self, Description):
      nReturn = CExecute.Execute("PEC_0505")
      assert nReturn == 0
# --------------------------------------------------------------------------------------------------------------
