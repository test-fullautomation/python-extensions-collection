#  Copyright 2020-2022 Robert Bosch GmbH
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
# test_CString.py
#
# XC-CT/ECA3-Queckenstedt
#
# 06.06.2023
#
# --------------------------------------------------------------------------------------------------------------

# -- import standard Python modules
import os, sys, time, pytest, platform

# -- import own Python modules (containing the code to be tested)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))) # to make sure to hit the package relative to this file at first
from PythonExtensionsCollection.File.CFile import CFile
from PythonExtensionsCollection.String.CString import CString

# --------------------------------------------------------------------------------------------------------------
#TM***

class Test_NormalizePath:
    """Tests of CString method 'NormalizePath'.
Because of access to environment variables and paths these tests are operating system depending."""

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["String with resolved environment variable is not expected to be the same as the input string.",]
    )
    def test_Windows_ExpandEnvVar_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"%RobotPythonPath%"
        sOut = CString.NormalizePath(sIn)
        assert sIn != sOut

    @pytest.mark.parametrize(
        "Description", ["String with resolved environment variable is not expected to be the same as the input string.",]
    )
    def test_Linux_ExpandEnvVar_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"${RobotPythonPath}"
        sOut = CString.NormalizePath(sIn)
        assert sIn != sOut

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["String with environment variable is returned unresolved.",]
    )
    def test_Windows_ExpandEnvVar_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"%RobotPythonPath%"
        sOut = CString.NormalizePath(sIn, bExpandEnvVars=False)
        assert sIn == sOut

    @pytest.mark.parametrize(
        "Description", ["String with environment variable is returned unresolved.",]
    )
    def test_Linux_ExpandEnvVar_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"${RobotPythonPath}"
        sOut = CString.NormalizePath(sIn, bExpandEnvVars=False)
        assert sIn == sOut

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["All backslashes replaced by single slashes.",]
    )
    def test_Windows_Separators_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"C:\dir\subdir\subsubdir"
        sOut = CString.NormalizePath(sIn)
        sExp = r"C:/dir/subdir/subsubdir"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["All backslashes replaced by single slashes.",]
    )
    def test_Linux_Separators_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"/tmp\dir\subdir\subsubdir"
        sOut = CString.NormalizePath(sIn)
        sExp = r"/tmp/dir/subdir/subsubdir"
        assert sOut == sExp

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["Surrounding quotes and spaces are removed (1).",]
    )
    def test_Windows_SurroundingChars_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r'  "  C:\dir\subdir\subsubdir  "  '
        sOut = CString.NormalizePath(sIn)
        sExp = r"C:/dir/subdir/subsubdir"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Surrounding quotes and spaces are removed (2).",]
    )
    def test_Windows_SurroundingChars_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"  '  C:\dir\subdir\subsubdir  '  "
        sOut = CString.NormalizePath(sIn)
        sExp = r"C:/dir/subdir/subsubdir"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Surrounding quotes and spaces are removed (1).",]
    )
    def test_Linux_SurroundingChars_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r'  " /tmp\dir\subdir\subsubdir  "  '
        sOut = CString.NormalizePath(sIn)
        sExp = r"/tmp/dir/subdir/subsubdir"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Surrounding quotes and spaces are removed (2).",]
    )
    def test_Linux_SurroundingChars_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"  '  /tmp\dir\subdir\subsubdir  '  "
        sOut = CString.NormalizePath(sIn)
        sExp = r"/tmp/dir/subdir/subsubdir"
        assert sOut == sExp

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["Redundant path separators removed; all backslashes replaced by single slashes.",]
    )
    def test_Windows_Separators_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"C:\dir\\subdir//subsubdir"
        sOut = CString.NormalizePath(sIn)
        sExp = r"C:/dir/subdir/subsubdir"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Redundant path separators removed; all backslashes replaced by single slashes.",]
    )
    def test_Linux_Separators_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"/tmp\dir\\subdir//subsubdir"
        sOut = CString.NormalizePath(sIn)
        sExp = r"/tmp/dir/subdir/subsubdir"
        assert sOut == sExp

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["Redundant path separators removed; remaining separators are masked backslashes.",]
    )
    def test_Windows_Separators_3(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"C:\dir\\subdir//subsubdir"
        sOut = CString.NormalizePath(sIn, bWin=True)
        sExp = r"C:\\dir\\subdir\\subsubdir"
        assert sOut == sExp

    # Under Linux it most probably makes no sense to set bWin=True
    # to get something like \\tmp\\dir\\subdir\\subsubdir
    # => no corresponding Linux test

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["All backslashes replaced by single slashes; up-level references resolved.",]
    )
    def test_Windows_Separators_4(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"C:\dir1\..\\dir2"
        sOut = CString.NormalizePath(sIn)
        sExp = r"C:/dir2"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["All backslashes replaced by single slashes; up-level references resolved.",]
    )
    def test_Linux_Separators_4(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"/tmp/dir1\..\\dir2"
        sOut = CString.NormalizePath(sIn)
        sExp = r"/tmp/dir2"
        assert sOut == sExp

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["All slashes replaced by double (masked) backslashes; up-level references resolved.",]
    )
    def test_Windows_Separators_5(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"C:\dir/../dir\\subdir"
        sOut = CString.NormalizePath(sIn, bWin=True)
        sExp = r"C:\\dir\\subdir"
        assert sOut == sExp

    # Under Linux it most probably makes no sense to set bWin=True
    # to get something like \\tmp\\dir\\subdir
    # => no corresponding Linux test

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["All slashes replaced by single (unmasked) backslashes; up-level references resolved.",]
    )
    def test_Windows_Separators_6(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"C:\dir/../dir\\subdir"
        sOut = CString.NormalizePath(sIn, bWin=True, bMask=False)
        sExp = r"C:\dir\subdir"
        assert sOut == sExp

    # Under Linux it most probably makes no sense to set bWin=True, bMask=False
    # to get something like \tmp\dir\subdir
    # => no corresponding Linux test

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["Resulting absolute path is a merge of the absolute reference path and the relative input path; single slashes as separator.",]
    )
    def test_Windows_RelPath_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"../test_2\\subdir"
        sReferencePathAbs = r"C:\test"
        sOut = CString.NormalizePath(sIn, bWin=False, bMask=False, sReferencePathAbs=sReferencePathAbs)
        sExp = r"C:/test_2/subdir"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting absolute path is a merge of the absolute reference path and the relative input path; single slashes as separator.",]
    )
    def test_Linux_RelPath_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"../test_2\\subdir"
        sReferencePathAbs = r"/tmp/test"
        sOut = CString.NormalizePath(sIn, bWin=False, bMask=False, sReferencePathAbs=sReferencePathAbs)
        sExp = r"/tmp/test_2/subdir"
        assert sOut == sExp

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["Resulting absolute path is a merge of the absolute reference path and the relative input path; masked backslashes as separator.",]
    )
    def test_Windows_RelPath_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"../test_2\\subdir"
        sReferencePathAbs = r"C:\test"
        sOut = CString.NormalizePath(sIn, bWin=True, bMask=True, sReferencePathAbs=sReferencePathAbs)
        sExp = r"C:\\test_2\\subdir"
        assert sOut == sExp

    # Under Linux it most probably makes no sense to set bWin=True, bMask=False
    # to get something like \\tmp\\test_2\\subdir
    # => no corresponding Linux test

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["Paths with blanks inside are encapsulated in quotes; single slashes as separator; up-level references resolved.",]
    )
    def test_Windows_Blanks_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"C:\dir//../dir\\sub  dir"
        sOut = CString.NormalizePath(sIn, bConsiderBlanks=True)
        sExp = r'"C:/dir/sub  dir"'
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Paths with blanks inside are encapsulated in quotes; single slashes as separator; up-level references resolved.",]
    )
    def test_Linux_Blanks_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"/tmp\dir/../dir\\sub  dir"
        sOut = CString.NormalizePath(sIn, bConsiderBlanks=True)
        sExp = r'"/tmp/dir/sub  dir"'
        assert sOut == sExp

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["Paths without blanks inside are not encapsulated in quotes; single slashes as separator.",]
    )
    def test_Windows_Blanks_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"C:\dir\\subdir"
        sOut = CString.NormalizePath(sIn, bConsiderBlanks=True)
        sExp = r"C:/dir/subdir"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Paths without blanks inside are not encapsulated in quotes; single slashes as separator.",]
    )
    def test_Linux_Blanks_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"/tmp\dir\\subdir"
        sOut = CString.NormalizePath(sIn, bConsiderBlanks=True)
        sExp = r"/tmp/dir/subdir"
        assert sOut == sExp

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["Resulting local network resource path contains single slashes as separator (1).",]
    )
    def test_LocalNetworkPath_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"//server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn)
        sExp = r"//server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting local network resource path contains single slashes as separator (2).",]
    )
    def test_LocalNetworkPath_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"\\server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn)
        sExp = r"//server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting local network resource path contains single backslashes as separator (1).",]
    )
    def test_LocalNetworkPath_3(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"//server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn, bWin=True)
        sExp = r"\\server.com\002\003\004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting local network resource path contains single backslashes as separator (2).",]
    )
    def test_LocalNetworkPath_4(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"\\server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn, bWin=True)
        sExp = r"\\server.com\002\003\004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting local network resource path (web browser format) contains single slashes as separator.",]
    )
    def test_LocalNetworkPath_5(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"file://///server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn)
        sExp = r"file://///server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting local network resource path (web browser format) contains single slashes as separator; bWin has no effect.",]
    )
    def test_LocalNetworkPath_6(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"file://///server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn, bWin=True)
        sExp = r"file://///server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting internet address contains single backslashes as separator (http 1).",]
    )
    def test_WebAddress_1(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"http://server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn)
        sExp = r"http://server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting internet address contains single backslashes as separator (http 2).",]
    )
    def test_WebAddress_2(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"http:\\server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn)
        sExp = r"http://server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting internet address contains single backslashes as separator (https 1).",]
    )
    def test_WebAddress_3(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"https://server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn)
        sExp = r"https://server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting internet address contains single backslashes as separator (https 2).",]
    )
    def test_WebAddress_4(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"https:\\server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn)
        sExp = r"https://server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting internet address contains single backslashes as separator; bWin has no effect (http 1).",]
    )
    def test_WebAddress_5(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"http://server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn, bWin=True)
        sExp = r"http://server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting internet address contains single backslashes as separator; bWin has no effect (http 2).",]
    )
    def test_WebAddress_6(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"http:\\server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn, bWin=True)
        sExp = r"http://server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting internet address contains single backslashes as separator; bWin has no effect (https 1).",]
    )
    def test_WebAddress_7(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"https://server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn, bWin=True)
        sExp = r"https://server.com/002/003/004"
        assert sOut == sExp

    @pytest.mark.parametrize(
        "Description", ["Resulting internet address contains single backslashes as separator; bWin has no effect (https 2).",]
    )
    def test_WebAddress_8(self, Description):
        """pytest 'NormalizePath'"""
        sIn  = r"https:\\server.com\001//..\002/003\\004"
        sOut = CString.NormalizePath(sIn, bWin=True)
        sExp = r"https://server.com/002/003/004"
        assert sOut == sExp

# eof class Test_NormalizePath

# --------------------------------------------------------------------------------------------------------------
#TM***

class Test_DetectParentPath:
    """The functionality of this method is based on the structure of the file system, on which this test is executed.
Therefore we compute all expected return values dynamically inside every test - relative to the position of this file
(to ensure that this test can be executed in any folder).
But it must be possible to go 3 levels up in the file system!"""

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Expected path detected two levels up; search for single folder.",]
    )
    def test_ParentPath_1(self, Description):
        """pytest 'DetectParentPath'"""
        sIn_StartPath       = CString.NormalizePath(__file__)
        sExp_DestPath       = CString.NormalizePath(os.path.dirname(os.path.dirname(sIn_StartPath)))
        sExp_DestPathParent = CString.NormalizePath(os.path.dirname(sExp_DestPath))
        sIn_Foldername      = os.path.basename(sExp_DestPath)
        sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername)
        assert sRet_DestPath == sExp_DestPath
        assert len(listRet_DestPaths) == 1
        assert listRet_DestPaths[0] == sExp_DestPath
        assert sRet_DestFile is None
        assert listRet_DestFiles is None
        assert sRet_DestPathParent == sExp_DestPathParent

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Expected paths detected one and two levels up; search for two folders.",]
    )
    def test_ParentPath_2(self, Description):
        """pytest 'DetectParentPath'"""
        sLogfile = None
        sPlatformSystem = platform.system()
        if sPlatformSystem == "Windows":
           sLogfile = os.path.expandvars(r"%TMP%\CString_test_ParentPath_2.log")
        elif sPlatformSystem == "Linux":
           sTmp = os.path.expanduser('~')
           sLogfile = f"{sTmp}/CString_test_ParentPath_2.log"

        oLogfile = CFile(sLogfile)

        sIn_StartPath           = CString.NormalizePath(__file__)
        sParentParentPath       = CString.NormalizePath(os.path.dirname(os.path.dirname(sIn_StartPath)))
        sIn_Foldername_1        = os.path.basename(sParentParentPath)
        sParentParentParentPath = CString.NormalizePath(os.path.dirname(os.path.dirname(os.path.dirname(sIn_StartPath))))
        sIn_Foldername_2        = os.path.basename(sParentParentParentPath)
        sIn_Foldername          = f"{sIn_Foldername_1};{sIn_Foldername_2}"
        sExp_DestPathParent = CString.NormalizePath(os.path.dirname(sParentParentPath))
        sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername)

        oLogfile.Write(f"===== test_ParentPath_2")
        oLogfile.Write(f"sIn_StartPath           : {sIn_StartPath}")
        oLogfile.Write(f"sParentParentPath       : {sParentParentPath}")
        oLogfile.Write(f"sIn_Foldername_1        : {sIn_Foldername_1}")
        oLogfile.Write(f"sParentParentParentPath : {sParentParentParentPath}")
        oLogfile.Write(f"sIn_Foldername_2        : {sIn_Foldername_2}")
        oLogfile.Write(f"sIn_Foldername          : {sIn_Foldername}")
        oLogfile.Write(f"sExp_DestPathParent     : {sExp_DestPathParent}")
        oLogfile.Write(f"sRet_DestPath           : {sRet_DestPath}")
        oLogfile.Write(f"listRet_DestPaths       : {listRet_DestPaths}")
        oLogfile.Write(f"sRet_DestFile           : {sRet_DestFile}")
        oLogfile.Write(f"listRet_DestFiles       : {listRet_DestFiles}")
        oLogfile.Write(f"sRet_DestPathParent     : {sRet_DestPathParent}")
        del oLogfile

        assert sRet_DestPath == sParentParentPath
        assert len(listRet_DestPaths) == 2
        assert listRet_DestPaths[0] == sParentParentPath
        assert listRet_DestPaths[1] == sParentParentParentPath
        assert sRet_DestFile is None
        assert listRet_DestFiles is None
        assert sRet_DestPathParent == sExp_DestPathParent

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Expected path detected two levels up; search for two folders; first folder not existing.",]
    )
    def test_ParentPath_3(self, Description):
        """pytest 'DetectParentPath'"""
        sIn_StartPath     = CString.NormalizePath(__file__)
        sParentParentPath = CString.NormalizePath(os.path.dirname(os.path.dirname(sIn_StartPath)))
        sIn_Foldername_1  = "iamnotexisting"
        sIn_Foldername_2  = os.path.basename(sParentParentPath)
        sIn_Foldername    = f"{sIn_Foldername_1};{sIn_Foldername_2}"
        sExp_DestPathParent = CString.NormalizePath(os.path.dirname(sParentParentPath))
        sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername)
        assert sRet_DestPath == sParentParentPath
        assert len(listRet_DestPaths) == 1
        assert listRet_DestPaths[0] == sParentParentPath
        assert sRet_DestFile is None
        assert listRet_DestFiles is None
        assert sRet_DestPathParent == sExp_DestPathParent

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["No path detected; search for two folders; both folders not existing.",]
    )
    def test_ParentPath_4(self, Description):
        """pytest 'DetectParentPath'"""
        sIn_StartPath    = CString.NormalizePath(__file__)
        sIn_Foldername_1 = "iamnotexisting"
        sIn_Foldername_2 = "iamalsonotexisting"
        sIn_Foldername   = f"{sIn_Foldername_1};{sIn_Foldername_2}"
        sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername)
        assert sRet_DestPath is None
        assert listRet_DestPaths is None
        assert sRet_DestFile is None
        assert listRet_DestFiles is None
        assert sRet_DestPathParent is None

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Expected path detected two levels up; search for single folder; search additionally for a file; file found one times.",]
    )
    def test_ParentPath_5(self, Description):
        """pytest 'DetectParentPath'"""
        sIn_StartPath       = CString.NormalizePath(__file__)
        sExp_DestPath       = CString.NormalizePath(os.path.dirname(os.path.dirname(sIn_StartPath)))
        sExp_DestPathParent = CString.NormalizePath(os.path.dirname(sExp_DestPath))
        sIn_Foldername      = os.path.basename(sExp_DestPath)
        sIn_FileName        = "0010101.txt"
        sExp_DestFile       = f"{sExp_DestPath}/testfiles/001/00101/0010101/{sIn_FileName}"
        sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername, sFileName=sIn_FileName)
        assert sRet_DestPath == sExp_DestPath
        assert len(listRet_DestPaths) == 1
        assert listRet_DestPaths[0] == sExp_DestPath
        assert sRet_DestFile == sExp_DestFile
        assert len(listRet_DestFiles) == 1
        assert listRet_DestFiles[0] == sExp_DestFile
        assert sRet_DestPathParent == sExp_DestPathParent

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Expected path detected two levels up; search for single folder; search additionally for a file; file found two times.",]
    )
    def test_ParentPath_6(self, Description):
        """pytest 'DetectParentPath'"""
        sIn_StartPath       = CString.NormalizePath(__file__)
        sExp_DestPath       = CString.NormalizePath(os.path.dirname(os.path.dirname(sIn_StartPath)))
        sExp_DestPathParent = CString.NormalizePath(os.path.dirname(sExp_DestPath))
        sIn_Foldername      = os.path.basename(sExp_DestPath)
        sIn_FileName        = "000A.txt"
        sExp_DestFile_1     = f"{sExp_DestPath}/testfiles/001/{sIn_FileName}"
        sExp_DestFile_2     = f"{sExp_DestPath}/testfiles/002/00201/0020101/{sIn_FileName}"
        sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername, sFileName=sIn_FileName)
        assert sRet_DestPath == sExp_DestPath
        assert len(listRet_DestPaths) == 1
        assert listRet_DestPaths[0] == sExp_DestPath
        assert sRet_DestFile == sExp_DestFile_1
        assert len(listRet_DestFiles) == 2
        assert listRet_DestFiles[0] == sExp_DestFile_1
        assert listRet_DestFiles[1] == sExp_DestFile_2
        assert sRet_DestPathParent == sExp_DestPathParent

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Expected path detected two levels up; search for single folder; search additionally for a file; file not found.",]
    )
    def test_ParentPath_7(self, Description):
        """pytest 'DetectParentPath'"""
        sIn_StartPath       = CString.NormalizePath(__file__)
        sExp_DestPath       = CString.NormalizePath(os.path.dirname(os.path.dirname(sIn_StartPath)))
        sExp_DestPathParent = CString.NormalizePath(os.path.dirname(sExp_DestPath))
        sIn_Foldername      = os.path.basename(sExp_DestPath)
        sIn_FileName        = "IAmNotExisting.txt"
        sExp_DestFileDummy  = f"{sExp_DestPath}/testfiles/001/00101/{sIn_FileName}"
        sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername, sFileName=sIn_FileName)
        assert sRet_DestPath == sExp_DestPath
        assert len(listRet_DestPaths) == 1
        assert listRet_DestPaths[0] == sExp_DestPath
        assert sRet_DestFile is None
        assert listRet_DestFiles is None
        assert sRet_DestPathParent == sExp_DestPathParent

