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
# CUtils.py
#
# XC-CT/ECA3-Queckenstedt
#
# 30.05.2023
#
# **************************************************************************************************************

# -- import standard Python modules
import os, sys, subprocess
from dotdict import dotdict

from PythonExtensionsCollection.String.CString import CString
from PythonExtensionsCollection.File.CFile import CFile


# **************************************************************************************************************
# wrapper
# **************************************************************************************************************

def PrettyPrint(oData=None, hOutputFile=None, bToConsole=True, nIndent=0, sPrefix=None, bHexFormat=False):
   """
Wrapper function to create and use a ``CTypePrint`` object. This wrapper function is responsible for
printing out the content to console and to a file (depending on input parameter).

The content itself is prepared by the method ``TypePrint`` of class ``CTypePrint``. This happens ``PrettyPrint`` internally.

The idea behind the ``PrettyPrint`` function is to resolve also the content of composite data types and provide for every parameter inside:

* the type
* the total number of elements inside (e.g. the number of keys inside a dictionary)
* the counter number of the current element
* the value

**Arguments:**

* ``oData``

  / *Condition*: required / *Type*: (*any Python data type*) /

  A variable of any Python data type.

* ``hOutputFile``

  / *Condition*: optional / *Type*: file handle / *Default*: None /

  If handle is not ``None`` the content is written to this file, otherwise not.

* ``bToConsole``

  / *Condition*: optional / *Type*: bool / *Default*: True /

  If ``True`` the content is written to console, otherwise not.

* ``nIndent``

  / *Condition*: optional / *Type*: int / *Default*: 0 /

  Sets the number of additional blanks at the beginning of every line of output (indentation).

* ``sPrefix``

  / *Condition*: optional / *Type*: str / *Default*: None /

  Sets a prefix string that is added at the beginning of every line of output.

* ``bHexFormat``

  / *Condition*: optional / *Type*: bool / *Default*: False /

  If ``True`` the output is printed in hexadecimal format (but valid for strings only).

**Returns:**

* ``listOutLines`` (*list*)

  / *Type*: list /

  List of lines containing the prepared output
   """

   oTypePrint   = CTypePrint()
   listOutLines = oTypePrint.TypePrint(oData, bHexFormat)

   listReturned = []
   for sLine in listOutLines:
      # if requested add indentation and prefix
      sLineOut = ""
      if sPrefix is not None:
         sLineOut = nIndent*" " + sPrefix + " " + sLine
      else:
         sLineOut = nIndent*" " + sLine
      listReturned.append(sLineOut)

      if hOutputFile is not None:
         hOutputFile.write(sLineOut + "\n")
      if bToConsole is True:
         print(sLineOut)

   return listReturned

# eof def PrettyPrint(oData=None, hOutputFile=None, bToConsole=True, nIndent=0, sPrefix=None, bHexFormat=False):

# --------------------------------------------------------------------------------------------------------------
# TM***

