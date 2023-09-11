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
# component_test.py
#
# XC-CT/ECA3-Queckenstedt
#
# --------------------------------------------------------------------------------------------------------------
#
VERSION      = "0.7.0"
VERSION_DATE = "08.09.2023"
#
# --------------------------------------------------------------------------------------------------------------
#
# This self test is partially contradictory. The system under test is the PythonExtensionCollection.
# But additionally to this the PythonExtensionCollection is also used in code, that executes the test.
# Therefore we have no strict separation of test and system under test. This should not happen and
# I tried to avoid this as much as possible. But it's not avoided completely.
#
# To avoid to use some PythonExtensionCollection functions also within this test, would cause additional effort.
# Parts of the code are taken over from other applications (reuse). I do not want to rework all, only to
# separate the test from the system under test completely.
#
# The paradigm is: The entire code must work! Independent from the position (test or system under test).
# The test must fit to the system under test. In case of any errors, they will be detected, no matter if the
# error occurs in the system under test or in the test itself.
#
# But this belongs only to a few functions, not to all functions available in the PythonExtensionCollection.
# --------------------------------------------------------------------------------------------------------------

#TM***
# TOC:
# [TESTCONFIG]
# [PRELIMINARIES]
# [CODEDUMP]
# [EXECUTION]
# --------------------------------------------------------------------------------------------------------------

import os, sys, shlex, subprocess, ctypes, time
import colorama as col
import pprint

from PythonExtensionsCollection.String.CString import CString
from PythonExtensionsCollection.Folder.CFolder import CFolder
from PythonExtensionsCollection.File.CFile import CFile
from PythonExtensionsCollection.Utils.CUtils import *

from PythonExtensionsCollection.version import VERSION as SUT_VERSION
from PythonExtensionsCollection.version import VERSION_DATE as SUT_VERSION_DATE

from libs.CConfig import CConfig
from libs.CCodePatterns import CCodePatterns
from libs.CGenCode import CGenCode

from tests.testfunctions import *
from tests.testconfig import *

col.init(autoreset=True)

COLBR = col.Style.BRIGHT + col.Fore.RED
COLBY = col.Style.BRIGHT + col.Fore.YELLOW
COLBG = col.Style.BRIGHT + col.Fore.GREEN
COLBB = col.Style.BRIGHT + col.Fore.BLUE

SUCCESS = 0
ERROR   = 1

# --------------------------------------------------------------------------------------------------------------

def printerror(sMsg, prefix=None):
   if prefix is None:
      sError = COLBR + f"{sMsg}\n\n"
   else:
      sError = COLBR + f"{prefix}:\n{sMsg}\n\n"
   sys.stderr.write(sError)

def printunknown(sMsg, prefix=None):
   if prefix is None:
      sUnknown = COLBB + f"{sMsg}\n\n"
   else:
      sUnknown = COLBB + f"{prefix}:\n{sMsg}\n\n"
   sys.stderr.write(sUnknown)

# --------------------------------------------------------------------------------------------------------------
# [TESTCONFIG]
# --------------------------------------------------------------------------------------------------------------
# [TESTCONFIG]

# -- initialize and dump test configuration

oConfig = None
try:
   oConfig = CConfig(os.path.abspath(__file__))
except Exception as ex:
   print()
   printerror(CString.FormatResult("(main)", None, str(ex)))
   print()
   sys.exit(ERROR)

# update version and date of this app
oConfig.Set("VERSION", VERSION)
oConfig.Set("VERSION_DATE", VERSION_DATE)
THISSCRIPTNAME = oConfig.Get('THISSCRIPTNAME')
THISSCRIPTFULLNAME = f"{THISSCRIPTNAME} v. {VERSION} / {VERSION_DATE}"
oConfig.Set("THISSCRIPTFULLNAME", THISSCRIPTFULLNAME)

# add information about system under test
SUT_FULL_NAME = f"PythonExtensionsCollection v. {SUT_VERSION} / {SUT_VERSION_DATE}"
oConfig.Set("SUT_FULL_NAME", SUT_FULL_NAME)

# dump configuration values to screen
listConfigLines = oConfig.DumpConfig()

