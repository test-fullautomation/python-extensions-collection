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
# test_CUtils.py
#
# XC-CI1/ECA3-Queckenstedt
#
# 06.06.2023
#
# --------------------------------------------------------------------------------------------------------------

# -- import standard Python modules
import os, sys, platform, time, pytest

# -- import own Python modules (containing the code to be tested)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))) # to make sure to hit the package relative to this file at first
from PythonExtensionsCollection.Utils.CUtils import *
from PythonExtensionsCollection.File.CFile import CFile
from PythonExtensionsCollection.String.CString import CString

# --------------------------------------------------------------------------------------------------------------

class Test_PrettyPrint:
    """Tests of CUtils method 'PrettyPrint'."""

    # --------------------------------------------------------------------------------------------------------------

    # ---- simple data types

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'int'.",]
    )
    def test_Integer(self, Description):
        """pytest 'PrettyPrint'"""
        oData = 4
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[INT]  :  4")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'float'.",]
    )
    def test_Float(self, Description):
        """pytest 'PrettyPrint'"""
        oData = 6.8
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[FLOAT]  :  6.8")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'str'.",]
    )
    def test_String(self, Description):
        """pytest 'PrettyPrint'"""
        oData = "ABC"
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[STR]  :  'ABC'")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'bool'.",]
    )
    def test_Bool(self, Description):
        """pytest 'PrettyPrint'"""
        oData = True
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[BOOL]  :  True")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'None'.",]
    )
    def test_None(self, Description):
        """pytest 'PrettyPrint'"""
        oData = None
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[NONE]  :  None")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    # --------------------------------------------------------------------------------------------------------------

    # ---- composite data types

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'list'.",]
    )
    def test_List(self, Description):
        """pytest 'PrettyPrint'"""
        oData = [4, 6.8, "ABC", True, None]
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[LIST] (5/1) > [INT]  :  4")
        listExpected.append("[LIST] (5/2) > [FLOAT]  :  6.8")
        listExpected.append("[LIST] (5/3) > [STR]  :  'ABC'")
        listExpected.append("[LIST] (5/4) > [BOOL]  :  True")
        listExpected.append("[LIST] (5/5) > [NONE]  :  None")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'tuple'.",]
    )
    def test_Tuple(self, Description):
        """pytest 'PrettyPrint'"""
        oData = (4, 6.8, "ABC", True, None)
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[TUPLE] (5/1) > [INT]  :  4")
        listExpected.append("[TUPLE] (5/2) > [FLOAT]  :  6.8")
        listExpected.append("[TUPLE] (5/3) > [STR]  :  'ABC'")
        listExpected.append("[TUPLE] (5/4) > [BOOL]  :  True")
        listExpected.append("[TUPLE] (5/5) > [NONE]  :  None")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'set'.",]
    )
    def test_Set(self, Description):
        """pytest 'PrettyPrint'"""
        oData = {4, 6.8, "ABC", True, None}
        listOutLines = PrettyPrint(oData)
        listExpectedParts = []
        listExpectedParts.append("> [INT]  :  4")
        listExpectedParts.append("> [FLOAT]  :  6.8")
        listExpectedParts.append("> [STR]  :  'ABC'")
        listExpectedParts.append("> [BOOL]  :  True")
        listExpectedParts.append("> [NONE]  :  None")
        # !!! elements of a set are not ordered !!!
        assert len(listOutLines) == len(listExpectedParts)
        for sLine in listOutLines:
            assert sLine.startswith("[SET] (5")
            bFound = False
            for sExpectedPart in listExpectedParts:
                if sLine.endswith(sExpectedPart):
                    bFound = True
                    break
            assert bFound is True

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'dict'.",]
    )
    def test_Dict(self, Description):
        """pytest 'PrettyPrint'"""
        oData = {}
        oData['K1'] = 4
        oData['K2'] = 6.8
        oData['K3'] = "ABC"
        oData['K4'] = True
        oData['K5'] = None
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[DICT] (5/1) > {K1} [INT]  :  4")
        listExpected.append("[DICT] (5/2) > {K2} [FLOAT]  :  6.8")
        listExpected.append("[DICT] (5/3) > {K3} [STR]  :  'ABC'")
        listExpected.append("[DICT] (5/4) > {K4} [BOOL]  :  True")
        listExpected.append("[DICT] (5/5) > {K5} [NONE]  :  None")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'dotdict'.",]
    )
    def test_DotDict(self, Description):
        """pytest 'PrettyPrint'"""
        dData = {}
        dData['K1'] = 4
        dData['K2'] = 6.8
        dData['K3'] = "ABC"
        dData['K4'] = True
        dData['K5'] = None
        oData = dotdict(dData)
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[DOTDICT] (5/1) > {K1} [INT]  :  4")
        listExpected.append("[DOTDICT] (5/2) > {K2} [FLOAT]  :  6.8")
        listExpected.append("[DOTDICT] (5/3) > {K3} [STR]  :  'ABC'")
        listExpected.append("[DOTDICT] (5/4) > {K4} [BOOL]  :  True")
        listExpected.append("[DOTDICT] (5/5) > {K5} [NONE]  :  None")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    # --------------------------------------------------------------------------------------------------------------

    # ---- nested data types

    @pytest.mark.parametrize(
        "Description", ["Input parameter of nested types.",]
    )
    def test_NestedTypes(self, Description):
        """pytest 'PrettyPrint'"""
        listData = [1, "A"]
        dictData = {}
        dictData['K1'] = 2
        dictData['K2'] = [3, 'B', (4.5, 'X', False, None)]
        dotdictData = dotdict(dictData)
        oData = [6, listData, dictData, dotdictData, None]
        listOutLines = PrettyPrint(oData)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("[LIST] (5/1) > [INT]  :  6")
        listExpected.append("[LIST] (5/2) > [LIST] (2/1) > [INT]  :  1")
        listExpected.append("[LIST] (5/2) > [LIST] (2/2) > [STR]  :  'A'")
        listExpected.append("[LIST] (5/3) > [DICT] (2/1) > {K1} [INT]  :  2")
        listExpected.append("[LIST] (5/3) > [DICT] (2/2) > {K2} [LIST] (3/1) > [INT]  :  3")
        listExpected.append("[LIST] (5/3) > [DICT] (2/2) > {K2} [LIST] (3/2) > [STR]  :  'B'")
        listExpected.append("[LIST] (5/3) > [DICT] (2/2) > {K2} [LIST] (3/3) > [TUPLE] (4/1) > [FLOAT]  :  4.5")
        listExpected.append("[LIST] (5/3) > [DICT] (2/2) > {K2} [LIST] (3/3) > [TUPLE] (4/2) > [STR]  :  'X'")
        listExpected.append("[LIST] (5/3) > [DICT] (2/2) > {K2} [LIST] (3/3) > [TUPLE] (4/3) > [BOOL]  :  False")
        listExpected.append("[LIST] (5/3) > [DICT] (2/2) > {K2} [LIST] (3/3) > [TUPLE] (4/4) > [NONE]  :  None")
        listExpected.append("[LIST] (5/4) > [DOTDICT] (2/1) > {K1} [INT]  :  2")
        listExpected.append("[LIST] (5/4) > [DOTDICT] (2/2) > {K2} [LIST] (3/1) > [INT]  :  3")
        listExpected.append("[LIST] (5/4) > [DOTDICT] (2/2) > {K2} [LIST] (3/2) > [STR]  :  'B'")
        listExpected.append("[LIST] (5/4) > [DOTDICT] (2/2) > {K2} [LIST] (3/3) > [TUPLE] (4/1) > [FLOAT]  :  4.5")
        listExpected.append("[LIST] (5/4) > [DOTDICT] (2/2) > {K2} [LIST] (3/3) > [TUPLE] (4/2) > [STR]  :  'X'")
        listExpected.append("[LIST] (5/4) > [DOTDICT] (2/2) > {K2} [LIST] (3/3) > [TUPLE] (4/3) > [BOOL]  :  False")
        listExpected.append("[LIST] (5/4) > [DOTDICT] (2/2) > {K2} [LIST] (3/3) > [TUPLE] (4/4) > [NONE]  :  None")
        listExpected.append("[LIST] (5/5) > [NONE]  :  None")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    # --------------------------------------------------------------------------------------------------------------

    # ---- indentation and prefix

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'list'; output indented by 5 blanks.",]
    )
    def test_ListIndented(self, Description):
        """pytest 'PrettyPrint'"""
        oData = [4, 6.8, "ABC", True, None]
        listOutLines = PrettyPrint(oData, nIndent=5)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("     [LIST] (5/1) > [INT]  :  4")
        listExpected.append("     [LIST] (5/2) > [FLOAT]  :  6.8")
        listExpected.append("     [LIST] (5/3) > [STR]  :  'ABC'")
        listExpected.append("     [LIST] (5/4) > [BOOL]  :  True")
        listExpected.append("     [LIST] (5/5) > [NONE]  :  None")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    @pytest.mark.parametrize(
        "Description", ["Input parameter of type 'list'; output indented by 2 blanks and with prefix.",]
    )
    def test_ListIndentedWithPrefix(self, Description):
        """pytest 'PrettyPrint'"""
        oData = [4, 6.8, "ABC", True, None]
        listOutLines = PrettyPrint(oData, nIndent=2, sPrefix="--PREFIX--")
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("  --PREFIX-- [LIST] (5/1) > [INT]  :  4")
        listExpected.append("  --PREFIX-- [LIST] (5/2) > [FLOAT]  :  6.8")
        listExpected.append("  --PREFIX-- [LIST] (5/3) > [STR]  :  'ABC'")
        listExpected.append("  --PREFIX-- [LIST] (5/4) > [BOOL]  :  True")
        listExpected.append("  --PREFIX-- [LIST] (5/5) > [NONE]  :  None")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

    @pytest.mark.parametrize(
        "Description", ["Input parameter of nested types; output indented by 2 blanks and with prefix; strings in hexadecimal format.",]
    )
    def test_ListIndentedPrefix(self, Description):
        """pytest 'PrettyPrint'"""
        oData = [4, 6.8, "ABC", True, None, ("A", "B"), ["DE", "FGH"], {"KA":4, "KB":6.8, "KC":"ABC", "KD":True, "KE":None, "KF":[1, "MNO"]}]
        listOutLines = PrettyPrint(oData, nIndent=2, sPrefix="--HEX OUTPUT--", bHexFormat=True)
        sRet = "\n".join(listOutLines)
        listExpected = []
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/1) > [INT]  :  4")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/2) > [FLOAT]  :  6.8")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/3) > [STR]  :  '0x41 0x42 0x43'")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/4) > [BOOL]  :  True")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/5) > [NONE]  :  None")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/6) > [TUPLE] (2/1) > [STR]  :  '0x41'")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/6) > [TUPLE] (2/2) > [STR]  :  '0x42'")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/7) > [LIST] (2/1) > [STR]  :  '0x44 0x45'")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/7) > [LIST] (2/2) > [STR]  :  '0x46 0x47 0x48'")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/8) > [DICT] (6/1) > {KA} [INT]  :  4")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/8) > [DICT] (6/2) > {KB} [FLOAT]  :  6.8")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/8) > [DICT] (6/3) > {KC} [STR]  :  '0x41 0x42 0x43'")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/8) > [DICT] (6/4) > {KD} [BOOL]  :  True")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/8) > [DICT] (6/5) > {KE} [NONE]  :  None")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/8) > [DICT] (6/6) > {KF} [LIST] (2/1) > [INT]  :  1")
        listExpected.append("  --HEX OUTPUT-- [LIST] (8/8) > [DICT] (6/6) > {KF} [LIST] (2/2) > [STR]  :  '0x4d 0x4e 0x4f'")
        sExp = "\n".join(listExpected)
        assert sRet == sExp

