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
# 07.08.2023
#
# --------------------------------------------------------------------------------------------------------------

import os, sys, platform
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
#TM***

# --------------------------------------------------------------------------------------------------------------
# CFile
# --------------------------------------------------------------------------------------------------------------

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
   if bSuccess is not False: del oFile; return bSuccess, oResults.Results()
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
   if bSuccess is not False: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.Delete() # bConfirmDelete is True per default
   oResults.Results(sResult)
   if bSuccess is not False: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.CopyTo(sFile_copy)
   oResults.Results(sResult)
   if bSuccess is not False: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.MoveTo(sFile_move)
   oResults.Results(sResult)
   if bSuccess is not False: del oFile; return bSuccess, oResults.Results()
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
   if bSuccess is not False: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.MoveTo(sFile_notexistingpath)
   oResults.Results(sResult)
   if bSuccess is not False: del oFile; return bSuccess, oResults.Results()
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
   if bSuccess is not False: del oFile; return bSuccess, oResults.Results()
   bSuccess, sResult = oFile.MoveTo(sFile)
   oResults.Results(sResult)
   if bSuccess is not False: del oFile; return bSuccess, oResults.Results()
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
   if bSuccess is not False: del oFile_1; return bSuccess, oResults.Results()
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
   if bSuccess is not False: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
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
   if bSuccess is not False: del oFile_1; del oFile_2; return bSuccess, oResults.Results()
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
