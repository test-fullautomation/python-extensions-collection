# **************************************************************************************************************
#
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
#
# **************************************************************************************************************
#
# executepytest.py
#
# XC-CT/ECA3-Queckenstedt
#
# Executes pytest recursively in current folder.
# Log file can be set in command line. If not, default log is written.
#
# --------------------------------------------------------------------------------------------------------------
#
# 26.09.2022
#
# --------------------------------------------------------------------------------------------------------------

import os, sys, platform, shlex, subprocess, shutil, argparse

import colorama as col

from PythonExtensionsCollection.String.CString import CString
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

def printexception(sMsg):
    sys.stderr.write(COLBR + f"Exception: {sMsg}!\n")

# --------------------------------------------------------------------------------------------------------------

# -- some informations about the environment of this script

sThisScript     = sys.argv[0]
sThisScript     = CString.NormalizePath(sThisScript)
sThisScriptPath = os.path.dirname(sThisScript)
sThisScriptName = os.path.basename(sThisScript)

sOSName         = os.name
sPlatformSystem = platform.system()
sPythonPath     = CString.NormalizePath(os.path.dirname(sys.executable))
sPython         = CString.NormalizePath(sys.executable)
sPythonVersion  = sys.version

sFilter = None
if sPlatformSystem == "Windows":
    sFilter = "not _Linux_"
elif sPlatformSystem == "Linux":
    sFilter = "not _Windows_"
else:
   bSuccess = False
   sResult  = f"Operating system {sPlatformSystem} ({sOSName}) not supported"
   printerror(CString.FormatResult(sThisScriptName, bSuccess, sResult))
   sys.exit(ERROR)

print()
print(f"{sThisScriptName} is running under {sPlatformSystem} ({sOSName})")
print()

# -- parse the command line of this script (optional path and name of pytest xml log file)

oCmdLineParser = argparse.ArgumentParser()
oCmdLineParser.add_argument('--logfile', type=str, help='Path and name of XML log file.')
oCmdLineArgs = oCmdLineParser.parse_args()
sLogFile = None
if oCmdLineArgs.logfile is not None:
   sLogFile = CString.NormalizePath(oCmdLineArgs.logfile, sReferencePathAbs=sThisScriptPath)
else:
   sLogFile = f"{sThisScriptPath}/logfiles/PyTestLog.xml"

# -- create the log file folder

sLogFilesPath = os.path.dirname(sLogFile)
oLogFilesPath = CFolder(sLogFilesPath)
bSuccess, sResult = oLogFilesPath.Create(bOverwrite=False, bRecursive=True)
del oLogFilesPath
if bSuccess is not True:
   printerror(CString.FormatResult(sThisScriptName, bSuccess, sResult))
   sys.exit(ERROR)
print(sResult)
print()

# -- prepare the command line for the test execution

listCmdLineParts = []
listCmdLineParts.append(f"\"{sPython}\"")
listCmdLineParts.append("-m pytest")
if sFilter is not None:
   listCmdLineParts.append(f"-k \"{sFilter}\"")
listCmdLineParts.append("--show-capture=all")
listCmdLineParts.append(f"--junitxml=\"{sLogFile}\"")
listCmdLineParts.append(f"\"{sThisScriptPath}\"")
sCmdLine = " ".join(listCmdLineParts)
del listCmdLineParts

# -- execute the tests

listCmdLineParts = shlex.split(sCmdLine)
sCmdLine = " ".join(listCmdLineParts)
print(f"Now executing command line:\n{sCmdLine}")
print()
nReturn = ERROR
try:
   nReturn = subprocess.call(listCmdLineParts)
   print(f"[{sThisScriptName}] : Subprocess returned {nReturn}")
except Exception as ex:
   print()
   printexception(str(ex))
   print()
   sys.exit(ERROR)
print()
if nReturn != SUCCESS:
   printerror(f"Subprocess has not returned expected value {SUCCESS}")
   print()
else:
   print(f"Test results in '{sLogFile}'")
   print()

print(COLBG + f"{sThisScriptName} done")
print()

sys.exit(nReturn)