# eof class Test_DetectParentPath:

# --------------------------------------------------------------------------------------------------------------
#TM***

class Test_StringFilter:
    """Tests of CString method 'StringFilter'."""

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["bSkipBlankStrings = True",]
    )
    def test_StringFilter_01(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "    ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["bSkipBlankStrings = False",]
    )
    def test_StringFilter_02(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "    ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = False,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sComment 1",]
    )
    def test_StringFilter_03(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  # Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = "#",
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sComment 2",]
    )
    def test_StringFilter_04(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  ; Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = ";",
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sComment 3",]
    )
    def test_StringFilter_05(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  # Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = "#",
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = "beats",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sComment 4",]
    )
    def test_StringFilter_06(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = "Speed",
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = "beats",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sComment 5",]
    )
    def test_StringFilter_07(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = False,
                                    bSkipBlankStrings = True,
                                    sComment          = "SPEED",
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = "beats",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sComment 6",]
    )
    def test_StringFilter_08(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = "SPEED",
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = "beats",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sStartsWith",]
    )
    def test_StringFilter_09(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = "Spee",
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sEndsWith",]
    )
    def test_StringFilter_10(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = "nute",
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sStartsNotWith",]
    )
    def test_StringFilter_11(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = "Spee",
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sEndsNotWith",]
    )
    def test_StringFilter_12(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = "nute",
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sContains 1",]
    )
    def test_StringFilter_13(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = "ts pe",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sContains 2",]
    )
    def test_StringFilter_14(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = "otto;25;beats;all",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sContains and sContainsNot",]
    )
    def test_StringFilter_15(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = "otto;25;beats;all",
                                    sContainsNot      = "beats",
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sContainsNot",]
    )
    def test_StringFilter_16(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = "ts pe",
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter combinations; case sensitive",]
    )
    def test_StringFilter_17(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = "Speed",
                                    sEndsWith         = "minute",
                                    sStartsNotWith    = "Speed",
                                    sEndsNotWith      = "minute",
                                    sContains         = "beats",
                                    sContainsNot      = "beats",
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter combinations; not case sensitive",]
    )
    def test_StringFilter_18(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = False,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = "spEED",
                                    sEndsWith         = "MINute",
                                    sStartsNotWith    = "minute",
                                    sEndsNotWith      = "Speed",
                                    sContains         = "BEats",
                                    sContainsNot      = "really not",
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sInclRegEx 1",]
    )
    def test_StringFilter_19(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = r"\d{2}",
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sInclRegEx 2",]
    )
    def test_StringFilter_20(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = r"\d{3}",
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter combinations 1",]
    )
    def test_StringFilter_21(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = "Speed",
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = r"\d{3}",
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter combinations 2",]
    )
    def test_StringFilter_22(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = "Speed",
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = r"\d{2}",
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter combinations 3",]
    )
    def test_StringFilter_23(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = "Speed",
                                    sEndsNotWith      = None,
                                    sContains         = "beats",
                                    sContainsNot      = None,
                                    sInclRegEx        = r"\d{2}",
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter combinations 4",]
    )
    def test_StringFilter_24(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = "Speed",
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = "really not",
                                    sInclRegEx        = r"\d{3}",
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sExclRegEx 1",]
    )
    def test_StringFilter_25(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = r"\d{2}")
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["sExclRegEx 2",]
    )
    def test_StringFilter_26(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = r"\d{3}")
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["all filter combinations 1",]
    )
    def test_StringFilter_27(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = "Speed",
                                    sEndsWith         = "minute",
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = r"\d{3}")
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["all filter combinations 2",]
    )
    def test_StringFilter_28(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = "Speed",
                                    sEndsWith         = "minute",
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = r"\d{2}")
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["all filter combinations 3",]
    )
    def test_StringFilter_29(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = "Speed",
                                    sEndsNotWith      = "minute",
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = r"\d{3}")
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["all filter combinations 4",]
    )
    def test_StringFilter_30(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "  Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = "Speed",
                                    sEndsNotWith      = "minute",
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = r"\d{2}")
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["handling of blanks 1",]
    )
    def test_StringFilter_31(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "   Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = "   Speed ",
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["handling of blanks 2",]
    )
    def test_StringFilter_32(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "   Speed is 25 beats per minute  ",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = r"\s{3}Speed",
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter string lists 1",]
    )
    def test_StringFilter_33(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "Alpha is not beta; and beta is not gamma",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = "beta; and",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter string lists 2",]
    )
    def test_StringFilter_34(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "Alpha is not beta; and beta is not gamma",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = "beta; not",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter string lists 3",]
    )
    def test_StringFilter_35(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "Alpha is not beta; and beta is not gamma",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = r"beta\; and",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter string lists 4",]
    )
    def test_StringFilter_36(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "Alpha is not beta; and beta is not gamma",
                                    bCaseSensitive    = True,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = r"beta\; not",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter string lists 5",]
    )
    def test_StringFilter_37(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "Alpha is not beta; and beta is not gamma",
                                    bCaseSensitive    = False,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = r"BETA\; AND",
                                    sContainsNot      = None,
                                    sInclRegEx        = None,
                                    sExclRegEx        = None)
        assert bAck is True

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter string lists 6",]
    )
    def test_StringFilter_38(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "Alpha is not beta; and beta is not gamma",
                                    bCaseSensitive    = False,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = r"BETA\;\sAND",
                                    sExclRegEx        = None)
        assert bAck is False

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["filter string lists 7",]
    )
    def test_StringFilter_39(self, Description):
        """pytest 'StringFilter'"""
        bAck = CString.StringFilter(sString           = "Alpha is not beta; and beta is not gamma",
                                    bCaseSensitive    = False,
                                    bSkipBlankStrings = True,
                                    sComment          = None,
                                    sStartsWith       = None,
                                    sEndsWith         = None,
                                    sStartsNotWith    = None,
                                    sEndsNotWith      = None,
                                    sContains         = None,
                                    sContainsNot      = None,
                                    sInclRegEx        = r"beta\;\sand",
                                    sExclRegEx        = None)
        assert bAck is True

