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
# CComparison.py
#
# XC-CT/ECA3-Queckenstedt
#
# 08.11.2022
#
# **************************************************************************************************************

# -- import standard Python modules
import os, re

# -- import own Python modules
from PythonExtensionsCollection.File.CFile import CFile
from PythonExtensionsCollection.String.CString import CString

# **************************************************************************************************************

class CComparison(object):
   """The class ``CComparison`` contains mechanisms to compare two files either based on the original version of these files
or based on an extract (made with regular expressions) to ensure that only relevant parts of the files are compared.
   """

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   def __init__(self):
      self.__bSkipBlankLines = True
      self.__bToScreen       = False # content of files will be printed to screen (debug)
   # eof def __init__(self):

   # --------------------------------------------------------------------------------------------------------------
   #TM***

   def Compare(self, sFile_1=None, sFile_2=None, sPatternFile=None):
      """
Compares two files. While reading in all files empty lines are skipped.

**Arguments:**

* ``sFile_1``

  / *Condition*: required / *Type*: str /

  First file used for comparison.

* ``sFile_2``

  / *Condition*: required / *Type*: str /

  Second file used for comparison.

* ``sPatternFile``

  / *Condition*: optional / *Type*: str  / *Default*: None /

  Pattern file containing a set of regular expressions (line by line). The regular expressions are used to make
  an extract of both input files. In this case the extracts are compared (instead of the original file content).

**Returns:**

* ``bIdentical``

  / *Type*: bool /

  Indicates if the two input files have the same content or not.

* ``bSuccess``

  / *Type*: bool /

  Indicates if the computation of the method was successful or not.

* ``sResult``

  / *Type*: str /

  The result of the computation of the method.
      """

      sMethod = "CComparison.Compare"

      bIdentical = None
      bSuccess   = None
      sResult    = "unknown"

      if sFile_1 is None:
         bSuccess = False
         sResult  = "sFile_1 is None"
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bIdentical, bSuccess, sResult

      if sFile_2 is None:
         bSuccess = False
         sResult  = "sFile_2 is None"
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bIdentical, bSuccess, sResult

      sFile_1 = CString.NormalizePath(sFile_1)
      sFile_2 = CString.NormalizePath(sFile_2)

      if sFile_1 == sFile_2:
         bSuccess = False
         sResult  = f"Path and name of input files are the same."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bIdentical, bSuccess, sResult

      if os.path.isfile(sFile_1) is False:
         bSuccess = False
         sResult  = f"The file '{sFile_1}' does not exist"
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bIdentical, bSuccess, sResult

      if os.path.isfile(sFile_2) is False:
         bSuccess = False
         sResult  = f"The file '{sFile_2}' does not exist"
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bIdentical, bSuccess, sResult

      if sPatternFile is not None:
         # (optional)
         sPatternFile = CString.NormalizePath(sPatternFile)
         if os.path.isfile(sPatternFile) is False:
            bSuccess = False
            sResult  = f"The file '{sPatternFile}' does not exist"
            sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
            return bIdentical, bSuccess, sResult

      if self.__bToScreen is True:
         print()
         print("[FILE 1]")
      oFile_1 = CFile(sFile_1)
      listLines_1, bSuccess, sResult = oFile_1.ReadLines(bSkipBlankLines=self.__bSkipBlankLines, bLStrip=True, bRStrip=True, bToScreen=self.__bToScreen)
      del oFile_1
      if bSuccess is False:
         del listLines_1
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return bIdentical, bSuccess, sResult

      if self.__bToScreen is True:
         print()
         print("[FILE 2]")
      oFile_2 = CFile(sFile_2)
      listLines_2, bSuccess, sResult = oFile_2.ReadLines(bSkipBlankLines=self.__bSkipBlankLines, bLStrip=True, bRStrip=True, bToScreen=self.__bToScreen)
      del oFile_2
      if bSuccess is False:
         del listLines_1
         del listLines_2
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return bIdentical, bSuccess, sResult

      # -- check number of lines
      nNrOfLines_1 = len(listLines_1)
      nNrOfLines_2 = len(listLines_2)
      if nNrOfLines_1 != nNrOfLines_2:
         del listLines_1
         del listLines_2
         bIdentical = False
         bSuccess   = True
         sResult    = f"The files contain different number of lines (file 1: {nNrOfLines_1} lines, file 2: {nNrOfLines_2} lines"
         return bIdentical, bSuccess, sResult

      if sPatternFile is None:
         # no pattern given => compare the original version of the files
         for nIndex, sLine_1 in enumerate(listLines_1):
            sLine_2 = listLines_2[nIndex]
            if sLine_1 != sLine_2:
               del listLines_1
               del listLines_2
               bIdentical = False
               bSuccess   = True
               sResult    = f"Found deviating lines\n(1) '{sLine_1}'\n(2) '{sLine_2}'"
               return bIdentical, bSuccess, sResult
      else:
         if self.__bToScreen is True:
            print()
            print("[PATTERN]")
         # -- read pattern for comparison of files
         oPatternFile = CFile(sPatternFile)
         listPatterns, bSuccess, sResult = oPatternFile.ReadLines(bSkipBlankLines=True, bLStrip=True, bRStrip=True, bToScreen=self.__bToScreen)
         del oPatternFile
         if bSuccess is False:
            del listPatterns
            sResult = CString.FormatResult(sMethod, bSuccess, sResult)
            return bIdentical, bSuccess, sResult
         # -- compile pattern for comparison of files
         listRegEx = []
         for sPattern in listPatterns:
            listRegEx.append(re.compile(sPattern))
         del listPatterns
         # -- apply pattern to content of file 1
         listSubsetLines_1 = []
         for sLine in listLines_1:
            for RegEx in listRegEx:
               listPositions = RegEx.findall(sLine)
               if len(listPositions) > 0:
                  listSubsetLines_1.append(listPositions[0])
                  break # for RegEx in listRegEx:
         # eof for sLine in listLines_1:
         del listLines_1
         # -- apply pattern to content of file 2
         listSubsetLines_2 = []
         for sLine in listLines_2:
            for RegEx in listRegEx:
               listPositions = RegEx.findall(sLine)
               if len(listPositions) > 0:
                  listSubsetLines_2.append(listPositions[0])
                  break # for RegEx in listRegEx:
         # eof for sLine in listLines_2:
         del listLines_2
         del listRegEx

         # -- check number of lines
         nNrOfSubsetLines_1 = len(listSubsetLines_1)
         nNrOfSubsetLines_2 = len(listSubsetLines_2)
         if nNrOfSubsetLines_1 != nNrOfSubsetLines_2:
            del listSubsetLines_1
            del listSubsetLines_2
            bIdentical = False
            bSuccess   = True
            sResult    = f"The subsets of files contain different number of lines (subset 1: {nNrOfSubsetLines_1} lines, subset 2: {nNrOfSubsetLines_2} lines"
            return bIdentical, bSuccess, sResult

         # -- compare subsets of content
         for nIndex, sLine_1 in enumerate(listSubsetLines_1):
            sLine_2 = listSubsetLines_2[nIndex]
            if sLine_1 != sLine_2:
               del listSubsetLines_1
               del listSubsetLines_2
               bIdentical = False
               bSuccess   = True
               sResult    = f"Found deviating lines\n(1) '{sLine_1}'\n(2) '{sLine_2}'"
               return bIdentical, bSuccess, sResult
         # eof for nIndex, sLine_1 in enumerate(listSubsetLines_1):
         del listSubsetLines_1
         del listSubsetLines_2

      # eof else - if sPatternFile is None:

      # final result
      bIdentical = True
      bSuccess   = True
      sResult    = "Both files have same content"

      return bIdentical, bSuccess, sResult

   # eof def Compare(self, sFile_1=None, sFile_2=None, sPatternFile=None):

# eof class CComparison(object):

# --------------------------------------------------------------------------------------------------------------