class CTypePrint(object):
   """
The class ``CTypePrint`` provides a method (``TypePrint``) to compute the following data:

* the type
* the total number of elements inside (e.g. the number of keys inside a dictionary)
* the counter number of the current element
* the value

of simple and composite data types.

The call of this method is encapsulated within the function ``PrettyPrint`` inside this module.
   """
   def __init__(self):
      self.listGlobalPrefixes = []
      self.listOutLines       = []

   def __del__(self):
      pass

   def _ToHex(self, sString=None):
      if ( (sString is None) or (sString == "") ):
         return sString
      listHex = []
      for sChar in sString:
         listHex.append(hex(ord(sChar)))
      sStringHex = " ".join(listHex)
      return sStringHex

   def TypePrint(self, oData=None, bHexFormat=False):
      """
The method ``TypePrint`` computes details about the input variable ``oData``.

**Arguments:**

* ``oData``

  / *Condition*: required / *Type*: any Python data type /

  Python variable of any data type.

* ``bHexFormat``

  / *Condition*: optional / *Type*: bool / *Default*: False /

  If ``True`` the output is provide in hexadecimal format.

**Returns:**

* ``listOutLines``

  / *Type*: list /

  List of lines containing the resolved content of ``oData``.
      """

      if oData is None:
         sLocalPrefix = "[NONE]"
         sGlobalPrefix = " ".join(self.listGlobalPrefixes)
         sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  " + str(oData)
         self.listOutLines.append(sOut.strip())

      elif type(oData) is int:
         sLocalPrefix = "[INT]"
         sGlobalPrefix = " ".join(self.listGlobalPrefixes)
         sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  " + str(oData)
         self.listOutLines.append(sOut.strip())

      elif type(oData) is float:
         sLocalPrefix = "[FLOAT]"
         sGlobalPrefix = " ".join(self.listGlobalPrefixes)
         sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  " + str(oData)
         self.listOutLines.append(sOut.strip())

      elif type(oData) is bool:
         sLocalPrefix = "[BOOL]"
         sGlobalPrefix = " ".join(self.listGlobalPrefixes)
         sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  " + str(oData)
         self.listOutLines.append(sOut.strip())

      elif type(oData) is str:
         sLocalPrefix = "[STR]"
         sGlobalPrefix = " ".join(self.listGlobalPrefixes)
         sData = str(oData)
         if bHexFormat is True:
            sData = self._ToHex(sData)
         sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  '" + sData + "'"
         self.listOutLines.append(sOut.strip())

      elif type(oData) is list:
         nNrOfElements = len(oData)
         if nNrOfElements == 0:
            # -- indicate empty list
            sLocalPrefix = "[LIST]"
            sGlobalPrefix = " ".join(self.listGlobalPrefixes)
            sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  []"
            self.listOutLines.append(sOut.strip())
         else:
            # -- list elements of list
            self.listGlobalPrefixes.append("[LIST]")
            nCnt = 0
            for oElement in oData:
               nCnt = nCnt + 1
               sCnt = "(" + str(nNrOfElements) + "/" + str(nCnt) + ") >"
               self.listGlobalPrefixes.append(sCnt)
               self.TypePrint(oElement, bHexFormat) # >>>> recursion
               del self.listGlobalPrefixes[-1]      # remove prefix count
            del self.listGlobalPrefixes[-1]         # remove prefix name

      elif type(oData) is tuple:
         nNrOfElements = len(oData)
         if nNrOfElements == 0:
            # -- indicate empty tuple
            sLocalPrefix = "[TUPLE]"
            sGlobalPrefix = " ".join(self.listGlobalPrefixes)
            sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  ()"
            self.listOutLines.append(sOut.strip())
         else:
            # -- list elements of tuple
            self.listGlobalPrefixes.append("[TUPLE]")
            nCnt = 0
            for oElement in oData:
               nCnt = nCnt + 1
               sCnt = "(" + str(nNrOfElements) + "/" + str(nCnt) + ") >"
               self.listGlobalPrefixes.append(sCnt)
               self.TypePrint(oElement, bHexFormat) # >>>> recursion
               del self.listGlobalPrefixes[-1]      # remove prefix count
            del self.listGlobalPrefixes[-1]         # remove prefix name

      elif type(oData) is set:
         nNrOfElements = len(oData)
         if nNrOfElements == 0:
            # -- indicate empty set
            sLocalPrefix = "[SET]"
            sGlobalPrefix = " ".join(self.listGlobalPrefixes)
            sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  ()"
            self.listOutLines.append(sOut.strip())
         else:
            # -- list elements of set
            self.listGlobalPrefixes.append("[SET]")
            nCnt = 0
            for oElement in oData:
               nCnt = nCnt + 1
               sCnt = "(" + str(nNrOfElements) + "/" + str(nCnt) + ") >"
               self.listGlobalPrefixes.append(sCnt)
               self.TypePrint(oElement, bHexFormat) # >>>> recursion
               del self.listGlobalPrefixes[-1]      # remove prefix count
            del self.listGlobalPrefixes[-1]         # remove prefix name

      elif type(oData) is dict:
         nNrOfElements = len(oData)
         if nNrOfElements == 0:
            # -- indicate empty dictionary
            sLocalPrefix = "[DICT]"
            sGlobalPrefix = " ".join(self.listGlobalPrefixes)
            sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  {}"
            self.listOutLines.append(sOut.strip())
         else:
            # -- list elements of dictionary
            self.listGlobalPrefixes.append("[DICT]")
            nCnt = 0
            listKeys = list(oData.keys())
            for sKey in listKeys:
               nCnt = nCnt + 1
               oValue = oData[sKey]
               sCntAndKey = "(" + str(nNrOfElements) + "/" + str(nCnt) + ") > {" + str(sKey) + "}"
               self.listGlobalPrefixes.append(sCntAndKey)
               self.TypePrint(oValue, bHexFormat) # >>>> recursion
               del self.listGlobalPrefixes[-1]    # remove prefix count
            del self.listGlobalPrefixes[-1]       # remove prefix name

      elif ( (type(oData) is dotdict) or (str(type(oData)) == "<class 'robot.utils.dotdict.DotDict'>") ):
         nNrOfElements = len(oData)
         if nNrOfElements == 0:
            # -- indicate empty dot dictionary
            sLocalPrefix = "[DOTDICT]"
            sGlobalPrefix = " ".join(self.listGlobalPrefixes)
            sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  {}"
            self.listOutLines.append(sOut.strip())
         else:
            # -- list elements of dot dictionary
            self.listGlobalPrefixes.append("[DOTDICT]")
            nCnt = 0
            listKeys = list(oData.keys())
            for sKey in listKeys:
               nCnt = nCnt + 1
               oValue = oData[sKey]
               sCntAndKey = "(" + str(nNrOfElements) + "/" + str(nCnt) + ") > {" + str(sKey) + "}"
               self.listGlobalPrefixes.append(sCntAndKey)
               self.TypePrint(oValue, bHexFormat) # >>>> recursion
               del self.listGlobalPrefixes[-1]    # remove prefix count
            del self.listGlobalPrefixes[-1]       # remove prefix name

      else:
         sLocalPrefix = "[" + str(type(oData)) + "]"
         sGlobalPrefix = " ".join(self.listGlobalPrefixes)
         sData = str(oData)
         if bHexFormat is True:
            sData = self._ToHex(sData)
         sOut = sGlobalPrefix + " " + sLocalPrefix + "  :  '" + sData + "'"
         self.listOutLines.append(sOut.strip())

      return self.listOutLines

   # eof def TypePrint(...):

