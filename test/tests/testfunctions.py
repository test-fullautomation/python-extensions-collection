# **************************************************************************************************************
#
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
#
# **************************************************************************************************************
#
# testfunctions.py
#
# XC-CT/ECA3-Queckenstedt
#
# --------------------------------------------------------------------------------------------------------------
#
# 03.08.2023
#
# --------------------------------------------------------------------------------------------------------------

import os, sys, platform

import colorama as col

from PythonExtensionsCollection.String.CString import CString
from PythonExtensionsCollection.File.CFile import CFile
from PythonExtensionsCollection.Folder.CFolder import CFolder

col.init(autoreset=True)

COLBR = col.Style.BRIGHT + col.Fore.RED
COLBY = col.Style.BRIGHT + col.Fore.YELLOW
COLBG = col.Style.BRIGHT + col.Fore.GREEN

SUCCESS = 0
ERROR   = 1

# --------------------------------------------------------------------------------------------------------------

def printerror(sMsg):
    sys.stderr.write(COLBR + f"Error: {sMsg}!\n")

# --------------------------------------------------------------------------------------------------------------

# ==============================================================================================================
#                                        TESTFUNCTIONS
# ==============================================================================================================
#TM***

# --------------------------------------------------------------------------------------------------------------
# CFile
# --------------------------------------------------------------------------------------------------------------

def PEC_0001(oConfig):
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   sTestString = "Teststring-1"
   bSuccess, sResult = oFile.Write(sTestString)
   if bSuccess is not True:
      del oFile
      return bSuccess, sResult
   bSuccess, sResult = oFile.Close()
   if bSuccess is not True:
      del oFile
      return bSuccess, sResult
   listLines, bSuccess, sResult = oFile.ReadLines()
   if bSuccess is not True:
      del oFile
      return bSuccess, sResult
   if len(listLines) != 1:
      del oFile
      return False, "not: len(listLines) != 1"
   if listLines[0] != sTestString:
      del oFile
      return False, "not: listLines[0] != sTestString"
   bSuccess, sResult = oFile.Close()
   if bSuccess is not True:
      del oFile
      return bSuccess, sResult
   del oFile
   os.remove(sFile)
   return True, "Done"

# --------------------------------------------------------------------------------------------------------------

def PEC_0002(oConfig):
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)

   sTestString = "Teststring-2"
   bSuccess, sResult = oFile.Write(sTestString)
   if bSuccess is not True:
      del oFile
      return bSuccess, sResult
   listLines, bSuccess, sResult = oFile.ReadLines()
   if bSuccess is not True:
      del oFile
      return bSuccess, sResult
   if len(listLines) != 1:
      del oFile
      return False, "not: len(listLines) != 1"
   if listLines[0] != sTestString:
      del oFile
      return False, "not: listLines[0] != sTestString"

   del oFile
   os.remove(sFile)
   return True, "Done"

# --------------------------------------------------------------------------------------------------------------

def PEC_0003(oConfig):
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   bSuccess, sResult = oFile.Write("Dummy")
   if bSuccess is not True:
      del oFile
      return bSuccess, sResult
   bSuccess, sResult = oFile.Delete()
   if bSuccess is not True:
      del oFile
      return bSuccess, sResult
   del oFile
   return True, "Done"

# --------------------------------------------------------------------------------------------------------------



