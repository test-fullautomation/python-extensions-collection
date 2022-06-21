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
# test_CFolder.py
#
# XC-CT/ECA3-Queckenstedt
#
# 10.06.2022
#
# --------------------------------------------------------------------------------------------------------------

# -- import standard Python modules
import os, sys, time, platform, pytest, stat

# -- import own Python modules (containing the code to be tested)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))) # to make sure to hit the package relative to this file at first
from PythonExtensionsCollection.Folder.CFolder import CFolder
from PythonExtensionsCollection.File.CFile import CFile
from PythonExtensionsCollection.String.CString import CString

# --------------------------------------------------------------------------------------------------------------

class Test_CFolder:
   """Tests of module CFolder."""

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   @pytest.mark.parametrize(
      "Description", ["Create a folder, bOverwrite=False",]
   )
   def test_CFolder_1(self, Description):
      """pytest 'CFolder'"""
      sFolder = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFolder = os.path.expandvars(r"%TMP%\CFolder_TestFolder")
      elif sPlatformSystem == "Linux":
         sFolder = r"/tmp/CFolder_TestFolder"

      # test file for test folder
      sTestFile = f"{sFolder}/CFolder_TestFile.txt"

      # initial test folder creation with bOverwrite=True
      oFolder = CFolder(sFolder)
      bSuccess, sResult = oFolder.Create(bOverwrite=True, bRecursive=False)
      assert bSuccess is True

      # expected: folder exists
      assert os.path.isdir(sFolder) is True

      # expected: test file not exists
      assert os.path.isfile(sTestFile) is False

      # create test file within test folder
      oTestFile = CFile(sTestFile)
      bSuccess, sResult = oTestFile.Write(sTestFile)
      assert bSuccess is True
      bSuccess, sResult = oTestFile.Close()
      assert bSuccess is True
      del oTestFile

      # expected: test file exists
      assert os.path.isfile(sTestFile) is True

      # test folder creation with bOverwrite=False
      bSuccess, sResult = oFolder.Create(bOverwrite=False, bRecursive=False)
      assert bSuccess is True

      # expected: folder still exists
      assert os.path.isdir(sFolder) is True

      # expected: test file still exists
      assert os.path.isfile(sTestFile) is True

      # tidying up
      del oFolder

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   @pytest.mark.parametrize(
      "Description", ["Create a folder, bOverwrite=True",]
   )
   def test_CFolder_2(self, Description):
      """pytest 'CFolder'"""
      sFolder = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFolder = os.path.expandvars(r"%TMP%\CFolder_TestFolder")
      elif sPlatformSystem == "Linux":
         sFolder = r"/tmp/CFolder_TestFolder"

      # test file for test folder
      sTestFile = f"{sFolder}/CFolder_TestFile.txt"

      # initial test folder creation with bOverwrite=True
      oFolder = CFolder(sFolder)
      bSuccess, sResult = oFolder.Create(bOverwrite=True, bRecursive=False)
      assert bSuccess is True

      # expected: folder exists
      assert os.path.isdir(sFolder) is True

      # expected: test file not exists
      assert os.path.isfile(sTestFile) is False

      # create test file within test folder
      oTestFile = CFile(sTestFile)
      bSuccess, sResult = oTestFile.Write(sTestFile)
      assert bSuccess is True
      bSuccess, sResult = oTestFile.Close()
      assert bSuccess is True
      del oTestFile

      # expected: test file exists
      assert os.path.isfile(sTestFile) is True

      # test folder creation with bOverwrite=True
      bSuccess, sResult = oFolder.Create(bOverwrite=True, bRecursive=False)
      assert bSuccess is True

      # expected: folder still exists
      assert os.path.isdir(sFolder) is True

      # expected: test file not exists
      assert os.path.isfile(sTestFile) is False

      # tidying up
      del oFolder

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   @pytest.mark.parametrize(
      "Description", ["Create a folder, bOverwrite=True, open file handle, (! test needs some time - internal loop of tries !)",]
   )
   def test_Windows_CFolder_3(self, Description):
      """pytest 'CFolder'"""
      sFolder = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFolder = os.path.expandvars(r"%TMP%\CFolder_TestFolder")
      elif sPlatformSystem == "Linux":
         sFolder = r"/tmp/CFolder_TestFolder"

      # test file for test folder
      sTestFile = f"{sFolder}/CFolder_TestFile.txt"

      # initial test folder creation with bOverwrite=True
      oFolder = CFolder(sFolder)
      bSuccess, sResult = oFolder.Create(bOverwrite=True, bRecursive=False)
      assert bSuccess is True

      # expected: folder exists
      assert os.path.isdir(sFolder) is True

      # expected: test file not exists
      assert os.path.isfile(sTestFile) is False

      # create test file within test folder
      oTestFile = CFile(sTestFile)
      bSuccess, sResult = oTestFile.Write(sTestFile)
      assert bSuccess is True

      # !! without Close() the file handle is still open, this causes an access violation and it should not be possible to delete the folder
      #    >>> under Windows only !!!
      # !! bSuccess, sResult = oTestFile.Close()
      # !! assert bSuccess is True
      # !! del oTestFile

      # expected: test file exists
      assert os.path.isfile(sTestFile) is True

      # test folder creation with bOverwrite=True
      # (this includes an internal Delete() running in loop several times, therefore this test needs some time,
      # because of an access violation it is expected that the folder cannot be deleted and Create()
      # returns an error)
      bSuccess, sResult = oFolder.Create(bOverwrite=True, bRecursive=False)
      assert bSuccess is False

      # expected: folder still exists
      assert os.path.isdir(sFolder) is True

      # expected: test file still exists
      assert os.path.isfile(sTestFile) is True

      # cross check
      bSuccess, sResult = oFolder.Create(bOverwrite=False, bRecursive=False)
      assert bSuccess is True

      # tidying up
      bSuccess, sResult = oTestFile.Close()
      assert bSuccess is True
      del oTestFile

      del oFolder

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   @pytest.mark.parametrize(
      "Description", ["Create a folder, bOverwrite=True, open file handle",]
   )
   def test_Linux_CFolder_3(self, Description):
      """pytest 'CFolder'"""
      sFolder = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFolder = os.path.expandvars(r"%TMP%\CFolder_TestFolder")
      elif sPlatformSystem == "Linux":
         sFolder = r"/tmp/CFolder_TestFolder"

      # test file for test folder
      sTestFile = f"{sFolder}/CFolder_TestFile.txt"

      # initial test folder creation with bOverwrite=True
      oFolder = CFolder(sFolder)
      bSuccess, sResult = oFolder.Create(bOverwrite=True, bRecursive=False)
      assert bSuccess is True

      # expected: folder exists
      assert os.path.isdir(sFolder) is True

      # expected: test file not exists
      assert os.path.isfile(sTestFile) is False

      # create test file within test folder
      oTestFile = CFile(sTestFile)
      bSuccess, sResult = oTestFile.Write(sTestFile)
      assert bSuccess is True

      # !! without Close() the file handle is still open, under Linux this doesn't matter
      # !! bSuccess, sResult = oTestFile.Close()
      # !! assert bSuccess is True
      # !! del oTestFile

      # expected: test file exists
      assert os.path.isfile(sTestFile) is True

      # test folder creation with bOverwrite=True
      # (this includes an internal Delete() running in loop several times, therefore this test needs some time,
      bSuccess, sResult = oFolder.Create(bOverwrite=True, bRecursive=False)
      assert bSuccess is True

      # expected: folder exists
      assert os.path.isdir(sFolder) is True

      # expected: test file not exists
      assert os.path.isfile(sTestFile) is False

      # cross check
      bSuccess, sResult = oFolder.Create(bOverwrite=False, bRecursive=False)
      assert bSuccess is True

      # tidying up
      bSuccess, sResult = oTestFile.Close()
      assert bSuccess is True
      del oTestFile

      del oFolder

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   @pytest.mark.parametrize(
      "Description", ["Multiple CFolder instances of same folder",]
   )
   def test_CFolder_4(self, Description):
      """pytest 'CFolder'"""
      sFolder = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFolder = os.path.expandvars(r"%TMP%\CFolder_TestFolder")
      elif sPlatformSystem == "Linux":
         sFolder = r"/tmp/CFolder_TestFolder"

      # first CFolder instance expected to be created without exception
      bException = False
      try:
         oFolder_1 = CFolder(sFolder)
      except Exception as reason:
         bException = True
      assert bException is False

      # further CFolder instance of same folder must cause an exception
      bException = False
      try:
         oFolder_2 = CFolder(sFolder)
      except Exception as reason:
         bException = True
      assert bException is True

      # deletion of first (and only) CFolder instance must enable to create again an instance with same folder
      del oFolder_1
      bException = False
      try:
         oFolder_2 = CFolder(sFolder)
      except Exception as reason:
         bException = True
      assert bException is False

      # tidying up
      del oFolder_2

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   @pytest.mark.parametrize(
      "Description", ["Create and delete a folder, bRecursive=True",]
   )
   def test_CFolder_5(self, Description):
      """pytest 'CFolder'"""
      sFolder = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFolder = os.path.expandvars(r"%TMP%\CFo\ld\er_Te\st\Fol\der")
      elif sPlatformSystem == "Linux":
         sFolder = r"/tmp/CFo/ld/er_Te/st/Fol/der"

      sParentFolder = os.path.dirname(sFolder)

      # test file for test folder
      sTestFile = f"{sFolder}/CFolder_TestFile.txt"

      # initial test folder creation with bOverwrite=True
      oFolder = CFolder(sFolder)
      bSuccess, sResult = oFolder.Create(bOverwrite=True, bRecursive=True)
      assert bSuccess is True

      # expected: folder exists
      assert os.path.isdir(sFolder) is True

      # expected: test file not exists
      assert os.path.isfile(sTestFile) is False

      # create test file within test folder
      oTestFile = CFile(sTestFile)
      bSuccess, sResult = oTestFile.Write(sTestFile)
      assert bSuccess is True
      bSuccess, sResult = oTestFile.Close()
      assert bSuccess is True
      del oTestFile

      # expected: test file exists
      assert os.path.isfile(sTestFile) is True

      # test folder creation with bOverwrite=False
      bSuccess, sResult = oFolder.Create(bOverwrite=False, bRecursive=True)
      assert bSuccess is True

      # expected: folder still exists
      assert os.path.isdir(sFolder) is True

      # expected: test file still exists
      assert os.path.isfile(sTestFile) is True

      # delete test folder
      bSuccess, sResult = oFolder.Delete(bConfirmDelete=True)
      assert bSuccess is True

      # expected: test file not exists
      assert os.path.isfile(sTestFile) is False

      # expected: folder not exists
      assert os.path.isdir(sFolder) is False

      # expected: parent folder exists
      assert os.path.isdir(sParentFolder) is True

      # try to delete same test folder again; but folder does not exist any more; because of a confirmation is requested, Delete() returns an error
      bSuccess, sResult = oFolder.Delete(bConfirmDelete=True)
      assert bSuccess is False

      # try to delete same test folder again; but folder does not exist any more; because of a confirmation is not requested, Delete() returns success
      bSuccess, sResult = oFolder.Delete(bConfirmDelete=False)
      assert bSuccess is True

      # tidying up
      del oFolder

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   @pytest.mark.parametrize(
      "Description", ["Delete a folder with content write protected",]
   )
   def test_CFolder_6(self, Description):
      """pytest 'CFolder'"""
      sFolder = None
      sPlatformSystem = platform.system()
      if sPlatformSystem == "Windows":
         sFolder = os.path.expandvars(r"%TMP%\CFolder_TestFolder")
      elif sPlatformSystem == "Linux":
         sFolder = r"/tmp/CFolder_TestFolder"

      sSubFolder_1 = f"{sFolder}/sub1"
      sSubFolder_2 = f"{sFolder}/sub2"
      sTestFile_1  = f"{sSubFolder_1}/TestFile_1.txt"
      sTestFile_2  = f"{sSubFolder_2}/TestFile_2.txt"

      # initial test folder creation with bOverwrite=True
      oFolder = CFolder(sFolder)
      bSuccess, sResult = oFolder.Create(bOverwrite=True, bRecursive=True)
      assert bSuccess is True

      # expected: folder exists
      assert os.path.isdir(sFolder) is True

      # expected: sub folder not exists
      assert os.path.isdir(sSubFolder_1) is False
      assert os.path.isdir(sSubFolder_2) is False

      # sub folder creation
      oSubFolder_1 = CFolder(sSubFolder_1)
      bSuccess, sResult = oSubFolder_1.Create()
      assert bSuccess is True
      del oSubFolder_1
      assert os.path.isdir(sSubFolder_1) is True
      oSubFolder_2 = CFolder(sSubFolder_2)
      bSuccess, sResult = oSubFolder_2.Create()
      assert bSuccess is True
      del oSubFolder_2
      assert os.path.isdir(sSubFolder_1) is True

      # test file creation
      oTestFile_1 = CFile(sTestFile_1)
      bSuccess, sResult = oTestFile_1.Write(sTestFile_1)
      assert bSuccess is True
      bSuccess, sResult = oTestFile_1.Close()
      assert bSuccess is True
      del oTestFile_1
      assert os.path.isfile(sTestFile_1) is True
      oTestFile_2 = CFile(sTestFile_2)
      bSuccess, sResult = oTestFile_2.Write(sTestFile_2)
      assert bSuccess is True
      bSuccess, sResult = oTestFile_2.Close()
      assert bSuccess is True
      del oTestFile_2
      assert os.path.isfile(sTestFile_2) is True

      # make test files write protected
      os.chmod(sTestFile_1, stat.S_IREAD)
      os.chmod(sTestFile_2, stat.S_IREAD)

      # delete entire test folder
      bSuccess, sResult = oFolder.Delete(bConfirmDelete=True)
      assert bSuccess is True

      # check outcome
      assert os.path.isfile(sTestFile_1) is False
      assert os.path.isfile(sTestFile_2) is False
      assert os.path.isdir(sSubFolder_1) is False
      assert os.path.isdir(sSubFolder_2) is False
      assert os.path.isdir(sFolder) is False

      # and some further tries
      bSuccess, sResult = oFolder.Delete(bConfirmDelete=True)
      assert bSuccess is False
      bSuccess, sResult = oFolder.Delete(bConfirmDelete=False)
      assert bSuccess is True

      # tidying up
      del oFolder

   # --------------------------------------------------------------------------------------------------------------

# eof class Test_CFolder

# --------------------------------------------------------------------------------------------------------------