CONFIGDUMP = oConfig.Get('CONFIGDUMP')
if CONFIGDUMP is True:
   # if that's all, we have nothing more to do
   sys.exit(SUCCESS)


# --------------------------------------------------------------------------------------------------------------
# [PRELIMINARIES]
# --------------------------------------------------------------------------------------------------------------
#TM***

# -- access to configuration

THISSCRIPTNAME  = oConfig.Get('THISSCRIPTNAME')
SELFTESTLOGFILE = oConfig.Get('SELFTESTLOGFILE')

# -- start logging
oSelfTestLogFile = CFile(SELFTESTLOGFILE)
NOW = time.strftime('%d.%m.%Y - %H:%M:%S')
oSelfTestLogFile.Write(f"{THISSCRIPTNAME} started at: {NOW}\n")
oSelfTestLogFile.Write(listConfigLines) # from DumpConfig() called above
oSelfTestLogFile.Write()

# -- prepare TESTIDs

# ('listofdictUsecases' is imported directly from test/testconfig/testconfig.py)

TESTID = oConfig.Get('TESTID')

if TESTID is not None:
   listTESTIDs = TESTID.split(';')
   listofdictUsecasesSubset = []
   for sTESTID in listTESTIDs:
      sTESTID = sTESTID.strip()
      for dictUsecase in listofdictUsecases:
         if sTESTID == dictUsecase['TESTID']:
            listofdictUsecasesSubset.append(dictUsecase)
   # eof for sTESTID in listTESTIDs:
   if len(listofdictUsecasesSubset) == 0:
      bSuccess = False
      sResult  = f"Test ID '{TESTID}' not defined"
      sResult  = CString.FormatResult(THISSCRIPTNAME, bSuccess, sResult)
      print()
      printerror(sResult)
      print()
      printerror(sResult)
      oSelfTestLogFile.Write(sResult, 1)
      del oSelfTestLogFile
      sys.exit(ERROR)
   del listofdictUsecases
   listofdictUsecases = listofdictUsecasesSubset
# eof if TESTID is not None:

# --------------------------------------------------------------------------------------------------------------

# -- check for duplicate test IDs
# Test IDs are used to identify and select test cases. They have to be unique.

listIDs = []
listDuplicates = []
for dictUsecase in listofdictUsecases:
   TESTID = dictUsecase['TESTID']
   if TESTID in listIDs:
      listDuplicates.append(TESTID)
   else:
      listIDs.append(TESTID)
# eof for dictUsecase in listofdictUsecases:
if len(listDuplicates) > 0:
   sDuplicates = "[" + ", ".join(listDuplicates) + "]"
   bSuccess = False
   sResult  = f"Duplicate test IDs found in test configuration: {sDuplicates}\nTest IDs are used to identify and select test cases. They have to be unique"
   sResult  = CString.FormatResult(THISSCRIPTNAME, bSuccess, sResult)
   print()
   printerror(sResult)
   print()
   oSelfTestLogFile.Write(sResult, 1)
   del oSelfTestLogFile
   sys.exit(ERROR)


# --------------------------------------------------------------------------------------------------------------
# [CODEDUMP]
# special function (with premature end of execution = no test execution)
# --------------------------------------------------------------------------------------------------------------
#TM***

CODEDUMP = oConfig.Get('CODEDUMP')
if CODEDUMP is True:
   oCodeGenerator = None
   try:
      oCodeGenerator = CGenCode(oConfig)
   except Exception as ex:
      bSuccess = None
      sResult  = str(ex)
      sResult  = CString.FormatResult(THISSCRIPTNAME, bSuccess, sResult)
      print()
      printerror(sResult)
      print()
      oSelfTestLogFile.Write(sResult, 1)
      del oSelfTestLogFile
      sys.exit(ERROR)

   bSuccess, sResult = oCodeGenerator.GenCode()
   if bSuccess is not True:
      sResult = CString.FormatResult(THISSCRIPTNAME, bSuccess, sResult)
      print()
      printerror(sResult)
      print()
      oSelfTestLogFile.Write(sResult, 1)
      del oSelfTestLogFile
      sys.exit(ERROR)

   print(COLBG + f"{sResult}\n")

   # after code dump nothing more to do here
   sys.exit(SUCCESS)


