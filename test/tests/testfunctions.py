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
# 08.09.2023
#
# --------------------------------------------------------------------------------------------------------------
#
# Some test variables depend on the operating system. If the test runs on a operating system, that is not supported,
# these variables are not defined! This will cause an expection. This exception will be catched (component_test.py)
# and the result of the corresponding test case will be UNKNOWN. Because of an error handling is guaranteed and
# to keep this code short, those variables are not initialized! These variables are also used to compare
# received against expected values. If they would have the same initial value, the result of the test case would
# be PASSED by mistake (instead opf UNKNOWN).
#
# --------------------------------------------------------------------------------------------------------------

import os, sys, platform, stat, shutil
from dotdict import dotdict
import colorama as col

from PythonExtensionsCollection.String.CString import CString
from PythonExtensionsCollection.File.CFile import CFile
from PythonExtensionsCollection.Folder.CFolder import CFolder
from PythonExtensionsCollection.Comparison.CComparison import CComparison

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

def compare(valuepairs = (), prefix=None, bInverse=False):
   # 'valuepairs' expected to be a tuple of tuples of 2 elements: received value and expected value
   bSuccess = True
   sResult  = "valid"
   listDeviations = []
   for tupleValues in valuepairs:
      if len(tupleValues) == 2:
         sReceived = f"{tupleValues[0]}"
         sExpected = f"{tupleValues[1]}"
         if bInverse is False:
            if sReceived != sExpected:
               sDeviation = f"Expected: '{sExpected}', but received: '{sReceived}'."
               listDeviations.append(sDeviation)
         elif bInverse is True:
            if sReceived == sExpected:
               sDeviation = f"Received what is not expected: '{sReceived}'."
               listDeviations.append(sDeviation)
         else:
            bSuccess = None
            sResult  = f"Invalid value '{bInverse}' for bInverse"
            return bSuccess, sResult

      elif len(tupleValues) == 3:
         sReceived = f"{tupleValues[0]}"
         sExpected = f"{tupleValues[1]}"
         sLabel    = f"{tupleValues[2]}"
         if bInverse is False:
            if sReceived != sExpected:
               sDeviation = f"Expected: '{sExpected}', but received: '{sReceived}' ({sLabel})."
               listDeviations.append(sDeviation)
         elif bInverse is True:
            if sReceived == sExpected:
               sDeviation = f"Received what is not expected: '{sReceived}' ({sLabel})."
               listDeviations.append(sDeviation)
         else:
            bSuccess = None
            sResult  = f"Invalid value '{bInverse}' for bInverse"
            return bSuccess, sResult

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
# eof def compare(valuepairs = (), prefix=None):

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
# CString / NormalizePath
# --------------------------------------------------------------------------------------------------------------
#TM***