# eof class Test_PrettyPrint

# --------------------------------------------------------------------------------------------------------------

class Test_GetInstalledPackages:
    """Tests of CUtils method 'GetInstalledPackages'."""

    # --------------------------------------------------------------------------------------------------------------

    @pytest.mark.parametrize(
        "Description", ["'GetInstalledPackages' default usage.",]
    )
    def test_DefaultUsage(self, Description):
        """pytest 'GetInstalledPackages' default usage"""
        listofTuplesPackages, bSuccess, sResult = CUtils.GetInstalledPackages()
        print(sResult)
        assert bSuccess is True
        assert len(listofTuplesPackages) > 0

    @pytest.mark.parametrize(
        "Description", ["'GetInstalledPackages' with output file.",]
    )
    def test_OutputFile(self, Description):
        """pytest 'GetInstalledPackages' with output file"""
        sOutputFile = None
        sPlatformSystem = platform.system()
        if sPlatformSystem == "Windows":
           sOutputFile = r"%TMP%\CUtils_TestFile.txt"
        elif sPlatformSystem == "Linux":
           sTmp = os.path.expanduser('~')
           sOutputFile = f"{sTmp}/CUtils_TestFile.txt"
        sOutputFile = CString.NormalizePath(sOutputFile)
        oOutputFile = CFile(sOutputFile)
        bSuccess, sResult = oOutputFile.Delete(bConfirmDelete=False)
        print(sResult)
        assert bSuccess is True
        del oOutputFile
        listofTuplesPackages, bSuccess, sResult = CUtils.GetInstalledPackages(sOutputFile)
        print(sResult)
        assert bSuccess is True
        assert len(listofTuplesPackages) > 0
        bIsFile = os.path.isfile(sOutputFile)
        assert bIsFile is True
        os.remove(sOutputFile)

# --------------------------------------------------------------------------------------------------------------