# --------------------------------------------------------------------------------------------------------------
# [EXECUTION]
# --------------------------------------------------------------------------------------------------------------
#TM***

print("Executing test cases")
print()

nNrOfUsecases = len(listofdictUsecases)

# -- initialize test conter
nCntUsecases        = 0
nCntPassedUsecases  = 0
nCntFailedUsecases  = 0
nCntUnknownUsecases = 0

listTestsNotPassed = []

for dictUsecase in listofdictUsecases:

   # debug
   # PrettyPrint(dictUsecase, sPrefix="dictUsecase")
   # print()

   nCntUsecases = nCntUsecases + 1

   # get required parameters
   TESTID            = dictUsecase['TESTID']
   DESCRIPTION       = dictUsecase['DESCRIPTION']
   EXPECTATION       = dictUsecase['EXPECTATION']
   SECTION           = dictUsecase['SECTION']
   SUBSECTION        = dictUsecase['SUBSECTION']

   # get optional parameters
   HINT = None
   if "HINT" in dictUsecase:
      HINT = dictUsecase['HINT']
   COMMENT = None
   if "COMMENT" in dictUsecase:
      COMMENT = dictUsecase['COMMENT']

   # get derived parameters
   TESTFULLNAME = f"{TESTID}-({SECTION})-[{SUBSECTION}]"

   sOut = f"====== [START OF TEST] : '{TESTFULLNAME}' / ({nCntUsecases}/{nNrOfUsecases})"
   print(COLBY + sOut)
   print()
   oSelfTestLogFile.Write(122*"-", 1)
   oSelfTestLogFile.Write(sOut, 1)
   sOut = f"[DESCRIPTION] : {DESCRIPTION}"
   print(COLBY + sOut)
   oSelfTestLogFile.Write(sOut)
   sOut = f"[EXPECTATION] : {EXPECTATION}"
   print(COLBY + sOut)
   oSelfTestLogFile.Write(sOut)
   if COMMENT is not None:
      sOut = f"    [COMMENT] : {COMMENT}"
      print(COLBY + sOut)
      oSelfTestLogFile.Write(sOut)
   if HINT is not None:
      sOut = f"       [HINT] : {HINT}"
      print(COLBY + sOut)
      oSelfTestLogFile.Write(sOut)
   print()
   oSelfTestLogFile.Write()

   # -- execute test function
   sTestFunction = TESTID # same name for both!
   sExec = f"bSuccess, sResult = {sTestFunction}(oConfig)"
   bSuccess = None
   sResult  = None
   try:
      exec(sExec)
   except Exception as ex:
      bSuccess = None
      sResult  = str(ex)
      sResult  = CString.FormatResult(THISSCRIPTNAME, bSuccess, sResult)
      print()
      printerror(sResult)
      print()
      oSelfTestLogFile.Write(sResult, 1)

   # --------------------------------------------------------------------------------------------------------------
   # # debug
   # print()
   # print(f"============== (exec) bSuccess: {bSuccess}")
   # print(f"============== (exec) sResult : {sResult}")
   # print()
   #
   # TODO: if bDebug:
   # oSelfTestLogFile.Write(100*"-")
   oSelfTestLogFile.Write("Testflow:", 1)
   oSelfTestLogFile.Write(sResult, 1)
   # oSelfTestLogFile.Write(100*"-", 1)
   # --------------------------------------------------------------------------------------------------------------

   if bSuccess is True:
      nCntPassedUsecases = nCntPassedUsecases + 1
      sOut = f"    Test '{TESTFULLNAME}' PASSED"
      print(COLBG + sOut)
      print()
      oSelfTestLogFile.Write(sOut)
      oSelfTestLogFile.Write()
   elif bSuccess is False:
      listTestsNotPassed.append(TESTFULLNAME)
      nCntFailedUsecases = nCntFailedUsecases + 1
      print()
      printerror(f"Error: {sResult}")
      print()
      printerror(f"Test '{TESTFULLNAME}' FAILED\n")
      print()
      oSelfTestLogFile.Write(f"\nError: {sResult}\n\n" + f"    Test '{TESTFULLNAME}' FAILED", 1)
   else:
      listTestsNotPassed.append(TESTFULLNAME)
      nCntUnknownUsecases = nCntUnknownUsecases + 1
      print()
      printerror(f"Error: {sResult}")
      print()
      printunknown(f"Test '{TESTFULLNAME}' UNKNOWN\n")
      print()
      oSelfTestLogFile.Write(f"\nInternal error: {sResult}\n\n" + f"    Test '{TESTFULLNAME}' UNKNOWN", 1)

