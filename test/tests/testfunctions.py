﻿# **************************************************************************************************************
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
# 11.08.2023
#
# --------------------------------------------------------------------------------------------------------------

import os, sys, platform, stat, shutil
from dotdict import dotdict
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

def compare(valuepairs = [], prefix=None):
   # 'valuepairs' expected to be a tuple of tuples of 2 elements: received value and expected value
   bSuccess = True
   sResult  = "valid"
   listDeviations = []
   for tupleValues in valuepairs:
      if len(tupleValues) == 2:
         sReceived = f"{tupleValues[0]}"
         sExpected = f"{tupleValues[1]}"
         if sReceived != sExpected:
            sDeviation = f"Expected: '{sExpected}', but received: '{sReceived}'."
            listDeviations.append(sDeviation)
      elif len(tupleValues) == 3:
         sReceived = f"{tupleValues[0]}"
         sExpected = f"{tupleValues[1]}"
         sLabel    = f"{tupleValues[2]}"
         if sReceived != sExpected:
            sDeviation = f"Expected: '{sExpected}', but received: '{sReceived}' ({sLabel})."
            listDeviations.append(sDeviation)
      else:
         bSuccess = None
         sResult  = "Invalid input (expected tuple with 2 or 3 values)"
         return bSuccess, sResult
   # eof for tupleValues in valuepairs:
   if len(listDeviations) > 0:
      bSuccess = False
      sResult  = "Deviation"
      if prefix is not None:
         sResult = f"{sResult} ({prefix})"
      sResult = f"{sResult}!\n" + "\n".join(listDeviations)
   return bSuccess, sResult
# eof def compare(valuepairs = [], prefix=None):

# --------------------------------------------------------------------------------------------------------------

def is_file(sFile=None):
   bSuccess = None
   sResult  = "UNKNOWN"
   if sFile is None:
      bSuccess = None
      sResult  = "sFile is None"
   elif os.path.isfile(sFile) is True:
      bSuccess = True
      sResult  = f"File '{sFile}' exists"
   else:
      bSuccess = False
      sResult  = f"File '{sFile}' does not exist"
   return bSuccess, sResult
# eof def is_file(sFile=None):

# --------------------------------------------------------------------------------------------------------------

def is_folder(sFolder=None):
   bSuccess = None
   sResult  = "UNKNOWN"
   if sFolder is None:
      bSuccess = None
      sResult  = "sFolder is None"
   elif os.path.isdir(sFolder) is True:
      bSuccess = True
      sResult  = f"Folder '{sFolder}' exists"
   else:
      bSuccess = False
      sResult  = f"Folder '{sFolder}' does not exist"
   return bSuccess, sResult
# eof def is_folder(sFolder=None):

# --------------------------------------------------------------------------------------------------------------

class CResult:
   def __init__(self):
      self.__listResults = []
   def __deinit__(self):
      del self.__listResults
   def Results(self, sResult=None):
      if sResult is not None:
         self.__listResults.append(f"{sResult}")
      return "\n".join(self.__listResults)

# --------------------------------------------------------------------------------------------------------------

# ==============================================================================================================
#                                        TESTFUNCTIONS
# ==============================================================================================================

# --------------------------------------------------------------------------------------------------------------
# CFile
# --------------------------------------------------------------------------------------------------------------
#TM***

