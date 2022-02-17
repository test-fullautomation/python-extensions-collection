#  Copyright 2020-2022 Robert Bosch Car Multimedia GmbH
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
# test_CFile.py
#
# XC-CT/ECA3-Queckenstedt
#
# 26.01.2022
#
# --------------------------------------------------------------------------------------------------------------

# -- import standard Python modules
import os, sys, time, platform, pytest
from dotdict import dotdict

# -- import own Python modules (containing the code to be tested)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))) # to make sure to hit the package relative to this file at first
from PythonExtensionsCollection.File.CFile import CFile
from PythonExtensionsCollection.String.CString import CString

# --------------------------------------------------------------------------------------------------------------

class Test_CFile:
   """Tests of module CFile ."""

   # --------------------------------------------------------------------------------------------------------------

   @pytest.mark.parametrize(
      "Description", ["Write and Read with explicit Close",]
   )
   def test_CFile_1(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      sTestString = "Teststring-1"
      bSuccess, sResult = oFile.Write(sTestString)
      assert bSuccess is True
      bSuccess, sResult = oFile.Close()
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == sTestString
      bSuccess, sResult = oFile.Close()
      assert bSuccess is True
      del oFile


   @pytest.mark.parametrize(
      "Description", ["Write and Read without explicit Close",]
   )
   def test_CFile_2(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      sTestString = "Teststring-2"
      bSuccess, sResult = oFile.Write(sTestString)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == sTestString
      del oFile


   @pytest.mark.parametrize(
      "Description", ["Delete file",]
   )
   def test_CFile_3(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      bSuccess, sResult = oFile.Write("Dummy")
      assert bSuccess is True
      bSuccess, sResult = oFile.Delete()
      assert bSuccess is True
      del oFile


   @pytest.mark.parametrize(
      "Description", ["Append and Read with explicit Close",]
   )
   def test_CFile_4(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      bSuccess, sResult = oFile.Delete(bConfirmDelete=False) # no matter if file exists from previous test run or not; only making sure that file does not exist (precondition)
      assert bSuccess is True
      sTestString_1 = "Teststring_1_ABC"
      sTestString_2 = "Teststring_2_MNO"
      sTestString_3 = "Teststring_3_XYZ"
      bSuccess, sResult = oFile.Append(sTestString_1)
      assert bSuccess is True
      bSuccess, sResult = oFile.Append(sTestString_2)
      assert bSuccess is True
      bSuccess, sResult = oFile.Append(sTestString_3)
      assert bSuccess is True
      bSuccess, sResult = oFile.Close()
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 3
      assert listLines[0] == sTestString_1
      assert listLines[1] == sTestString_2
      assert listLines[2] == sTestString_3
      bSuccess, sResult = oFile.Close()
      assert bSuccess is True
      del oFile


   @pytest.mark.parametrize(
      "Description", ["Delete, Append and Read without explicit Close",]
   )
   def test_CFile_5(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      sTestString_1 = "Teststring_1_ABC"
      sTestString_2 = "Teststring_2_MNO"
      sTestString_3 = "Teststring_3_XYZ"
      bSuccess, sResult = oFile.Delete(bConfirmDelete=False) # no matter if file exists from previous test run or not; only making sure that file does not exist (precondition)
      assert bSuccess is True
      bSuccess, sResult = oFile.Append(sTestString_1)
      assert bSuccess is True
      bSuccess, sResult = oFile.Append(sTestString_2)
      assert bSuccess is True
      bSuccess, sResult = oFile.Append(sTestString_3)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 3
      assert listLines[0] == sTestString_1
      assert listLines[1] == sTestString_2
      assert listLines[2] == sTestString_3
      del oFile


   @pytest.mark.parametrize(
      "Description", ["Write to new file; repeated ReadLines with filter",]
   )
   def test_CFile_6(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      sTestString_1 = " # ABC 1 test line (a)  "
      sTestString_2 = "  = BCD 22 test line (b)  "
      sTestString_3 = "   # CDE 333 test line (c)  "
      sTestString_4 = "    = DEF 4444 test line (d)  "
      bSuccess, sResult = oFile.Write(sTestString_1)
      assert bSuccess is True
      bSuccess, sResult = oFile.Write(sTestString_2)
      assert bSuccess is True
      bSuccess, sResult = oFile.Write(sTestString_3)
      assert bSuccess is True
      bSuccess, sResult = oFile.Write(sTestString_4)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines(sContains="CD") # with default: bLStrip=False, bRStrip=True
      assert bSuccess is True
      assert len(listLines) == 2
      assert listLines[0] == sTestString_2.rstrip()
      assert listLines[1] == sTestString_3.rstrip()
      listLines, bSuccess, sResult = oFile.ReadLines(sContains="CD", bLStrip=True, bRStrip=True)
      assert bSuccess is True
      assert len(listLines) == 2
      assert listLines[0] == sTestString_2.strip()
      assert listLines[1] == sTestString_3.strip()
      listLines, bSuccess, sResult = oFile.ReadLines(sContains="CD", bLStrip=False, bRStrip=False)
      assert bSuccess is True
      assert len(listLines) == 2
      assert listLines[0] == sTestString_2
      assert listLines[1] == sTestString_3
      listLines, bSuccess, sResult = oFile.ReadLines(sInclRegEx=r"\d{4}", bLStrip=False, bRStrip=False)
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == sTestString_4
      listLines, bSuccess, sResult = oFile.ReadLines(sComment="#", sContains="test") # with default: bLStrip=False, bRStrip=True
      assert bSuccess is True
      assert len(listLines) == 2
      assert listLines[0] == sTestString_2.rstrip()
      assert listLines[1] == sTestString_4.rstrip()
      del oFile


   @pytest.mark.parametrize(
      "Description", ["ReadLines; skip blank lines",]
   )
   def test_CFile_7(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      sTestString_1 = "  ABC  "
      sTestString_2 = ""
      sTestString_3 = "  DEF  "
      sTestString_4 = "      "
      sTestString_5 = "  ZYZ  "
      bSuccess, sResult = oFile.Write(sTestString_1)
      assert bSuccess is True
      bSuccess, sResult = oFile.Write(sTestString_2)
      assert bSuccess is True
      bSuccess, sResult = oFile.Write(sTestString_3)
      assert bSuccess is True
      bSuccess, sResult = oFile.Write(sTestString_4)
      assert bSuccess is True
      bSuccess, sResult = oFile.Write(sTestString_5)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines(bSkipBlankLines=True) # with default: bLStrip=False, bRStrip=True
      assert bSuccess is True
      assert len(listLines) == 3
      assert listLines[0] == sTestString_1.rstrip()
      assert listLines[1] == sTestString_3.rstrip()
      assert listLines[2] == sTestString_5.rstrip()
      del oFile


   @pytest.mark.parametrize(
      "Description", ["Write, Append and ReadLines combinations",]
   )
   def test_CFile_8(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      sTestString_1 = "ABC"
      sTestString_2 = "DEF"
      sTestString_3 = "ZYZ"
      bSuccess, sResult = oFile.Write(sTestString_1)
      assert bSuccess is True
      bSuccess, sResult = oFile.Append(sTestString_2)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 2
      assert listLines[0] == sTestString_1
      assert listLines[1] == sTestString_2
      bSuccess, sResult = oFile.Write(sTestString_3)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == sTestString_3
      bSuccess, sResult = oFile.Append(sTestString_1)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 2
      assert listLines[0] == sTestString_3
      assert listLines[1] == sTestString_1
      bSuccess, sResult = oFile.Write(sTestString_2)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == sTestString_2
      del oFile


   @pytest.mark.parametrize(
      "Description", ["Write and ReadLines of composite data types",]
   )
   def test_CFile_9(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"

      oFile = CFile(sFile)

      listValues = ["ABC", "OPQ", "ZYZ"]
      bSuccess, sResult = oFile.Write(listValues)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 3
      assert listLines[0] == listValues[0]
      assert listLines[1] == listValues[1]
      assert listLines[2] == listValues[2]

      tupleValues = [11, 22, 33]
      bSuccess, sResult = oFile.Write(tupleValues)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 3
      assert listLines[0] == str(tupleValues[0])
      assert listLines[1] == str(tupleValues[1])
      assert listLines[2] == str(tupleValues[2])

      setValues = {44, 55, 66}
      bSuccess, sResult = oFile.Write(setValues)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 3
      # a Python 3 'set' has no index!!
      assert "44" in listLines
      assert "55" in listLines
      assert "66" in listLines

      dictValues = {'kV_1' : 'Val1', 'kV__2' : 'Val2', 'kV___3' : 'Val3'}
      bSuccess, sResult = oFile.Write(dictValues)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 3
      assert listLines[0] == "  kV_1 : Val1"
      assert listLines[1] == " kV__2 : Val2"
      assert listLines[2] == "kV___3 : Val3"

      dotdictValues = dotdict(dictValues)
      bSuccess, sResult = oFile.Write(dictValues)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 3
      assert listLines[0] == "  kV_1 : Val1"
      assert listLines[1] == " kV__2 : Val2"
      assert listLines[2] == "kV___3 : Val3"

      del oFile


   @pytest.mark.parametrize(
      "Description", ["Write: Prefix and additional vertical space",]
   )
   def test_CFile_10(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"

      oFile = CFile(sFile)

      listValues = ["ABC", "OPQ", "ZYZ"]
      bSuccess, sResult = oFile.Write(listValues, nVSpaceAfter=2, sPrefix="* ")
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 5
      assert listLines[0] == "* " + listValues[0]
      assert listLines[1] == "* " + listValues[1]
      assert listLines[2] == "* " + listValues[2]
      assert listLines[3] == ""
      assert listLines[4] == ""

      tupleValues = [11, 22, 33]
      bSuccess, sResult = oFile.Write(tupleValues, nVSpaceAfter=2, sPrefix="+ ")
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 5
      assert listLines[0] == "+ " + str(tupleValues[0])
      assert listLines[1] == "+ " + str(tupleValues[1])
      assert listLines[2] == "+ " + str(tupleValues[2])
      assert listLines[3] == ""
      assert listLines[4] == ""

      setValues = {44, 55, 66}
      bSuccess, sResult = oFile.Write(setValues, nVSpaceAfter=1, sPrefix="- ")
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 4
      # a Python 3 'set' has no index!!
      assert "- 44" in listLines
      assert "- 55" in listLines
      assert "- 66" in listLines
      assert "" in listLines

      dictValues = {'kV_1' : 'Val1', 'kV__2' : 'Val2', 'kV___3' : 'Val3'}
      bSuccess, sResult = oFile.Write(dictValues, nVSpaceAfter=2, sPrefix="   ")
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 5
      assert listLines[0] == "     kV_1 : Val1"
      assert listLines[1] == "    kV__2 : Val2"
      assert listLines[2] == "   kV___3 : Val3"
      assert listLines[3] == ""
      assert listLines[4] == ""

      dotdictValues = dotdict(dictValues)
      bSuccess, sResult = oFile.Write(dotdictValues, nVSpaceAfter=2, sPrefix=" == ")
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 5
      assert listLines[0] == " ==   kV_1 : Val1"
      assert listLines[1] == " ==  kV__2 : Val2"
      assert listLines[2] == " == kV___3 : Val3"
      assert listLines[3] == ""
      assert listLines[4] == ""

      del oFile


   @pytest.mark.parametrize(
      "Description", ["Invalid source paths",]
   )
   def test_CFile_11(self, Description):
      """pytest 'CFile'"""
      sFile      = None
      sFile_copy = None
      sFile_move = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile      = r"%TMP%\IAmNotExisting\IAmNotExisting.txt"
         sFile_copy = r"%TMP%\CFile_TestFile_copied.txt"
         sFile_move = r"%TMP%\CFile_TestFile_moved.txt"
      elif sPlatformSystem == "Linux":
         sFile      = r"/tmp/IAmNotExisting/IAmNotExisting.txt"
         sFile_copy = r"/tmp/CFile_TestFile_copied.txt"
         sFile_move = r"/tmp/CFile_TestFile_moved.txt"

      oFile = CFile(sFile)
      bSuccess, sResult = oFile.Write("A B C")
      assert bSuccess is None
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is False
      bSuccess, sResult = oFile.Delete()
      assert bSuccess is False
      bSuccess, sResult = oFile.CopyTo(sFile_copy)
      assert bSuccess is False
      bSuccess, sResult = oFile.MoveTo(sFile_move)
      assert bSuccess is False
      del oFile


   @pytest.mark.parametrize(
      "Description", ["Invalid destination paths",]
   )
   def test_CFile_12(self, Description):
      """pytest 'CFile'"""
      sFile      = None
      sFile_copy = None
      sFile_move = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile      = r"%TMP%\CFile_TestFile.txt"
         sFile_copy = r"%TMP%\IAmNotExisting\CFile_TestFile_copied.txt"
         sFile_move = r"%TMP%\IAmNotExisting\CFile_TestFile_moved.txt"
      elif sPlatformSystem == "Linux":
         sFile      = r"/tmp/CFile_TestFile.txt"
         sFile_copy = r"/tmp/IAmNotExisting/CFile_TestFile_copied.txt"
         sFile_move = r"/tmp/IAmNotExisting/CFile_TestFile_moved.txt"

      oFile = CFile(sFile)
      bSuccess, sResult = oFile.Write("A B C")
      assert bSuccess is True
      bSuccess, sResult = oFile.CopyTo(sFile_copy)
      assert bSuccess is False
      bSuccess, sResult = oFile.MoveTo(sFile_move)
      assert bSuccess is False
      del oFile


   @pytest.mark.parametrize(
      "Description", ["CopyTo, MoveTo and GetFileInfo",]
   )
   def test_CFile_13(self, Description):
      """pytest 'CFile'"""
      sFile         = None
      sFile_copy    = None
      sFile_move    = None
      sFile_invalid = None
      sFilePath     = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile         = r"%TMP%\CFile_TestFile.txt"
         sFile_copy    = r"%TMP%\CFile_TestFile_copy.txt"
         sFile_move    = r"%TMP%\CFile_TestFile_move.txt"
         sFile_invalid = r"%TMP%\IAmNotExisting\IAmNotExisting.txt"
         sFilePath     = "%TMP%"
      elif sPlatformSystem == "Linux":
         sFile         = r"/tmp/CFile_TestFile.txt"
         sFile_copy    = r"/tmp/CFile_TestFile_copy.txt"
         sFile_move    = r"/tmp/CFile_TestFile_move.txt"
         sFile_invalid = r"/tmp/IAmNotExisting/IAmNotExisting.txt"
         sFilePath     = "/tmp"

      sFile_expected          = CString.NormalizePath(sFile)
      sFileName_expected      = "CFile_TestFile.txt"
      sFileExtension_expected = "txt"
      sFileNameOnly_expected  = "CFile_TestFile"
      sFilePath_expected      = CString.NormalizePath(sFilePath)

      sFile_expected_copy = CString.NormalizePath(sFile_copy)
      sFile_expected_move = CString.NormalizePath(sFile_move)

      sTestString = "A B C"

      oFile         = CFile(sFile)
      oFile_copy    = CFile(sFile_copy)
      oFile_move    = CFile(sFile_move)
      oFile_invalid = CFile(sFile_invalid)

      dFileInfo = oFile_invalid.GetFileInfo()
      assert dFileInfo['bFileIsExisting']     == False
      assert dFileInfo['bFilePathIsExisting'] == False

      bSuccess, sResult = oFile.Write(sTestString)
      assert bSuccess is True
      bSuccess, sResult = oFile.Delete()
      assert bSuccess is True
      dFileInfo = oFile.GetFileInfo()
      assert dFileInfo['sFile']               == sFile_expected
      assert dFileInfo['bFileIsExisting']     == False
      assert dFileInfo['sFileName']           == sFileName_expected
      assert dFileInfo['sFileExtension']      == sFileExtension_expected
      assert dFileInfo['sFileNameOnly']       == sFileNameOnly_expected
      assert dFileInfo['sFilePath']           == sFilePath_expected
      assert dFileInfo['bFilePathIsExisting'] == True
      bSuccess, sResult = oFile.Write(sTestString)
      assert bSuccess is True
      dFileInfo = oFile.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == True
      bSuccess, sResult = oFile_copy.Delete(bConfirmDelete=False) # no matter if file exists from previous test run or not; only making sure that file does not exist (precondition)
      assert bSuccess is True
      dFileInfo = oFile_copy.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == False
      del oFile_copy
      bSuccess, sResult = oFile.CopyTo(sFile_copy)
      assert bSuccess is True
      oFile_copy = CFile(sFile_copy)
      dFileInfo = oFile_copy.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == True
      listLines, bSuccess, sResult = oFile_copy.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == sTestString
      bSuccess, sResult = oFile_copy.Append(sTestString)
      assert bSuccess is True
      bSuccess, sResult = oFile_move.Delete(bConfirmDelete=False) # no matter if file exists from previous test run or not; only making sure that file does not exist (precondition)
      assert bSuccess is True
      dFileInfo = oFile_move.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == False
      del oFile_move
      bSuccess, sResult = oFile_copy.MoveTo(sFile_move)
      assert bSuccess is True
      dFileInfo = oFile_copy.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == False
      oFile_move = CFile(sFile_move)
      dFileInfo = oFile_move.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == True
      bSuccess, sResult = oFile_move.Append(sTestString)
      assert bSuccess is True
      listLines, bSuccess, sResult = oFile_move.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 3
      assert listLines[0] == sTestString
      assert listLines[1] == sTestString
      assert listLines[2] == sTestString

      del oFile
      del oFile_copy
      del oFile_move
      del oFile_invalid


   @pytest.mark.parametrize(
      "Description", ["ConfirmDelete",]
   )
   def test_CFile_14(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      bSuccess, sResult = oFile.Write("A B C")
      assert bSuccess is True
      dFileInfo = oFile.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == True
      bSuccess, sResult = oFile.Delete(bConfirmDelete=True) # default
      assert bSuccess is True
      dFileInfo = oFile.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == False
      bSuccess, sResult = oFile.Delete(bConfirmDelete=True) # default
      assert bSuccess is False
      bSuccess, sResult = oFile.Delete(bConfirmDelete=False)
      assert bSuccess is True
      del oFile


   @pytest.mark.parametrize(
      "Description", ["source file == dest file",]
   )
   def test_CFile_14(self, Description):
      """pytest 'CFile'"""
      sFile = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile = r"%TMP%\CFile_TestFile.txt"
      elif sPlatformSystem == "Linux":
         sFile = r"/tmp/CFile_TestFile.txt"
      oFile = CFile(sFile)
      bSuccess, sResult = oFile.Write("A B C")
      assert bSuccess is True
      dFileInfo = oFile.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == True
      bSuccess, sResult = oFile.CopyTo(sFile)
      assert bSuccess is False
      bSuccess, sResult = oFile.MoveTo(sFile)
      assert bSuccess is False
      dFileInfo = oFile.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == True
      listLines, bSuccess, sResult = oFile.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == "A B C"
      del oFile


   @pytest.mark.parametrize(
      "Description", ["bOverwrite and access violations",]
   )
   def test_CFile_15(self, Description):
      """pytest 'CFile'"""
      sFile_1 = None
      sFile_2 = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFile_1 = r"%TMP%\CFile_TestFile_1.txt"
         sFile_2 = r"%TMP%\CFile_TestFile_2.txt"
      elif sPlatformSystem == "Linux":
         sFile_1 = r"/tmp/CFile_TestFile_1.txt"
         sFile_2 = r"/tmp/CFile_TestFile_2.txt"
      oFile_1 = CFile(sFile_1)
      oFile_2 = CFile(sFile_2)
      bSuccess, sResult = oFile_1.Write("A B C")
      assert bSuccess is True
      bSuccess, sResult = oFile_2.Write("X Y Z")
      assert bSuccess is True
      bSuccess, sResult = oFile_1.Close()
      assert bSuccess is True
      bSuccess, sResult = oFile_2.Close()
      assert bSuccess is True
      dFileInfo = oFile_1.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == True
      dFileInfo = oFile_2.GetFileInfo()
      assert dFileInfo['bFileIsExisting'] == True
      del oFile_2
      # file 2 is closed, but not allowed to be overwritten
      bSuccess, sResult = oFile_1.CopyTo(sFile_2, bOverwrite=False)
      assert bSuccess is False
      # file 2 is expected to have still the same content as before
      oFile_2 = CFile(sFile_2)
      listLines, bSuccess, sResult = oFile_2.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == "X Y Z"
      del oFile_2
      # file 2 is closed, and is allowed to be overwritten
      bSuccess, sResult = oFile_1.CopyTo(sFile_2, bOverwrite=True)
      assert bSuccess is True
      # file 2 is expected to have the content of file 1
      oFile_2 = CFile(sFile_2)
      listLines, bSuccess, sResult = oFile_2.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == "A B C"
      # change the content of file 1
      bSuccess, sResult = oFile_1.Append("D E F")
      assert bSuccess is True
      # check the new content of file 1
      listLines, bSuccess, sResult = oFile_1.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 2
      assert listLines[0] == "A B C"
      assert listLines[1] == "D E F"
      # try to copy file 1 to file 2 - but file 2 is still in access
      bSuccess, sResult = oFile_1.CopyTo(sFile_2, bOverwrite=True)
      assert bSuccess is False
      # again check the content of file 2 - must be the same as before
      listLines, bSuccess, sResult = oFile_2.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == "A B C"
      # try to move file 1 to file 2 - but file 2 is still in access
      bSuccess, sResult = oFile_1.MoveTo(sFile_2, bOverwrite=True)
      assert bSuccess is False
      # again check the content of file 2 - must be the same as before
      listLines, bSuccess, sResult = oFile_2.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 1
      assert listLines[0] == "A B C"
      # and also file 1 must still exist with the same content as before
      listLines, bSuccess, sResult = oFile_1.ReadLines()
      assert bSuccess is True
      assert len(listLines) == 2
      assert listLines[0] == "A B C"
      assert listLines[1] == "D E F"
      del oFile_1
      del oFile_2
      # two instances with the same file (not allowed)
      bException = False
      try:
         oFile_1_a = CFile(sFile_1)
      except:
         bException = True
      assert bException is False
      bException = False
      try:
         oFile_1_b = CFile(sFile_1)
         bException = False
      except:
         bException = True
      assert bException is True
      del oFile_1_a

# eof class Test_CFile

# --------------------------------------------------------------------------------------------------------------
