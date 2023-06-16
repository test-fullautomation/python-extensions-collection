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
# AccessViolationTest / 26.01.2022
#
# --------------------------------------------------------------------------------------------------------------

# -- import standard Python modules
import os, sys, time, platform, shutil
from dotdict import dotdict

# -- import own Python modules (containing the code to be tested)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))) # to make sure to hit the package relative to this file at first
from PythonExtensionsCollection.File.CFile import CFile
from PythonExtensionsCollection.String.CString import CString

# --------------------------------------------------------------------------------------------------------------

print()
print(100*"*")
print("Standalone script to explore the behavior of some functions. !!! This is not a pytest !!!")
print(100*"*")
print()

# --------------------------------------------------------------------------------------------------------------

sFile_1 = None
sFile_2 = None
sPlatformSystem = platform.system()
if sPlatformSystem == "Windows":
   sFile_1 = r"%TMP%\CFile_TestFile_1.txt"
   sFile_2 = r"%TMP%\CFile_TestFile_2.txt"
elif sPlatformSystem == "Linux":
   sFile_1 = r"/tmp/CFile_TestFile_1.txt"
   sFile_2 = r"/tmp/CFile_TestFile_2.txt"

sFile_1 = CString.NormalizePath(sFile_1)
sFile_2 = CString.NormalizePath(sFile_2)

print()
print(f"* Platform : '{sPlatformSystem}'")
print(f"* File 1   : '{sFile_1}'")
print(f"* File 2   : '{sFile_2}'")
print()

# --------------------------------------------------------------------------------------------------------------
# Two instances of same file - not accepted
try:
   oFile_A = CFile(sFile_1)
except Exception as reason:
   print(str(reason))

try:
   oFile_B = CFile(sFile_1)
except Exception as reason:
   print(str(reason))

try:
   del oFile_A
   del oFile_B
except:
   pass
# --------------------------------------------------------------------------------------------------------------

oFile_1 = CFile(sFile_1)
bSuccess, sResult = oFile_1.Write("A B C")
print(f"> sResult oFile_1.Write : '{sResult}' / bSuccess : {bSuccess}")
print()

dFileInfo_1 = oFile_1.GetFileInfo()
for sKey in dFileInfo_1:
   sValue = dFileInfo_1[sKey]
   print(f"> '{sKey}' : '{sValue}'")
print()

listLines_1, bSuccess, sResult = oFile_1.ReadLines()
for sLine in listLines_1:
   print(f"* file 1 / sLine : '{sLine}'")
print()

oFile_2 = CFile(sFile_2)
bSuccess, sResult = oFile_2.Write("X Y Z")
print(f"> sResult oFile_2.Write : '{sResult}' / bSuccess : {bSuccess}")
print()

dFileInfo_2 = oFile_2.GetFileInfo()
for sKey in dFileInfo_2:
   sValue = dFileInfo_1[sKey]
   print(f"> '{sKey}' : '{sValue}'")
print()

listLines_2, bSuccess, sResult = oFile_2.ReadLines()
for sLine in listLines_2:
   print(f"* file 2 / sLine : '{sLine}'")
print()

del oFile_1
del oFile_2


# --------------------------------------------------------------------------------------------------------------

# -- manual, without CFile

hFile_1 = open(sFile_1, "w", encoding="utf-8")
hFile_1.write("A B C")
hFile_1.close()

hFile_2 = open(sFile_2, "w", encoding="utf-8")
hFile_2.write("X Y Z")
# !! we do not close !! # hFile_2.close()

try:
   shutil.copyfile(sFile_1, sFile_2)
   sResult  = f"File '{sFile_1}' copied to '{sFile_2}'."
except Exception as reason:
   sResult  = f"Exception while copying file '{sFile_1}' to '{sFile_2}'.\nReason: " + str(reason)

print(f"========== sResult : '{sResult}'")

# --------------------------------------------------------------------------------------------------------------