# eof class CTypePrint():


# --------------------------------------------------------------------------------------------------------------
# TM***

class CUtils(object):
   """The class ``CUtils`` contains useful methods.
   """

   def GetInstalledPackages(sOutputFile=None):
      """The method ``GetInstalledPackages`` computes a list of all installed Python packages.
The list is returned as list of tuples containing the name and the version of the package.

It is also possible to let the method dump the list to a text file.

**Arguments:**

* ``sOutputFile``

  / *Condition*: optional / *Type*: string / *Default*: None /

  Path and name of a file to dump the package list to.

**Returns:**

* ``listofTuplesPackages``

  / *Type*: list /

  List of tuples containing the name and the version of the package.

* ``bSuccess``

  / *Type*: bool /

  Indicates if the computation of the method was successful or not.

* ``sResult``

  / *Type*: str /

  The result of the computation of the method.
      """

      sMethod  = "GetInstalledPackages"
      bSuccess = None
      sResult  = "UNKNOWN"

      listofTuplesPackages = []

      sFreezeData = None
      try:
         sFreezeData = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'], encoding="utf-8", text=True)
      except Exception as reason:
         bSuccess = None
         sResult  = str(reason)
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return listofTuplesPackages, bSuccess, sResult

      if sFreezeData is None:
         bSuccess = None
         sResult  = "sFreezeData is None"
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return listofTuplesPackages, bSuccess, sResult

      sFreezeData = str(sFreezeData) # to make the content 'split()' save

      for sPackage in sFreezeData.split():
         sName    = None
         sVersion = None
         listParts = sPackage.split('==')
         if len(listParts) != 2:
            sName    = sPackage
            sVersion = "UNKNOWN"
            # but I really would not expect this
         else:
            sName    = listParts[0]
            sVersion = listParts[1]
         listofTuplesPackages.append((sName, sVersion))
      # eof for sPackage in sFreezeData.split():

      nNrOfPackages = len(listofTuplesPackages)

      if sOutputFile is not None:
         sOutputFile = CString.NormalizePath(sOutputFile)
         sParentDirectory = os.path.dirname(sOutputFile)
         if not os.path.isdir(sParentDirectory):
            bSuccess = False
            sResult  = f"The folder to store the output file does not exist: '{sParentDirectory}'"
            return listofTuplesPackages, bSuccess, sResult

         oFile = CFile(sOutputFile)
         for tuplePackage in listofTuplesPackages:
            sName    = tuplePackage[0]
            sVersion = tuplePackage[1]
            sOut = sName.rjust(40) + " = " + sVersion
            bSuccess, sResult = oFile.Write(sOut)
         del oFile

      # eof if sOutputFile is not None:

      bSuccess = True
      sResult  = f"Identified {nNrOfPackages} packages."

      return listofTuplesPackages, bSuccess, sResult

   # eof def GetInstalledPackages(sOutputFile=None):

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   # - make the methods static

   GetInstalledPackages = staticmethod(GetInstalledPackages)

# eof class CUtils(object):

# **************************************************************************************************************