def PEC_0001(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   sTestString = "Teststring-1"
   bSuccess, sResult = oFile.Write(sTestString)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # read what has been written
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0001 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0002(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   sTestString = "Teststring-2"
   bSuccess, sResult = oFile.Write(sTestString)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # read what has been written
   listLines, bSuccess, sResult = oFile.ReadLines()
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0002 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0003(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   bSuccess, sResult = oFile.Write("Dummy")
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # delete created file
   bSuccess, sResult = oFile.Delete()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   return True, oResults.Results("PEC_0003 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0004(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   bSuccess, sResult = oFile.Delete(bConfirmDelete=False) # no matter if file exists from previous test run or not; only making sure that file does not exist (precondition)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   sTestString_1 = "Teststring_1_ABC"
   sTestString_2 = "Teststring_2_MNO"
   sTestString_3 = "Teststring_3_XYZ"
   # append 3 test strings
   bSuccess, sResult = oFile.Append(sTestString_1)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Append(sTestString_2)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Append(sTestString_3)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # read what has been appended
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 3, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_1),
                                (listLines[1], sTestString_2),
                                (listLines[2], sTestString_3)))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0004 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0005(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   bSuccess, sResult = oFile.Delete(bConfirmDelete=False) # no matter if file exists from previous test run or not; only making sure that file does not exist (precondition)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   sTestString_1 = "Teststring_1_ABC"
   sTestString_2 = "Teststring_2_MNO"
   sTestString_3 = "Teststring_3_XYZ"
   # append 3 test strings
   bSuccess, sResult = oFile.Append(sTestString_1)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Append(sTestString_2)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Append(sTestString_3)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # (here no Close() before ReadLines()!)
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 3, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_1),
                                (listLines[1], sTestString_2),
                                (listLines[2], sTestString_3)))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0005 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0006(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   sTestString_1 = " # ABC 1 test line (a)  "
   sTestString_2 = "  = BCD 22 test line (b)  "
   sTestString_3 = "   # CDE 333 test line (c)  "
   sTestString_4 = "    = DEF 4444 test line (d)  "
   # write content to file
   bSuccess, sResult = oFile.Write(sTestString_1)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString_2)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString_3)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString_4)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # read filtered content from file
   listLines, bSuccess, sResult = oFile.ReadLines(sContains="CD") # with default: bLStrip=False, bRStrip=True
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 2, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_2.rstrip()),
                                (listLines[1], sTestString_3.rstrip())))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines(sContains="CD", bLStrip=True, bRStrip=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 2, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_2.strip()),
                                (listLines[1], sTestString_3.strip())))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines(sContains="CD", bLStrip=False, bRStrip=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 2, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_2),
                                (listLines[1], sTestString_3)))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines(sInclRegEx=r"\d{4}", bLStrip=False, bRStrip=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_4),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines(sComment="#", sContains="test") # with default: bLStrip=False, bRStrip=True
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 2, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_2.rstrip()),
                                (listLines[1], sTestString_4.rstrip())))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0006 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0007(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   sTestString_1 = "  ABC  "
   sTestString_2 = ""
   sTestString_3 = "  DEF  "
   sTestString_4 = "      "
   sTestString_5 = "  ZYZ  "
   # write content to file
   bSuccess, sResult = oFile.Write(sTestString_1)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString_2)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString_3)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString_4)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString_5)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # read what has been written, but without blank lines
   listLines, bSuccess, sResult = oFile.ReadLines(bSkipBlankLines=True) # with default: bLStrip=False, bRStrip=True
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 3, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_1.rstrip()),
                                (listLines[1], sTestString_3.rstrip()),
                                (listLines[2], sTestString_5.rstrip())))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0007 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0008(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   sTestString_1 = "ABC"
   sTestString_2 = "DEF"
   sTestString_3 = "ZYZ"
   # Write, Append and ReadLines combinations
   bSuccess, sResult = oFile.Write(sTestString_1)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Append(sTestString_2)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 2, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_1),
                                (listLines[1], sTestString_2)))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString_3)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_3),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Append(sTestString_1)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 2, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_3),
                                (listLines[1], sTestString_1)))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString_2)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_2),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0008 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0009(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   # Write and ReadLines of composite data types
   listValues = ["ABC", "OPQ", "ZYZ"]
   bSuccess, sResult = oFile.Write(listValues)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 3, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], listValues[0]),
                                (listLines[1], listValues[1]),
                                (listLines[2], listValues[2])))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   tupleValues = [11, 22, 33]
   bSuccess, sResult = oFile.Write(tupleValues)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 3, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], str(tupleValues[0])),
                                (listLines[1], str(tupleValues[1])),
                                (listLines[2], str(tupleValues[2]))))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   setValues = {44, 55, 66}
   bSuccess, sResult = oFile.Write(setValues)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 3, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # a Python 3 'set' has no index!!
   if "44" not in listLines: del oFile; oResults.Results("\"44\" not in listLines"); return False, oResults.Results()
   if "55" not in listLines: del oFile; oResults.Results("\"55\" not in listLines"); return False, oResults.Results()
   if "66" not in listLines: del oFile; oResults.Results("\"66\" not in listLines"); return False, oResults.Results()
   dictValues = {'kV_1' : 'Val1', 'kV__2' : 'Val2', 'kV___3' : 'Val3'}
   bSuccess, sResult = oFile.Write(dictValues)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()

   bSuccess, sResult = compare(((len(listLines), 3, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], "  kV_1 : Val1"),
                                (listLines[1], " kV__2 : Val2"),
                                (listLines[2], "kV___3 : Val3")))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   dotdictValues = dotdict(dictValues)
   bSuccess, sResult = oFile.Write(dictValues)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()

   bSuccess, sResult = compare(((len(listLines), 3, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], "  kV_1 : Val1"),
                                (listLines[1], " kV__2 : Val2"),
                                (listLines[2], "kV___3 : Val3")))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0009 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0010(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   listValues = ["ABC", "OPQ", "ZYZ"]
   # Write with additional vertical space and prefix
   bSuccess, sResult = oFile.Write(listValues, nVSpaceAfter=2, sPrefix="* ")
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 5, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], f"* {listValues[0]}"),
                                (listLines[1], f"* {listValues[1]}"),
                                (listLines[2], f"* {listValues[2]}"),
                                (listLines[3], ""),
                                (listLines[4], "")))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   tupleValues = [11, 22, 33]
   bSuccess, sResult = oFile.Write(tupleValues, nVSpaceAfter=2, sPrefix="+ ")
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 5, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], f"+ {tupleValues[0]}"),
                                (listLines[1], f"+ {tupleValues[1]}"),
                                (listLines[2], f"+ {tupleValues[2]}"),
                                (listLines[3], ""),
                                (listLines[4], "")))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   setValues = {44, 55, 66}
   bSuccess, sResult = oFile.Write(setValues, nVSpaceAfter=1, sPrefix="- ")
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 4, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # a Python 3 'set' has no index!!
   if "- 44" not in listLines: del oFile; oResults.Results("\"- 44\" not in listLines"); return False, oResults.Results()
   if "- 55" not in listLines: del oFile; oResults.Results("\"- 55\" not in listLines"); return False, oResults.Results()
   if "- 66" not in listLines: del oFile; oResults.Results("\"- 66\" not in listLines"); return False, oResults.Results()
   if "" not in listLines: del oFile; oResults.Results("\"\" not in listLines"); return False, oResults.Results()
   dictValues = {'kV_1' : 'Val1', 'kV__2' : 'Val2', 'kV___3' : 'Val3'}
   bSuccess, sResult = oFile.Write(dictValues, nVSpaceAfter=2, sPrefix="   ")
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 5, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], "     kV_1 : Val1"),
                                (listLines[1], "    kV__2 : Val2"),
                                (listLines[2], "   kV___3 : Val3"),
                                (listLines[3], ""),
                                (listLines[4], "")))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   dictValues = {'kV_1' : 'Val1', 'kV__2' : 'Val2', 'kV___3' : 'Val3'}
   dotdictValues = dotdict(dictValues)
   bSuccess, sResult = oFile.Write(dotdictValues, nVSpaceAfter=2, sPrefix=" == ")
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 5, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], " ==   kV_1 : Val1"),
                                (listLines[1], " ==  kV__2 : Val2"),
                                (listLines[2], " == kV___3 : Val3"),
                                (listLines[3], ""),
                                (listLines[4], "")))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0010 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0011(oConfig):
   oResults = CResult()
   sFilePath     = oConfig.Get('TMPFILESFOLDER')
   sFile         = oConfig.Get('CFILE_TESTFILE')
   sFile_invalid = oConfig.Get('CFILE_TESTFILE_NOTEXISTINGPATH')
   sFile_copy    = oConfig.Get('CFILE_TESTFILE_COPIED')
   sFile_move    = oConfig.Get('CFILE_TESTFILE_MOVED')
   sFile_expected          = sFile
   sFileName_expected      = "CFile_TestFile.txt"
   sFileExtension_expected = "txt"
   sFileNameOnly_expected  = "CFile_TestFile"
   sFilePath_expected      = sFilePath
   sFile_expected_copy = sFile_copy
   sFile_expected_move = sFile_move
   sTestString = "A B C"
   oFile         = CFile(sFile)
   oFile_invalid = CFile(sFile_invalid)
   dFileInfo = oFile_invalid.GetFileInfo()
   # get file info from copied and moved files
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], False),
                                (dFileInfo['bFilePathIsExisting'], False)))
   del oFile_invalid
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Delete()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   dFileInfo = oFile.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['sFile'], sFile_expected),
                                (dFileInfo['bFileIsExisting'], False),
                                (dFileInfo['sFileName'], sFileName_expected),
                                (dFileInfo['sFileExtension'], sFileExtension_expected),
                                (dFileInfo['sFileNameOnly'], sFileNameOnly_expected),
                                (dFileInfo['sFilePath'], sFilePath_expected),
                                (dFileInfo['bFilePathIsExisting'], True)))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Write(sTestString)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   dFileInfo = oFile.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], True),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   oFile_copy = CFile(sFile_copy)
   bSuccess, sResult = oFile_copy.Delete(bConfirmDelete=False) # no matter if file exists from previous test run or not; only making sure that file does not exist (precondition)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; del oFile_copy; return bSuccess, oResults.Results()
   dFileInfo = oFile_copy.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], False),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; del oFile_copy; return bSuccess, oResults.Results()
   del oFile_copy
   bSuccess, sResult = oFile.CopyTo(sFile_copy)
   del oFile
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   oFile_copy = CFile(sFile_copy)
   dFileInfo = oFile_copy.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], True),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile_copy.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile_copy.Append(sTestString)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; return bSuccess, oResults.Results()
   oFile_move = CFile(sFile_move)
   bSuccess, sResult = oFile_move.Delete(bConfirmDelete=False) # no matter if file exists from previous test run or not; only making sure that file does not exist (precondition)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; del oFile_move; return bSuccess, oResults.Results()
   dFileInfo = oFile_move.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], False),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; del oFile_move; return bSuccess, oResults.Results()
   del oFile_move
   bSuccess, sResult = oFile_copy.MoveTo(sFile_move)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; return bSuccess, oResults.Results()
   dFileInfo = oFile_copy.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], False),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; return bSuccess, oResults.Results()
   oFile_move = CFile(sFile_move)
   dFileInfo = oFile_move.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], True),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; del oFile_move; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile_move.Append(sTestString)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; del oFile_move; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile_move.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; del oFile_move; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 3, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString),
                                (listLines[1], sTestString),
                                (listLines[2], sTestString)))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; del oFile_move; return bSuccess, oResults.Results()
   del oFile_copy
   del oFile_move
   os.remove(sFile)
   os.remove(sFile_move)
   return True, oResults.Results("PEC_0011 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0012(oConfig):
   oResults = CResult()
   sFile = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   bSuccess, sResult = oFile.Write("A B C")
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   dFileInfo = oFile.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], True),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   # delete a file with and without confirmation
   bSuccess, sResult = oFile.Delete(bConfirmDelete=True) # default
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   dFileInfo = oFile.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], False),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Delete(bConfirmDelete=True) # default
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; bSuccess=False; del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Delete(bConfirmDelete=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   del oFile
   return True, oResults.Results("PEC_0011 done")

# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------

def PEC_0050(oConfig):
   oResults = CResult()
   sFile_notexistingpath = oConfig.Get('CFILE_TESTFILE_NOTEXISTINGPATH')
   sFile_copy          = oConfig.Get('CFILE_TESTFILE_COPIED')
   sFile_move           = oConfig.Get('CFILE_TESTFILE_MOVED')
   oFile = CFile(sFile_notexistingpath)
   bSuccess, sResult = oFile.Write("A B C")
   oResults.Results(sResult)
   if bSuccess is not None: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Delete() # bConfirmDelete is True per default
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.CopyTo(sFile_copy)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.MoveTo(sFile_move)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile; return bSuccess, oResults.Results()
   del oFile
   return True, oResults.Results("PEC_0050 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0051(oConfig):
   oResults = CResult()
   sFile                 = oConfig.Get('CFILE_TESTFILE')
   sFile_notexistingpath = oConfig.Get('CFILE_TESTFILE_NOTEXISTINGPATH')
   oFile = CFile(sFile)
   bSuccess, sResult = oFile.Write("A B C")
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.CopyTo(sFile_notexistingpath)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.MoveTo(sFile_notexistingpath)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0051 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0052(oConfig):
   oResults = CResult()
   sFile                 = oConfig.Get('CFILE_TESTFILE')
   oFile = CFile(sFile)
   sTestString = "A B C"
   bSuccess, sResult = oFile.Write(sTestString)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   dFileInfo = oFile.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], True),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.CopyTo(sFile)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.MoveTo(sFile)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile; return bSuccess, oResults.Results()
   dFileInfo = oFile.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], True),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   listLines, bSuccess, sResult = oFile.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_copy; del oFile_move; return bSuccess, oResults.Results()
   del oFile
   os.remove(sFile)
   return True, oResults.Results("PEC_0052 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0053(oConfig):
   oResults = CResult()
   sFile_1 = oConfig.Get('CFILE_TESTFILE_1')
   sFile_2 = oConfig.Get('CFILE_TESTFILE_2')
   oFile_1 = CFile(sFile_1)
   oFile_2 = CFile(sFile_2)
   sTestString_1 = "A B C"
   sTestString_2 = "X Y Z"
   sTestString_3 = "D E F"
   bSuccess, sResult = oFile_1.Write(sTestString_1)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile_2.Write(sTestString_2)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile_1.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile_2.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   dFileInfo = oFile_1.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], True),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   dFileInfo = oFile_2.GetFileInfo()
   bSuccess, sResult = compare(((dFileInfo['bFileIsExisting'], True),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   del oFile_2
   # file 2 is closed, but not allowed to be overwritten
   bSuccess, sResult = oFile_1.CopyTo(sFile_2, bOverwrite=False)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile_1; return bSuccess, oResults.Results()
   # file 2 is expected to have still the same content as before
   oFile_2 = CFile(sFile_2)
   listLines, bSuccess, sResult = oFile_2.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_2),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   del oFile_2
   # file 2 is closed, and is allowed to be overwritten
   bSuccess, sResult = oFile_1.CopyTo(sFile_2, bOverwrite=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; return bSuccess, oResults.Results()
   # file 2 is expected to have the content of file 1
   oFile_2 = CFile(sFile_2)
   listLines, bSuccess, sResult = oFile_2.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_1),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   # change the content of file 1
   bSuccess, sResult = oFile_1.Append(sTestString_3)
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   # check the new content of file 1
   listLines, bSuccess, sResult = oFile_1.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 2, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_1),
                                (listLines[1], sTestString_3)))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   # try to copy file 1 to file 2 - but file 2 is still in access
   bSuccess, sResult = oFile_1.CopyTo(sFile_2, bOverwrite=True)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   # again check the content of file 2 - must be the same as before
   listLines, bSuccess, sResult = oFile_2.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_1),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   # try to move file 1 to file 2 - but file 2 is still in access
   bSuccess, sResult = oFile_1.MoveTo(sFile_2, bOverwrite=True)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   # again check the content of file 2 - must be the same as before
   listLines, bSuccess, sResult = oFile_2.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 1, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_1),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   # and also file 1 must still exist with the same content as before
   listLines, bSuccess, sResult = oFile_1.ReadLines()
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listLines), 2, "number of lines"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listLines[0], sTestString_1),
                                (listLines[1], sTestString_3)))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
   del oFile_1
   del oFile_2
   # two instances with the same file (not allowed)
   bException = False
   oFile_1_a = None
   try:
      oFile_1_a = CFile(sFile_1)
   except:
      bException = True
   bSuccess, sResult = compare(((bException, False, "access violation"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1_a; return bSuccess, oResults.Results()
   bException = False
   oFile_1_b = None
   try:
      oFile_1_b = CFile(sFile_1)
   except:
      bException = True
   bSuccess, sResult = compare(((bException, True, "access violation"),))
   oResults.Results(sResult)
   if bSuccess is not True: del oFile_1_a; del oFile_1_b; return bSuccess, oResults.Results()
   del oFile_1_a
   del oFile_1_b
   os.remove(sFile_1)
   os.remove(sFile_2)
   return True, oResults.Results("PEC_0053 done")


# --------------------------------------------------------------------------------------------------------------
# CFolder
# --------------------------------------------------------------------------------------------------------------
#TM***

def PEC_0100(oConfig):
   oResults = CResult()
   sTestFolder = oConfig.Get('CFOLDER_TESTFOLDER')
   # test file for test folder
   sTestFile = f"{sTestFolder}/CFolder_TestFile.txt"

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file does not exist
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # create test file within test folder
   oTestFile = CFile(sTestFile)
   bSuccess, sResult = oTestFile.Write(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = oTestFile.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
   del oTestFile

   # expected: test file exists now
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()

   # try to create test folder again, but with bOverwrite=False (=> content will not be deleted)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=False, bRecursive=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: folder still exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file still exists
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   os.remove(sTestFile)
   shutil.rmtree(sTestFolder, ignore_errors=False)

   return True, oResults.Results("PEC_0100 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0101(oConfig):
   oResults = CResult()
   sTestFolder = oConfig.Get('CFOLDER_TESTFOLDER')
   # test file for test folder
   sTestFile = f"{sTestFolder}/CFolder_TestFile.txt"

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file does not exist
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # create test file within test folder
   oTestFile = CFile(sTestFile)
   bSuccess, sResult = oTestFile.Write(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = oTestFile.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
   del oTestFile

   # expected: test file exists now
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # try to create test folder again, but with bOverwrite=True (=> content will be deleted)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: folder still exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file does not exist an more
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   shutil.rmtree(sTestFolder, ignore_errors=False)

   return True, oResults.Results("PEC_0101 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0102(oConfig):
   oResults = CResult()
   sTestFolder = oConfig.Get('CFOLDER_TESTSUBFOLDERS')
   sFolder_tobedeletedfinally = oConfig.Get('CFOLDER_TESTSUBFOLDER_CFO')
   # test file for test folder
   sTestFile = f"{sTestFolder}/CFolder_TestFile.txt"

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file does not exist
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # create test file within test folder
   oTestFile = CFile(sTestFile)
   bSuccess, sResult = oTestFile.Write(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = oTestFile.Close()
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
   del oTestFile

   # expected: test file exists
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # try to create test folder again, with bOverwrite=False (=> content will not be deleted)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=False, bRecursive=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: folder still exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file still exists
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # delete test folder
   bSuccess, sResult = oTestFolder.Delete(bConfirmDelete=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file does not exist any more
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: test folder does not exist any more
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: parent folder exists
   sParentFolder = os.path.dirname(sTestFolder)
   bSuccess, sResult = is_folder(sParentFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # try to delete test folder again; but folder does not exist any more;
   # because of a confirmation is requested, Delete() returns an error
   bSuccess, sResult = oTestFolder.Delete(bConfirmDelete=True)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   shutil.rmtree(sFolder_tobedeletedfinally, ignore_errors=False)

   return True, oResults.Results("PEC_0102 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0103(oConfig):
   oResults = CResult()
   sTestFolder = oConfig.Get('CFOLDER_TESTFOLDER')

   sSubFolder_1 = f"{sTestFolder}/sub1"
   sSubFolder_2 = f"{sTestFolder}/sub2"
   sTestFile_1  = f"{sSubFolder_1}/TestFile_1.txt"
   sTestFile_2  = f"{sSubFolder_2}/TestFile_2.txt"

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: sub folders do not exist
   bSuccess, sResult = is_folder(sSubFolder_1)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_folder(sSubFolder_2)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # creation of sub folders
   oSubFolder_1 = CFolder(sSubFolder_1)
   bSuccess, sResult = oSubFolder_1.Create()
   del oSubFolder_1
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_folder(sSubFolder_1)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   oSubFolder_2 = CFolder(sSubFolder_2)
   bSuccess, sResult = oSubFolder_2.Create()
   del oSubFolder_2
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_folder(sSubFolder_2)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # creation of test files in sub folders
   oTestFile_1 = CFile(sTestFile_1)
   bSuccess, sResult = oTestFile_1.Write(sTestFile_1)
   del oTestFile_1
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_file(sTestFile_1)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   oTestFile_2 = CFile(sTestFile_2)
   bSuccess, sResult = oTestFile_2.Write(sTestFile_2)
   del oTestFile_2
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_file(sTestFile_2)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # make test files write protected
   os.chmod(sTestFile_1, stat.S_IREAD)
   os.chmod(sTestFile_2, stat.S_IREAD)

   # delete entire test folder (including write protected files; the write protection will be removed by Delete())
   bSuccess, sResult = oTestFolder.Delete(bConfirmDelete=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # check outcome (expected: subfolders and files within subfolders deleted)
   bSuccess, sResult = is_file(sTestFile_1)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_file(sTestFile_2)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_folder(sSubFolder_1)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_folder(sSubFolder_2)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # and some further tries (try to delete what does not exist)
   bSuccess, sResult = oTestFolder.Delete(bConfirmDelete=True)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = oTestFolder.Delete(bConfirmDelete=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder

   return True, oResults.Results("PEC_0103 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0104(oConfig):
   oResults = CResult()
   sTestFolder        = oConfig.Get('CFOLDER_TESTFOLDER')
   sDestFolder        = oConfig.Get('CFOLDER_COPY')
   sFolder_expected   = oConfig.Get('CFOLDER_COPY_TESTFOLDER')
   sTestFile          = f"{sTestFolder}/CFolder_TestFile.txt"
   sTestFile_expected = f"{sFolder_expected}/CFolder_TestFile.txt"

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # initial destination folder creation with bOverwrite=True
   oDestFolder = CFolder(sDestFolder)
   bSuccess, sResult = oDestFolder.Create(bOverwrite=True, bRecursive=True)
   del oDestFolder
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sDestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # create test file within test folder
   oTestFile = CFile(sTestFile)
   bSuccess, sResult = oTestFile.Write(sTestFile)
   del oTestFile
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: test file exists
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # copy the test folder
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: destination folder does exist
   bSuccess, sResult = is_folder(sFolder_expected)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: copied file within destination folder does exist
   bSuccess, sResult = is_file(sTestFile_expected)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   os.remove(sTestFile)
   os.remove(sTestFile_expected)
   shutil.rmtree(sTestFolder, ignore_errors=False)
   shutil.rmtree(sFolder_expected, ignore_errors=False)
   shutil.rmtree(sDestFolder, ignore_errors=False)

   return True, oResults.Results("PEC_0104 done")

# ----------------------------------------------------------------------------------------------------------

def PEC_0105(oConfig):
   oResults = CResult()
   sTestFolder        = oConfig.Get('CFOLDER_TESTFOLDER')
   sDestFolder        = oConfig.Get('CFOLDER_COPY')
   sFolder_expected   = oConfig.Get('CFOLDER_COPY_TESTFOLDER')
   sTestFile          = f"{sTestFolder}/CFolder_TestFile.txt"
   sTestFile_expected = f"{sFolder_expected}/CFolder_TestFile.txt"

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # initial destination folder creation with bOverwrite=True
   oDestFolder = CFolder(sDestFolder)
   bSuccess, sResult = oDestFolder.Create(bOverwrite=True, bRecursive=True)
   del oDestFolder
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sDestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResult

   # initial expected folder (the folder that is copied to the destination folder) creation with bOverwrite=True
   oFolder_expected = CFolder(sFolder_expected)
   bSuccess, sResult = oFolder_expected.Create(bOverwrite=True, bRecursive=True)
   del oFolder_expected
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sFolder_expected)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResult

   # create test file within test folder
   oTestFile = CFile(sTestFile)
   bSuccess, sResult = oTestFile.Write(sTestFile)
   del oTestFile
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: test file exists
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # copy the test folder to destination folder (with default bOverwrite=False)
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: copied folder exists within destination folder (because has already been created before)
   bSuccess, sResult = is_folder(sFolder_expected)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResult

   # expected: destination file does not exist (because nothing is copied)
   bSuccess, sResult = is_file(sTestFile_expected)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # again copy the test folder to destination folder (with bOverwrite=True)
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder, bOverwrite=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: copied folder exists within destination folder (now has been copied)
   bSuccess, sResult = is_folder(sFolder_expected)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResult

   # expected: destination file does exist now (because the folder containing the file, has been copied)
   bSuccess, sResult = is_file(sTestFile_expected)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   os.remove(sTestFile)
   os.remove(sTestFile_expected)
   shutil.rmtree(sTestFolder, ignore_errors=False)
   shutil.rmtree(sFolder_expected, ignore_errors=False)
   shutil.rmtree(sDestFolder, ignore_errors=False)

   return True, oResults.Results("PEC_0105 done")

   # --------------------------------------------------------------------------------------------------------------

def PEC_0150(oConfig):
   oResults = CResult()
   sTestFolder = oConfig.Get('CFOLDER_TESTFOLDER')
   sDestFolder = oConfig.Get('TMPFILESFOLDER')
   sTestFile   = f"{sTestFolder}/CFolder_TestFile.txt"

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # create test file within test folder
   oTestFile = CFile(sTestFile)
   bSuccess, sResult = oTestFile.Write(sTestFile)
   del oTestFile
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: test file exists
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # Copy the test folder to destination folder, with default bOverwrite=False.
   # But the outcome would be that the source path and the destination path are the same;
   # therefore CopyTo() returns an error
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: test folder still exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # again copy the test folder to destination folder, now with bOverwrite=True
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder, bOverwrite=True)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: test folder still exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file still exists
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   os.remove(sTestFile)
   shutil.rmtree(sTestFolder, ignore_errors=False)

   return True, oResults.Results("PEC_0150 done")

   # --------------------------------------------------------------------------------------------------------------

def PEC_0151(oConfig):
   oResults = CResult()
   sTestFolder             = oConfig.Get('CFOLDER_TESTFOLDER')
   sDestFolder_notexisting = oConfig.Get('CFOLDER_NOTEXISTING')
   sDestFolder_notexpected = oConfig.Get('CFOLDER_NOTEXISTING_TESTFOLDER')

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # Copy the test folder to destination folder, with default bOverwrite=False.
   # But the destination folder does not exist, therefore CopyTo() returns an error
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder_notexisting)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: destination folders do not exist
   bSuccess, sResult = is_folder(sDestFolder_notexisting)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_folder(sDestFolder_notexpected)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # Again copy the test folder to destination folder, now with bOverwrite=True.
   # But the destination folder does not exist, therefore CopyTo() returns an error
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder_notexisting, bOverwrite=True)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: destination folders do not exist
   bSuccess, sResult = is_folder(sDestFolder_notexisting)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()
   bSuccess, sResult = is_folder(sDestFolder_notexpected)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   shutil.rmtree(sTestFolder, ignore_errors=False)

   return True, oResults.Results("PEC_0151 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0152(oConfig):
   oResults = CResult()
   sTestFolder      = oConfig.Get('CFOLDER_TESTFOLDER')
   sDestFolder      = oConfig.Get('CFOLDER_COPY')
   sFolder_expected = oConfig.Get('CFOLDER_COPY_TESTFOLDER')
   sTestFile        = f"{sFolder_expected}/CFolder_TestFile.txt"

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # initial destination folder creation with bOverwrite=True
   oFolder_expected = CFolder(sFolder_expected)
   bSuccess, sResult = oFolder_expected.Create(bOverwrite=True, bRecursive=True)
   del oFolder_expected
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sFolder_expected)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResult

   # create test file within destination
   oTestFile = CFile(sTestFile)
   bSuccess, sResult = oTestFile.Write(sTestFile)
   del oTestFile
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: test file exists
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # create instance of expected folder
   oFolder_expected = CFolder(sFolder_expected)

   # Copy the test folder to destination folder, with default bOverwrite=False.
   # But the folder within the destination is already in use by oFolder_expected;
   # therefore CopyTo() returns an error
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # Again copy the test folder to destination folder, now with bOverwrite=True.
   # But the folder within the destination is still in use by oFolder_expected;
   # therefore CopyTo() returns an error
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder, bOverwrite=True)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file still exists (within destination)
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # delete instance of expected folder
   del oFolder_expected

   # Again copy the test folder to destination folder, with default bOverwrite=False.
   # The folder within the destination is not in use any more by another CFolder instance.
   # But the folder still exists and is not allowed to be overwritten;
   # therefore CopyTo() returns an error
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file still exists (within destination)
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # Again copy the test folder to destination folder, now with bOverwrite=True.
   # The folder within the destination is not in use any more by another CFolder instance.
   # The folder still exists and will be overwritten.
   # CopyTo() returns success
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder, bOverwrite=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test file does not exist any more (within destination)
   bSuccess, sResult = is_file(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   shutil.rmtree(sTestFolder, ignore_errors=False)
   shutil.rmtree(sFolder_expected, ignore_errors=False)
   shutil.rmtree(sDestFolder, ignore_errors=False)

   return True, oResults.Results("PEC_0152 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0153(oConfig):
   oResults = CResult()
   sTestFolder         = oConfig.Get('CFOLDER_TESTFOLDER')
   sDestFolder         = oConfig.Get('CFOLDER_COPY')
   sFolder_notexpected = oConfig.Get('CFOLDER_COPY_TESTFOLDER')

   # make sure that the test folder does not exist
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Delete(bConfirmDelete=False)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: test folder does not exist
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # make sure that the destination folder does not exist
   oFolder_notexpected = CFolder(sFolder_notexpected)
   bSuccess, sResult = oFolder_notexpected.Delete(bConfirmDelete=False)
   del oFolder_notexpected
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # expected: destination folder does not exist
   bSuccess, sResult = is_folder(sFolder_notexpected)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # copy the (not existing) folder
   bSuccess, sResult = oTestFolder.CopyTo(sDestFolder)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # expected: destination folder still does not exist
   bSuccess, sResult = is_folder(sFolder_notexpected)
   oResults.Results(sResult)
   if bSuccess is not False: bSuccess=False; del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   return True, oResults.Results("PEC_0153 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0154(oConfig):
   oResults = CResult()
   sTestFolder = oConfig.Get('CFOLDER_TESTFOLDER')
   # test file for test folder
   sTestFile = f"{sTestFolder}/CFolder_TestFile.txt"

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # create test file within test folder
   oTestFile = CFile(sTestFile)
   bSuccess, sResult = oTestFile.Write(sTestFile)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()

   # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
   # start: platform dependency

   sPlatformSystem = platform.system()
   if sPlatformSystem == "Windows":
      # Without 'oTestFile.Close()' or 'del oTestFile', the file handle is still open.
      # Under Windows the deletion of the folder causes an access violation and it should not be possible to delete
      # the folder.
      # A folder can be deleted explicitely: with Delete(bConfirmDelete=True).
      # A folder can also be deleted implicitely: with Create(bOverwrite=True).
      # The deletion runs in a loop. This takes some time. After an iteration counter exceeds a limit,
      # the computation stops with an error message.
      # Outcome: The folder is not deleted.
      bSuccess, sResult = oTestFolder.Delete(bConfirmDelete=True)
      oResults.Results(sResult)
      if bSuccess is not False: bSuccess=False; del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
      bSuccess, sResult = oTestFolder.Create(bOverwrite=True)
      oResults.Results(sResult)
      if bSuccess is not False: bSuccess=False; del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
      # expected: test file exists (and therefore the folder also)
      bSuccess, sResult = is_file(sTestFile)
      oResults.Results(sResult)
      if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
      # tidying up
      del oTestFile
      del oTestFolder
      os.remove(sTestFile)
      shutil.rmtree(sTestFolder, ignore_errors=False)

   elif sPlatformSystem == "Linux":
      # Without 'oTestFile.Close()' or 'del oTestFile', the file handle is still open.
      # Under Linux this doesn't matter
      # Outcome: The folder (and the file with open handle) is deleted.
      bSuccess, sResult = oTestFolder.Delete(bConfirmDelete=True)
      oResults.Results(sResult)
      if bSuccess is not True: del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
      # expected: the test folder does not exist any more
      bSuccess, sResult = is_folder(sTestFolder)
      oResults.Results(sResult)
      if bSuccess is not False: bSuccess=False; del oTestFile; del oTestFolder; return bSuccess, oResults.Results()
      # tidying up
      del oTestFile
      del oTestFolder

   else:
      # tidying up
      del oTestFile
      del oTestFolder
      os.remove(sTestFile)
      shutil.rmtree(sTestFolder, ignore_errors=False)
      bSuccess = None
      sResult  = f"Platform '{sPlatformSystem}' is not supported"
      oResults.Results(sResult)
      return bSuccess, oResults.Results()

   # end: platform dependency
   # //////////////////////////////////////////////////////////////////////////////////////////////////////////////

   # cross check (test folder should be ready to use again)
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder
   shutil.rmtree(sTestFolder, ignore_errors=False)
   return True, oResults.Results("PEC_0154 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0155(oConfig):
   oResults = CResult()
   sTestFolder = oConfig.Get('CFOLDER_TESTFOLDER')

   # initial test folder creation with bOverwrite=True
   oTestFolder = CFolder(sTestFolder)
   bSuccess, sResult = oTestFolder.Create(bOverwrite=True, bRecursive=True)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()
   # expected: folder exists
   bSuccess, sResult = is_folder(sTestFolder)
   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # further CFolder instance of same folder is expected to cause an exception
   oTestFolder_2 = None
   bSuccess = None
   sResult  = None
   try:
      oTestFolder_2 = CFolder(sTestFolder)
      bSuccess = False
      sResult  = "Missing exception in case of further CFolder instance of same folder"
   except Exception as reason:
      bSuccess = True
      sResult  = str(reason)

   del oTestFolder_2

   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder; return bSuccess, oResults.Results()

   # deletion of first CFolder instance must enable to create again an instance with same folder
   del oTestFolder

   oTestFolder_2 = None
   bSuccess = None
   sResult  = None
   try:
      oTestFolder_2 = CFolder(sTestFolder)
      bSuccess = True
      sResult  = "CFolder instance created"
   except Exception as reason:
      bSuccess = False
      sResult  = str(reason)

   oResults.Results(sResult)
   if bSuccess is not True: del oTestFolder_2; return bSuccess, oResults.Results()

   # tidying up
   del oTestFolder_2
   shutil.rmtree(sTestFolder, ignore_errors=False)
   return True, oResults.Results("PEC_0155 done")


# --------------------------------------------------------------------------------------------------------------