def PEC_0200(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"%TMP%"
   elif platform.system() == "Linux":
      sIn  = r"${HOME}"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sIn, sOut),), bInverse=True)
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   return True, oResults.Results("PEC_0200 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0201(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"%TMP%"
   elif platform.system() == "Linux":
      sIn  = r"${HOME}"
   sOut = CString.NormalizePath(sIn, bExpandEnvVars=False)
   bSuccess, sResult = compare(((sIn, sOut),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   return True, oResults.Results("PEC_0201 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0202(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"C:\dir\subdir\subsubdir"
      sExp = r"C:/dir/subdir/subsubdir"
   elif platform.system() == "Linux":
      sIn  = r"/tmp\dir\subdir\subsubdir"
      sExp = r"/tmp/dir/subdir/subsubdir"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   return True, oResults.Results("PEC_0202 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0203(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r'  "  C:\dir\subdir\subsubdir  "  '
      sExp = r"C:/dir/subdir/subsubdir"
   elif platform.system() == "Linux":
      sIn  = r'  " /tmp\dir\subdir\subsubdir  "  '
      sExp = r"/tmp/dir/subdir/subsubdir"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   if platform.system() == "Windows":
      sIn  = r"  '  C:\dir\subdir\subsubdir  '  "
      sExp = r"C:/dir/subdir/subsubdir"
   elif platform.system() == "Linux":
      sIn  = r"  '  /tmp\dir\subdir\subsubdir  '  "
      sExp = r"/tmp/dir/subdir/subsubdir"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0203 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0204(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"C:\dir\\subdir//subsubdir"
      sExp = r"C:/dir/subdir/subsubdir"
   elif platform.system() == "Linux":
      sIn  = r"/tmp\dir\\subdir//subsubdir"
      sExp = r"/tmp/dir/subdir/subsubdir"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0204 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0205(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"C:\dir\\subdir//subsubdir"
      sExp = r"C:\\dir\\subdir\\subsubdir"
   elif platform.system() == "Linux":
      sIn  = r"/tmp\dir\\subdir//subsubdir"
      sExp = r"\\tmp\\dir\\subdir\\subsubdir" # this makes no sense, but nevertheless let's do something under Linux also
   sOut = CString.NormalizePath(sIn, bWin=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0205 done")

   # --------------------------------------------------------------------------------------------------------------

def PEC_0206(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"C:\dir1\..\\dir2"
      sExp = r"C:/dir2"
   elif platform.system() == "Linux":
      sIn  = r"/tmp/dir1\..\\dir2"
      sExp = r"/tmp/dir2"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0206 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0207(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"C:\dir/../dir\\subdir"
      sExp = r"C:\\dir\\subdir"
   elif platform.system() == "Linux":
      sIn  = r"/tmp\dir/../dir\\subdir"
      sExp = r"\\tmp\\dir\\subdir" # this makes no sense, but nevertheless let's do something under Linux also
   sOut = CString.NormalizePath(sIn, bWin=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0207 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0208(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"C:\dir/../dir\\subdir"
      sExp = r"C:\dir\subdir"
   elif platform.system() == "Linux":
      sIn  = r"/tmp\dir/../dir\\subdir"
      sExp = r"\tmp\dir\subdir" # this makes no sense, but nevertheless let's do something under Linux also
   sOut = CString.NormalizePath(sIn, bWin=True, bMask=False)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0208 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0209(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sReferencePathAbs = r"C:\test"
      sIn  = r"../test_2\\subdir"
      sExp = r"C:/test_2/subdir"
   elif platform.system() == "Linux":
      sReferencePathAbs = r"/tmp/test"
      sIn  = r"../test_2\\subdir"
      sExp = r"/tmp/test_2/subdir"
   sOut = CString.NormalizePath(sIn, sReferencePathAbs=sReferencePathAbs)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0209 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0210(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sReferencePathAbs = r"C:\test"
      sIn  = r"../test_2\\subdir"
      sExp = r"C:\\test_2\\subdir"
   elif platform.system() == "Linux":
      sReferencePathAbs = r"/tmp/test"
      sIn  = r"../test_2\\subdir"
      sExp = r"\\tmp\\test_2\\subdir" # this makes no sense, but nevertheless let's do something under Linux also
   sOut = CString.NormalizePath(sIn, bWin=True, bMask=True, sReferencePathAbs=sReferencePathAbs)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0210 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0211(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"C:\dir//../dir\\sub  dir"
      sExp = r'"C:/dir/sub  dir"'
   elif platform.system() == "Linux":
      sIn  = r"/tmp\dir//../dir\\sub  dir"
      sExp = r'"/tmp/dir/sub  dir"'
   sOut = CString.NormalizePath(sIn, bConsiderBlanks=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0211 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0212(oConfig):
   oResults = CResult()
   if platform.system() == "Windows":
      sIn  = r"C:\dir\\subdir"
      sExp = r"C:/dir/subdir"
   elif platform.system() == "Linux":
      sIn  = r"/tmp\dir\\subdir"
      sExp = r"/tmp/dir/subdir"
   sOut = CString.NormalizePath(sIn, bConsiderBlanks=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0212 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0213(oConfig):
   oResults = CResult()
   sIn  = r"//server.com\001//..\002/003\\004"
   sExp = r"//server.com/002/003/004"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"\\server.com\001//..\002/003\\004"
   sExp = r"//server.com/002/003/004"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"//server.com\001//..\002/003\\004"
   sExp = r"\\server.com\002\003\004"
   sOut = CString.NormalizePath(sIn, bWin=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"\\server.com\001//..\002/003\\004"
   sExp = r"\\server.com\002\003\004"
   sOut = CString.NormalizePath(sIn, bWin=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0213 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0214(oConfig):
   oResults = CResult()
   sIn  = r"file://///server.com\001//..\002/003\\004"
   sExp = r"file://///server.com/002/003/004"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"file://///server.com\001//..\002/003\\004"
   sExp = r"file://///server.com/002/003/004"
   sOut = CString.NormalizePath(sIn, bWin=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0214 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0215(oConfig):
   oResults = CResult()
   sIn  = r"http://server.com\001//..\002/003\\004"
   sExp = r"http://server.com/002/003/004"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"http:\\server.com\001//..\002/003\\004"
   sExp = r"http://server.com/002/003/004"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"https://server.com\001//..\002/003\\004"
   sExp = r"https://server.com/002/003/004"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"https:\\server.com\001//..\002/003\\004"
   sExp = r"https://server.com/002/003/004"
   sOut = CString.NormalizePath(sIn)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"http://server.com\001//..\002/003\\004"
   sExp = r"http://server.com/002/003/004"
   sOut = CString.NormalizePath(sIn, bWin=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"http:\\server.com\001//..\002/003\\004"
   sExp = r"http://server.com/002/003/004"
   sOut = CString.NormalizePath(sIn, bWin=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"https://server.com\001//..\002/003\\004"
   sExp = r"https://server.com/002/003/004"
   sOut = CString.NormalizePath(sIn, bWin=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   sIn  = r"https:\\server.com\001//..\002/003\\004"
   sExp = r"https://server.com/002/003/004"
   sOut = CString.NormalizePath(sIn, bWin=True)
   bSuccess, sResult = compare(((sOut, sExp),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0215 done")

# --------------------------------------------------------------------------------------------------------------
# CString / DetectParentPath
# --------------------------------------------------------------------------------------------------------------
#TM***

# The functionality of this method is based on the structure of the file system, on which this test is executed.
# Therefore we compute all expected return values dynamically inside every test - relative to the position of this file
# (to ensure that this test can be executed in any folder).
# But it must be possible to go 3 levels up in the file system!

def PEC_0300(oConfig):
   oResults = CResult()

   sIn_StartPath       = CString.NormalizePath(os.path.dirname(__file__))
   sExp_DestPath       = CString.NormalizePath(os.path.dirname(sIn_StartPath))
   sExp_DestPathParent = CString.NormalizePath(os.path.dirname(sExp_DestPath))
   sIn_Foldername      = os.path.basename(sExp_DestPath)
   sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername)

   bSuccess, sResult = compare(((sRet_DestPath, sExp_DestPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listRet_DestPaths), 1),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestPaths[0], sExp_DestPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestFile, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestFiles, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestPathParent, sExp_DestPathParent),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0300 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0301(oConfig):
   oResults = CResult()

   sIn_StartPath       = CString.NormalizePath(os.path.dirname(__file__))
   sParentPath         = CString.NormalizePath(os.path.dirname(sIn_StartPath))
   sIn_Foldername_1    = os.path.basename(sParentPath)
   sParentParentPath   = CString.NormalizePath(os.path.dirname(os.path.dirname(sIn_StartPath)))
   sIn_Foldername_2    = os.path.basename(sParentParentPath)
   sIn_Foldername      = f"{sIn_Foldername_1};{sIn_Foldername_2}"
   sExp_DestPathParent = sParentParentPath

   sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername)

   bSuccess, sResult = compare(((sRet_DestPath, sParentPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listRet_DestPaths), 2),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestPaths[0], sParentPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestPaths[1], sParentParentPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestFile, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestFiles, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestPathParent, sExp_DestPathParent),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0301 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0302(oConfig):
   oResults = CResult()

   sIn_StartPath     = CString.NormalizePath(os.path.dirname(__file__))
   sParentPath       = CString.NormalizePath(os.path.dirname(sIn_StartPath))
   sParentParentPath = CString.NormalizePath(os.path.dirname(sParentPath))
   sIn_Foldername_1  = "iamnotexisting"
   sIn_Foldername_2  = os.path.basename(sParentPath)
   sIn_Foldername    = f"{sIn_Foldername_1};{sIn_Foldername_2}"

   sExp_DestPathParent = sParentParentPath

   sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername)

   bSuccess, sResult = compare(((sRet_DestPath, sParentPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listRet_DestPaths), 0, "listRet_DestPaths"),), bInverse=True)
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestPaths[0], sParentPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestFile, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestFiles, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestPathParent, sExp_DestPathParent),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0302 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0303(oConfig):
   oResults = CResult()

   sIn_StartPath    = CString.NormalizePath(os.path.dirname(__file__))
   sIn_Foldername_1 = "iamnotexisting"
   sIn_Foldername_2 = "iamalsonotexisting"
   sIn_Foldername   = f"{sIn_Foldername_1};{sIn_Foldername_2}"

   sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername)

   bSuccess, sResult = compare(((sRet_DestPath, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestPaths, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestFile, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestFiles, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestPathParent, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0303 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0304(oConfig):
   oResults = CResult()

   sIn_StartPath    = CString.NormalizePath(os.path.dirname(__file__))
   sExp_DestPath       = CString.NormalizePath(os.path.dirname(sIn_StartPath))
   sExp_DestPathParent = CString.NormalizePath(os.path.dirname(sExp_DestPath))
   sIn_Foldername      = os.path.basename(sExp_DestPath)
   sIn_FileName        = "testfunctions.py"
   sExp_DestFile       = f"{sIn_StartPath}/{sIn_FileName}"

   sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername, sFileName=sIn_FileName)

   bSuccess, sResult = compare(((sRet_DestPath, sExp_DestPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listRet_DestPaths), 1),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestPaths[0], sExp_DestPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestFile, sExp_DestFile),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listRet_DestFiles), 1),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestFiles[0], sExp_DestFile),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestPathParent, sExp_DestPathParent),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0304 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0305(oConfig):
   oResults = CResult()

   sIn_StartPath       = CString.NormalizePath(os.path.dirname(__file__))
   sExp_DestPath       = CString.NormalizePath(os.path.dirname(sIn_StartPath))
   sExp_DestPathParent = CString.NormalizePath(os.path.dirname(sExp_DestPath))
   sIn_Foldername      = os.path.basename(sExp_DestPath)
   sIn_FileName        = "IAmNotExisting.txt"

   sRet_DestPath, listRet_DestPaths, sRet_DestFile, listRet_DestFiles, sRet_DestPathParent = CString.DetectParentPath(sIn_StartPath, sIn_Foldername, sFileName=sIn_FileName)

   bSuccess, sResult = compare(((sRet_DestPath, sExp_DestPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((len(listRet_DestPaths), 1),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestPaths[0], sExp_DestPath),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestFile, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((listRet_DestFiles, None),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()
   bSuccess, sResult = compare(((sRet_DestPathParent, sExp_DestPathParent),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0305 done")

# --------------------------------------------------------------------------------------------------------------
# CString / StringFilter
# --------------------------------------------------------------------------------------------------------------
#TM***

def PEC_0400(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0400 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0401(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0401 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0402(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0402 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0403(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0403 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0404(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0404 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0405(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0405 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0406(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0406 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0407(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0407 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0408(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0408 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0409(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0409 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0410(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0410 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0411(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0411 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0412(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0412 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0413(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0413 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0414(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0414 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0415(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0415 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0416(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0416 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0417(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0417 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0418(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0418 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0419(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0419 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0420(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0420 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0421(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0421 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0422(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0422 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0423(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0423 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0424(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0424 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0425(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0425 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0426(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0426 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0427(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0427 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0428(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0428 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0429(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0429 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0430(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0430 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0431(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0431 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0432(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0432 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0433(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0433 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0434(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0434 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0435(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0435 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0436(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0436 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0437(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0437 done")

# --------------------------------------------------------------------------------------------------------------

def PEC_0438(oConfig):
   oResults = CResult()

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

   bSuccess, sResult = compare(((bAck, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0438 done")

# --------------------------------------------------------------------------------------------------------------
# CString / FormatResult
# --------------------------------------------------------------------------------------------------------------
#TM***

def PEC_0500(oConfig):
   oResults = CResult()
   sResult = CString.FormatResult(sMethod="Method",
                                  bSuccess=True,
                                  sResult="Result")
   bSuccess, sResult = compare(((sResult, "[Method] : Result"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0500 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0501(oConfig):
   oResults = CResult()
   sResult = CString.FormatResult(sMethod="",
                                  bSuccess=True,
                                  sResult="Result")
   bSuccess, sResult = compare(((sResult, "Result"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0501 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0502(oConfig):
   oResults = CResult()
   sResult = CString.FormatResult(sMethod="Method",
                                  bSuccess=False,
                                  sResult="Result")
   bSuccess, sResult = compare(((sResult, "!!! ERROR !!!\n[Method] : Result"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0502 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0503(oConfig):
   oResults = CResult()
   sResult = CString.FormatResult(sMethod="",
                                  bSuccess=False,
                                  sResult="Result")
   bSuccess, sResult = compare(((sResult, "!!! ERROR !!!\nResult"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0503 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0504(oConfig):
   oResults = CResult()
   sResult = CString.FormatResult(sMethod="Method",
                                  bSuccess=None,
                                  sResult="Result")
   bSuccess, sResult = compare(((sResult, "!!! EXCEPTION !!!\n[Method] : Result"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0504 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0505(oConfig):
   oResults = CResult()
   sResult = CString.FormatResult(sMethod="",
                                  bSuccess=None,
                                  sResult="Result")
   bSuccess, sResult = compare(((sResult, "!!! EXCEPTION !!!\nResult"),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0505 done")

# --------------------------------------------------------------------------------------------------------------
# CComparison / Compare
# --------------------------------------------------------------------------------------------------------------
#TM***

# # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def PEC_0600(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/01.File_1.A.txt")
   sFile_2        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/02.File_2.A.txt")
   oResults.Results(f"Compared file 1: '{sFile_1}'")
   oResults.Results(f"Compared file 2: '{sFile_2}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")

   bSuccess, sResult = compare(((bIdentical, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   bSuccess, sResult = compare(((bSuccess, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0600 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0601(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/03.File_1.B.txt")
   sFile_2        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/04.File_2.B.txt")

   oResults.Results(f"Compared file 1: '{sFile_1}'")
   oResults.Results(f"Compared file 2: '{sFile_2}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")

   bSuccess, sResult = compare(((bIdentical, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   bSuccess, sResult = compare(((bSuccess, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0601 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0602(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/03.File_1.B.txt")
   sFile_2        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/04.File_2.B.txt")
   sPatternFile   = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/10.PatternFile.txt")

   oResults.Results(f"Compared file 1: '{sFile_1}'")
   oResults.Results(f"Compared file 2: '{sFile_2}'")
   oResults.Results(f"Pattern file   : '{sPatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")

   bSuccess, sResult = compare(((bIdentical, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   bSuccess, sResult = compare(((bSuccess, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0602 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0603(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/03.File_1.B.txt")
   sFile_2        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/05.File_2.C.txt")
   sPatternFile   = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/10.PatternFile.txt")

   oResults.Results(f"Compared file 1: '{sFile_1}'")
   oResults.Results(f"Compared file 2: '{sFile_2}'")
   oResults.Results(f"Pattern file   : '{sPatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")

   bSuccess, sResult = compare(((bIdentical, False),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   bSuccess, sResult = compare(((bSuccess, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0603 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0604(oConfig):
   oResults = CResult()

   TESTFILES_PATH     = oConfig.Get('TESTFILES_PATH')
   sFile_1            = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/07.File_1.E.txt")
   sFile_2            = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/08.File_2.E.txt")
   sPatternFile       = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/10.PatternFile.txt")
   sIgnorePatternFile = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/11.IgnorePatternFile.txt")

   oResults.Results(f"Compared file 1    : '{sFile_1}'")
   oResults.Results(f"Compared file 2    : '{sFile_2}'")
   oResults.Results(f"Pattern file       : '{sPatternFile}'")
   oResults.Results(f"Ignore pattern file: '{sIgnorePatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile, sIgnorePatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")

   bSuccess, sResult = compare(((bIdentical, True),)) # because the different lines are ignored
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   bSuccess, sResult = compare(((bSuccess, True),))
   oResults.Results(sResult)
   if bSuccess is not True: return bSuccess, oResults.Results()

   return True, oResults.Results("PEC_0604 done")
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
def PEC_0650(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/03.File_1.B.txt")
   sFile_2        = sFile_1 # same file, therefore nothing to compare
   sPatternFile   = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/10.PatternFile.txt")

   oResults.Results(f"Compared file 1    : '{sFile_1}'")
   oResults.Results(f"Compared file 2    : '{sFile_2}'")
   oResults.Results(f"Pattern file       : '{sPatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")
   oResults.Results(f"bSuccess  : {bSuccess}")

   bSuccessCompare, sResult = compare(((bIdentical, None),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   bSuccessCompare, sResult = compare(((bSuccess, False),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   return True, oResults.Results("PEC_0650 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0651(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = None
   sFile_2        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/02.File_2.A.txt")
   sPatternFile   = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/10.PatternFile.txt")

   oResults.Results(f"Compared file 1    : '{sFile_1}'")
   oResults.Results(f"Compared file 2    : '{sFile_2}'")
   oResults.Results(f"Pattern file       : '{sPatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")
   oResults.Results(f"bSuccess  : {bSuccess}")

   bSuccessCompare, sResult = compare(((bIdentical, None),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   bSuccessCompare, sResult = compare(((bSuccess, False),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   return True, oResults.Results("PEC_0651 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0652(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/01.File_1.A.txt")
   sFile_2        = None
   sPatternFile   = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/10.PatternFile.txt")

   oResults.Results(f"Compared file 1    : '{sFile_1}'")
   oResults.Results(f"Compared file 2    : '{sFile_2}'")
   oResults.Results(f"Pattern file       : '{sPatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")
   oResults.Results(f"bSuccess  : {bSuccess}")

   bSuccessCompare, sResult = compare(((bIdentical, None),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   bSuccessCompare, sResult = compare(((bSuccess, False),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   return True, oResults.Results("PEC_0652 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0653(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/IAmNotExisting.txt")
   sFile_2        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/02.File_2.A.txt")
   sPatternFile   = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/10.PatternFile.txt")

   oResults.Results(f"Compared file 1    : '{sFile_1}'")
   oResults.Results(f"Compared file 2    : '{sFile_2}'")
   oResults.Results(f"Pattern file       : '{sPatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")
   oResults.Results(f"bSuccess  : {bSuccess}")

   bSuccessCompare, sResult = compare(((bIdentical, None),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   bSuccessCompare, sResult = compare(((bSuccess, False),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   return True, oResults.Results("PEC_0653 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0654(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/01.File_1.A.txt")
   sFile_2        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/IAmNotExisting.txt")
   sPatternFile   = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/10.PatternFile.txt")

   oResults.Results(f"Compared file 1    : '{sFile_1}'")
   oResults.Results(f"Compared file 2    : '{sFile_2}'")
   oResults.Results(f"Pattern file       : '{sPatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")
   oResults.Results(f"bSuccess  : {bSuccess}")

   bSuccessCompare, sResult = compare(((bIdentical, None),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   bSuccessCompare, sResult = compare(((bSuccess, False),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   return True, oResults.Results("PEC_0654 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0655(oConfig):
   oResults = CResult()

   TESTFILES_PATH = oConfig.Get('TESTFILES_PATH')
   sFile_1        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/01.File_1.A.txt")
   sFile_2        = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/02.File_2.A.txt")
   sPatternFile   = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/IAmNotExisting.txt")

   oResults.Results(f"Compared file 1    : '{sFile_1}'")
   oResults.Results(f"Compared file 2    : '{sFile_2}'")
   oResults.Results(f"Pattern file       : '{sPatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")
   oResults.Results(f"bSuccess  : {bSuccess}")

   bSuccessCompare, sResult = compare(((bIdentical, None),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   bSuccessCompare, sResult = compare(((bSuccess, False),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   return True, oResults.Results("PEC_0655 done")
# --------------------------------------------------------------------------------------------------------------
def PEC_0656(oConfig):
   oResults = CResult()

   TESTFILES_PATH     = oConfig.Get('TESTFILES_PATH')
   sFile_1            = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/01.File_1.A.txt")
   sFile_2            = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/02.File_2.A.txt")
   sPatternFile       = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/10.PatternFile.txt")
   sIgnorePatternFile = CString.NormalizePath(f"{TESTFILES_PATH}/Comparison/IAmNotExisting.txt")

   oResults.Results(f"Compared file 1    : '{sFile_1}'")
   oResults.Results(f"Compared file 2    : '{sFile_2}'")
   oResults.Results(f"Pattern file       : '{sPatternFile}'")
   oResults.Results(f"Ignore pattern file: '{sIgnorePatternFile}'")

   oComparison = CComparison()
   bIdentical, bSuccess, sResult = oComparison.Compare(sFile_1, sFile_2, sPatternFile, sIgnorePatternFile)
   del oComparison
   oResults.Results(f"bIdentical: {bIdentical}")
   oResults.Results(f"sResult   : {sResult}")
   oResults.Results(f"bSuccess  : {bSuccess}")

   bSuccessCompare, sResult = compare(((bIdentical, None),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   bSuccessCompare, sResult = compare(((bSuccess, False),)) # because of no comparison happened
   oResults.Results(sResult)
   if bSuccessCompare is not True: return bSuccessCompare, oResults.Results()

   return True, oResults.Results("PEC_0656 done")
# --------------------------------------------------------------------------------------------------------------