# eof class Test_StringFilter:

# --------------------------------------------------------------------------------------------------------------
#TM***

class Test_FormatResult:
    """Tests of CString method 'FormatResult'."""

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Success 1",]
    )
    def test_FormatResult_01(self, Description):
        """pytest 'FormatResult'"""
        sResult = CString.FormatResult(sMethod="Method",
                                       bSuccess=True,
                                       sResult="Result")
        assert sResult == "[Method] : Result"

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Success 2",]
    )
    def test_FormatResult_02(self, Description):
        """pytest 'FormatResult'"""
        sResult = CString.FormatResult(sMethod="",
                                       bSuccess=True,
                                       sResult="Result")
        assert sResult == "Result"

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Error 1",]
    )
    def test_FormatResult_03(self, Description):
        """pytest 'FormatResult'"""
        sResult = CString.FormatResult(sMethod="Method",
                                       bSuccess=False,
                                       sResult="Result")
        assert sResult == "!!! ERROR !!!\n[Method] : Result"

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Error 2",]
    )
    def test_FormatResult_04(self, Description):
        """pytest 'FormatResult'"""
        sResult = CString.FormatResult(sMethod="",
                                       bSuccess=False,
                                       sResult="Result")
        assert sResult == "!!! ERROR !!!\nResult"

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Exception 1",]
    )
    def test_FormatResult_05(self, Description):
        """pytest 'FormatResult'"""
        sResult = CString.FormatResult(sMethod="Method",
                                       bSuccess=None,
                                       sResult="Result")
        assert sResult == "!!! EXCEPTION !!!\n[Method] : Result"

    # --------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        "Description", ["Exception 2",]
    )
    def test_FormatResult_06(self, Description):
        """pytest 'FormatResult'"""
        sResult = CString.FormatResult(sMethod="",
                                       bSuccess=None,
                                       sResult="Result")
        assert sResult == "!!! EXCEPTION !!!\nResult"

# --------------------------------------------------------------------------------------------------------------