# eof for dictUsecase in listofdictUsecases:

del listofdictUsecases

# --------------------------------------------------------------------------------------------------------------
# paranoia check
if ( (nCntPassedUsecases + nCntFailedUsecases + nCntUnknownUsecases != nCntUsecases) or (nNrOfUsecases != nCntUsecases) ):
   oSelfTestLogFile.Write(122*"-", 1)
   print()
   sOut = CString.FormatResult(THISSCRIPTNAME, bSuccess=None, sResult="Internal counter mismatch")
   printunknown(sOut)
   oSelfTestLogFile.Write(sOut)
   sOut = f"Defined  : {nNrOfUsecases}"
   printunknown(sOut)
   oSelfTestLogFile.Write(sOut)
   sOut = f"Executed : {nCntUsecases}"
   printunknown(sOut)
   oSelfTestLogFile.Write(sOut)
   sOut = f"PASSED   : {nCntPassedUsecases}"
   printunknown(sOut)
   oSelfTestLogFile.Write(sOut)
   sOut = f"FAILED   : {nCntFailedUsecases}"
   printunknown(sOut)
   oSelfTestLogFile.Write(sOut)
   sOut = f"UNKNOWN  : {nCntUnknownUsecases}"
   printunknown(sOut)
   oSelfTestLogFile.Write(sOut, 1)
   print()
   sOut = f"Component test UNKNOWN"
   oSelfTestLogFile.Write(sOut, 1)
   printunknown(sOut)
   del oSelfTestLogFile
   sys.exit(ERROR)

# --------------------------------------------------------------------------------------------------------------

# -- component test result (over all test cases)

oSelfTestLogFile.Write(122*"-", 1)

if len(listTestsNotPassed) > 0:
   # print()
   sOut = "Tests that are not PASSED:"
   oSelfTestLogFile.Write(sOut + "\n")
   print(COLBY + sOut)
   print()
   for sTest in listTestsNotPassed:
      sOut = f"- {sTest}"
      oSelfTestLogFile.Write(sOut)
      print(sOut)
   oSelfTestLogFile.Write()
   print()

nReturn = ERROR

if nCntUsecases == 0:
   sOut = "Nothing executed - but why?" # should not happen
   oSelfTestLogFile.Write(sOut, 1)
   printerror(fsOut)
   nReturn = ERROR
elif ( (nCntFailedUsecases == 0) and (nCntUnknownUsecases == 0) ):
   sOut = f"Component test PASSED"
   oSelfTestLogFile.Write(sOut, 1)
   print(COLBG + sOut)
   print()
   nReturn = SUCCESS
else:
   sOut = f"Component test FAILED"
   oSelfTestLogFile.Write(sOut, 1)
   printerror(sOut)
   nReturn = ERROR

sOut = f"Defined : {nNrOfUsecases}"
print(COLBY + sOut)
oSelfTestLogFile.Write(sOut)
sOut = f"PASSED  : {nCntPassedUsecases}"
print(COLBY + sOut)
oSelfTestLogFile.Write(sOut)
sOut = f"FAILED  : {nCntFailedUsecases}"
print(COLBY + sOut)
oSelfTestLogFile.Write(sOut)
sOut = f"UNKNOWN : {nCntUnknownUsecases}"
print(COLBY + sOut)
oSelfTestLogFile.Write(sOut)

print()

del oSelfTestLogFile

sys.exit(nReturn)

# --------------------------------------------------------------------------------------------------------------

