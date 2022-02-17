#  Copyright 2020-2022 Robert Bosch Car Multimedia GmbH
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
# -*- coding: utf-8 -*-

# **************************************************************************************************************
#
# CFile.py
#
# XC-CT/ECA3-Queckenstedt
#
# 26.01.2022
#
# **************************************************************************************************************

# -- import standard Python modules
import os, shutil, platform

# -- import Bosch Python modules
from PythonExtensionsCollection.String.CString import CString

# **************************************************************************************************************

class enFileStatiType:
   closed             = "closed"
   openedforwriting   = "openedforwriting"
   openedforappending = "openedforappending"
   openedforreading   = "openedforreading"

# --------------------------------------------------------------------------------------------------------------

class CFile(object):
   """
|

The class ``CFile`` provides a small set of file functions with extended parametrization (like switches
defining if a file is allowed to be overwritten or not).

Most of the functions at least returns ``bSuccess`` and ``sResult``.

* ``bSuccess`` is ``True`` in case of no error occurred.
* ``bSuccess`` is ``False`` in case of an error occurred.
* ``bSuccess`` is ``None`` in case of a very fatal error occurred (exceptions).

* ``sResult`` contains details about what happens during computation.

Every instance of CFile handles one single file only and forces exclusive access to this file.

It is not possible to create an instance of this class with a file that is already in use by another instance.

It is also not possible to use ``CopyTo`` or ``MoveTo`` to overwrite files that are already in use by another instance.
This makes the file handling more save against access violations.

|
   """
   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def __init__(self, sFile=None):
      self.__sFile            = CString.NormalizePath(sFile)
      self.__oFileHandle      = None
      self.__oFileStatus      = enFileStatiType.closed
      self.__sLastDestination = None

      try:
         CFile.__listFilesInUse
      except:
         CFile.__listFilesInUse = []

      # exclusive access is required (checked by self.__bIsFreeToUse; relevant for destination in CopyTo and MoveTo)
      if self.__sFile in CFile.__listFilesInUse:
         raise Exception(f"The file '{self.__sFile}' is already in use by another CFile instance.")
      else:
         CFile.__listFilesInUse.append(self.__sFile)

   # eof def __init__(self, sFile=None):

   def __del__(self):
      self.Close()
      if self.__sFile in CFile.__listFilesInUse:
         CFile.__listFilesInUse.remove(self.__sFile)

   # eof def __del__(self):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def __bIsFreeToUse(self, sFile=None):

      bIsFreeToUse = False # init
      if sFile is None:
         bIsFreeToUse = False # error handling
      else:
         if sFile in CFile.__listFilesInUse:
            bIsFreeToUse = False
         else:
            bIsFreeToUse = True
      return bIsFreeToUse

   # eof def __bIsFreeToUse(self, sFile=None):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def __OpenForWriting(self):
      """
|

Opens a text file for writing.

Returns ``bSuccess`` and ``sResult`` (feedback).

|
      """

      sMethod = "CFile::__OpenForWriting"

      if self.__sFile is None:
         bSuccess = False
         sResult  = "self.__sFile is None; please provide path and name of a file when creating a CFile object."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      bSuccess, sResult = self.Close()
      if bSuccess is not True:
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      try:
         self.__oFileHandle = open(self.__sFile, "w", encoding="utf-8")
         self.__oFileStatus = enFileStatiType.openedforwriting
         bSuccess = True
         sResult  = f"File '{self.__sFile}' is open for writing"
      except Exception as reason:
         self.Close()
         bSuccess = None
         sResult  = f"Not possible to open file '{self.__sFile}' for writing.\nReason: " + str(reason)

      sResult = CString.FormatResult(sMethod, bSuccess, sResult)
      return bSuccess, sResult

   # eof def __OpenForWriting(self):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def __OpenForAppending(self):
      """
|

Opens a text file for appending.

Returns ``bSuccess`` and ``sResult`` (feedback).

|
      """

      sMethod = "CFile::__OpenForAppending"

      if self.__sFile is None:
         bSuccess = False
         sResult  = "self.__sFile is None; please provide path and name of a file when creating a CFile object."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      bSuccess, sResult = self.Close()
      if bSuccess is not True:
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      try:
         self.__oFileHandle = open(self.__sFile, "a", encoding="utf-8")
         self.__oFileStatus = enFileStatiType.openedforappending
         bSuccess = True
         sResult  = f"File '{self.__sFile}' is open for appending"
      except Exception as reason:
         self.Close()
         bSuccess = None
         sResult  = f"Not possible to open file '{self.__sFile}' for appending.\nReason: " + str(reason)

      sResult = CString.FormatResult(sMethod, bSuccess, sResult)
      return bSuccess, sResult

   # eof def __OpenForAppending(self):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def __OpenForReading(self):
      """
|

Opens a text file for reading.

Returns ``bSuccess`` and ``sResult`` (feedback).

|
      """

      sMethod = "CFile::__OpenForReading"

      if self.__sFile is None:
         bSuccess = False
         sResult  = "self.__sFile is None; please provide path and name of a file when creating a CFile object."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      bSuccess, sResult = self.Close()
      if bSuccess is not True:
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      try:
         self.__oFileHandle = open(self.__sFile, "r", encoding="utf-8")
         self.__oFileStatus = enFileStatiType.openedforreading
         bSuccess = True
         sResult  = f"File '{self.__sFile}' is open for reading"
      except Exception as reason:
         self.Close()
         bSuccess = None
         sResult  = f"Not possible to open file '{self.__sFile}' for reading.\nReason: " + str(reason)

      sResult = CString.FormatResult(sMethod, bSuccess, sResult)
      return bSuccess, sResult

   # eof def __OpenForReading(self):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def Close(self):
      """
|

Closes the opened file.

Returns ``bSuccess`` and ``sResult`` (feedback).

|
      """
      sMethod = "CFile::Close"

      if self.__oFileHandle is not None:
         try:
            self.__oFileHandle.flush()
            self.__oFileHandle.close()
            bSuccess = True
            sResult  = f"File '{self.__sFile}' closed"
         except Exception as reason:
            bSuccess = None
            sResult  = f"Exception while closing file '{self.__sFile}'.\nReason: " + str(reason)
         self.__oFileHandle = None
      else:
         bSuccess = True
         sResult  = "Done"

      self.__oFileStatus = enFileStatiType.closed

      sResult = CString.FormatResult(sMethod, bSuccess, sResult)
      return bSuccess, sResult

   # eof def Close(self):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def Delete(self, bConfirmDelete=True):
      """
|

Deletes the current file.

**bConfirmDelete**

   Defines if it will be handled as error if the file does not exist.

   If ``True``: If the file does not exist, the method indicates an error (``bSuccess = False``).

   If ``False``: It doesn't matter if the file exists or not.

Returns ``bSuccess`` and ``sResult`` (feedback).

|
      """

      sMethod = "CFile::Delete"

      if self.__sFile is None:
         bSuccess = False
         sResult  = "self.__sFile is None; please provide path and name of a file when creating a CFile object."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      if os.path.isfile(self.__sFile) is False:
         if bConfirmDelete is True:
            bSuccess = False
         else:
            bSuccess = True
         sResult = f"Nothing to delete. The file '{self.__sFile}' does not exist."
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      bSuccess, sResult = self.Close()
      if bSuccess is not True:
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      try:
         os.remove(self.__sFile)
         bSuccess = True
         sResult  = f"File '{self.__sFile}' deleted."
      except Exception as reason:
         bSuccess = None
         sResult  = f"Exception while deleting file '{self.__sFile}'.\nReason: " + str(reason)

      sResult = CString.FormatResult(sMethod, bSuccess, sResult)
      return bSuccess, sResult

   # eof def Delete(self, bConfirmDelete=True):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def __PrepareOutput(self, Content=""):
      """
|

Helper for ``Write`` and ``Append`` (consideration of composite data types).

Returns a list of strings (that will be written to file).

|
      """

      listOut = []

      if type(Content) == list:
         for element in Content:
            listOut.append(str(element))
      elif type(Content) == tuple:
         for element in Content:
            listOut.append(str(element))
      elif type(Content) == set:
         for element in Content:
            listOut.append(str(element))
      elif type(Content) == dict:
         listKeys = Content.keys()
         nRJust = 0
         for key in listKeys:
            sKey = str(key) # because also numerical values can be keys
            if len(sKey) > nRJust:
               nRJust = len(sKey)
         for key in listKeys:
            sKey = str(key) # because also numerical values can be keys
            sOut = sKey.rjust(nRJust, ' ') + " : " + str(Content[key])
            listOut.append(sOut)
      elif str(type(Content)).lower().find('dotdict') >=0:
         try:
            listKeys = Content.keys()
            nRJust = 0
            for key in listKeys:
               sKey = str(key) # because also numerical values can be keys
               if len(sKey) > nRJust:
                  nRJust = len(sKey)
            for key in listKeys:
               sKey = str(key) # because also numerical values can be keys
               sOut = sKey.rjust(nRJust, ' ') + " : " + str(Content[key])
               listOut.append(sOut)
         except Exception as reason:
            listOut.append(str(Content))
      else:
         listOut.append(str(Content))

      return listOut

   # eof def __PrepareOutput(self, Content=""):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def Write(self, Content="", nVSpaceAfter=0, sPrefix=None, bToScreen=False):
      """
|

Writes the content of a variable ``Content`` to file.

If ``Content`` is not a string, the ``Write`` method resolves the data structure (therefore ``Content`` can also be of type
``list``, ``tuple``, ``set``, ``dict``, ``dotdict``).

Adds vertical space ``nVSpaceAfter`` (= number of blank lines) after ``Content``.

Prints ``Content`` also to screen in case of ``bToScreen`` is ``True`` (default: ``False``).

Returns ``bSuccess`` and ``sResult`` (feedback).

|
      """

      sMethod = "CFile::Write"

      if self.__oFileStatus != enFileStatiType.openedforwriting:
         bSuccess, sResult = self.__OpenForWriting()
         if bSuccess is not True:
            sResult = CString.FormatResult(sMethod, bSuccess, sResult)
            return bSuccess, sResult

      listOut = self.__PrepareOutput(Content)

      for nCnt in range(nVSpaceAfter):
         listOut.append("")

      if bToScreen is True:
         for sOut in listOut:
            if ( (sPrefix is not None) and (sOut != '') ):
               sOut = f"{sPrefix}{sOut}"
            print(sOut)

      bSuccess = True
      sResult  = "Done"
      try:
         for sOut in listOut:
            if ( (sPrefix is not None) and (sOut != '') ):
               sOut = f"{sPrefix}{sOut}"
            self.__oFileHandle.write(sOut + "\n")
      except Exception as reason:
         bSuccess = None
         sResult  = f"Not possible to write to file '{self.__sFile}'.\nReason: " + str(reason)

      sResult = CString.FormatResult(sMethod, bSuccess, sResult)
      return bSuccess, sResult

   # eof def Write(self, Content="", nVSpaceAfter=0, sPrefix=None, bToScreen=False):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def Append(self, Content="", nVSpaceAfter=0, sPrefix=None, bToScreen=False):
      """
|

Appends the content of a variable ``Content`` to file.

If ``Content`` is not a string, the ``Write`` method resolves the data structure (therefore ``Content`` can also be of type
``list``, ``tuple``, ``set``, ``dict``, ``dotdict``).

Adds vertical space ``nVSpaceAfter`` (= number of blank lines) after ``Content``.

Prints ``Content`` also to screen in case of ``bToScreen`` is ``True`` (default: ``False``).

Returns ``bSuccess`` and ``sResult`` (feedback).

|
      """

      sMethod = "CFile::Append"

      if self.__oFileStatus != enFileStatiType.openedforappending:
         bSuccess, sResult = self.__OpenForAppending()
         if bSuccess is not True:
            sResult = CString.FormatResult(sMethod, bSuccess, sResult)
            return bSuccess, sResult

      listOut = self.__PrepareOutput(Content)

      for nCnt in range(nVSpaceAfter):
         listOut.append("")

      if bToScreen is True:
         for sOut in listOut:
            if ( (sPrefix is not None) and (sOut != '') ):
               sOut = f"{sPrefix}{sOut}"
            print(sOut)

      bSuccess = True
      sResult  = "Done"
      try:
         for sOut in listOut:
            if ( (sPrefix is not None) and (sOut != '') ):
               sOut = f"{sPrefix}{sOut}"
            self.__oFileHandle.write(sOut + "\n")
      except Exception as reason:
         bSuccess = None
         sResult  = f"Not possible to append to file '{self.__sFile}'.\nReason: " + str(reason)

      sResult = CString.FormatResult(sMethod, bSuccess, sResult)
      return bSuccess, sResult

   # eof def Append(self, Content="", nVSpaceAfter=0, sPrefix=None, bToScreen=False):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def ReadLines(self,
                 bCaseSensitive  = True,
                 bSkipBlankLines = False,
                 sComment        = None,
                 sStartsWith     = None,
                 sEndsWith       = None,
                 sStartsNotWith  = None,
                 sEndsNotWith    = None,
                 sContains       = None,
                 sContainsNot    = None,
                 sInclRegEx      = None,
                 sExclRegEx      = None,
                 bLStrip         = False,
                 bRStrip         = True,
                 bToScreen       = False):
      """
|

Reads content from current file. Returns an array of lines together with ``bSuccess`` and ``sResult`` (feedback).

The method takes care of opening and closing the file. The complete file content is read by ``ReadLines`` in one step,
but with the help of further parameters it is possible to reduce the content by including and excluding lines.

T.B.C.

|
      """

      sMethod = "[CFile::ReadLines]"

      listLines = []

      if os.path.isfile(self.__sFile) is False:
         bSuccess = False
         sResult  = f"The file '{self.__sFile}' does not exist."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return listLines, bSuccess, sResult

      # !!! independend from:  self.__oFileStatus != enFileStatiType.openedforreading: !!!
      # Reason: Repeated call of ReadLines needs to have the read pointer at the beginning of the file.
      bSuccess, sResult = self.__OpenForReading()
      if bSuccess is not True:
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return listLines, bSuccess, sResult

      try:
         sFileContent = self.__oFileHandle.read()
      except Exception as reason:
         bSuccess = None
         sResult  = f"Not possible to read from file '{self.__sFile}'.\nReason: " + str(reason)
         return listLines, bSuccess, sResult

      bSuccess, sResult = self.Close()
      if bSuccess is not True:
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return listLines, bSuccess, sResult

      listFileContent = sFileContent.splitlines() # in opposite to readlines this is OS independend!

      for sLine in listFileContent:
         if CString.StringFilter(sString           = sLine,
                                 bCaseSensitive    = bCaseSensitive,
                                 bSkipBlankStrings = bSkipBlankLines,
                                 sComment          = sComment,
                                 sStartsWith       = sStartsWith,
                                 sEndsWith         = sEndsWith,
                                 sStartsNotWith    = sStartsNotWith,
                                 sEndsNotWith      = sEndsNotWith,
                                 sContains         = sContains,
                                 sContainsNot      = sContainsNot,
                                 sInclRegEx        = sInclRegEx,
                                 sExclRegEx        = sExclRegEx,
                                 bDebug            = False) is True:
            if bLStrip is True:
               sLine = sLine.lstrip(" \t\r\n")

            if bRStrip is True:
               sLine = sLine.rstrip(" \t\r\n")

            if bToScreen is True:
               print(sLine)

            listLines.append(sLine)

      # eof for sLine in listFileContent:

      del listFileContent

      nNrOfLines = len(listLines)

      bSuccess = True
      sResult  = f"Read {nNrOfLines} lines from '{self.__sFile}'."
      sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
      return listLines, bSuccess, sResult

   # eof def ReadLines(...)

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def GetFileInfo(self):
      """
|

Returns the following informations about the file (encapsulated within a dictionary):

Key **sFile**

   Path and name of current file

Key **bFileIsExisting**

   ``True`` if file is existing, otherwise not

Key **sFileName**

   The name of the current file (incl. extension)

Key **sFileExtension**

   The extension of the current file

Key **sFileNameOnly**

   The pure name of the current file (without extension)

Key **sFilePath**

   The the path to current file

Key **bFilePathIsExisting**

   ``True`` if file path is existing, otherwise not

|
      """

      sMethod = "CFile::GetFileInfo"

      dFileInfo = {}
      dFileInfo['sFile']               = None
      dFileInfo['bFileIsExisting']     = None
      dFileInfo['sFileName']           = None
      dFileInfo['sFileExtension']      = None
      dFileInfo['sFileNameOnly']       = None
      dFileInfo['sFilePath']           = None
      dFileInfo['bFilePathIsExisting'] = None

      if self.__sFile is None:
         return None

      dFileInfo['sFile']           = self.__sFile
      dFileInfo['bFileIsExisting'] = os.path.isfile(self.__sFile)

      sFileName = os.path.basename(self.__sFile)
      dFileInfo['sFileName'] = sFileName

      sFileExtension = ""
      sFileNameOnly  = ""
      listParts = sFileName.split('.')
      if len(listParts) > 1:
         sFileExtension = listParts[len(listParts)-1]
         sFileNameOnly  = sFileName[:-len(sFileExtension)-1]
      else:
         sFileExtension = ""
         sFileNameOnly  = sFileName

      dFileInfo['sFileExtension']      = sFileExtension
      dFileInfo['sFileNameOnly']       = sFileNameOnly
      dFileInfo['sFilePath']           = os.path.dirname(self.__sFile)
      dFileInfo['bFilePathIsExisting'] = os.path.isdir(dFileInfo['sFilePath'])

      return dFileInfo

   # eof def GetFileInfo(self):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def CopyTo(self, sDestination=None, bOverwrite=False):
      """
|

Copies the current file to ``sDestination``, that can either be a path without file name or a path together with a file name.

In case of the destination file already exists and ``bOverwrite`` is ``True``, than the destination file will be overwritten.

In case of the destination file already exists and ``bOverwrite`` is ``False`` (default), than the destination file will not be overwritten
and ``CopyTo`` returns ``bSuccess = False``.

Returns ``bSuccess`` and ``sResult`` (feedback).

|
      """

      sMethod = "CFile::CopyTo"

      if self.__sFile is None:
         bSuccess = False
         sResult  = "self.__sFile is None; please provide path and name of a file when creating a CFile object."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      if os.path.isfile(self.__sFile) is False:
         bSuccess = False
         sResult  = f"The file '{self.__sFile}' does not exist, therefore nothing can be copied."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      if sDestination is None:
         bSuccess = False
         sResult  = "sDestination is None; please provide path and name of destination file. Or at least the destination path. In this case the file name will be taken over."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      sDestination = CString.NormalizePath(sDestination)

      bDeleteDestFile = False

      sDestFile = sDestination # default

      if os.path.isdir(sDestination) is True:
         sFileName = os.path.basename(self.__sFile)
         sDestFile = f"{sDestination}/{sFileName}" # file name in destination is required for: shutil.copyfile

      if self.__bIsFreeToUse(sDestFile) is False:
         bSuccess = False
         sResult  = f"The destination file '{sDestFile}' is already in use by another CFile instance."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      self.__sLastDestination = sDestFile

      if os.path.isfile(sDestFile) is True:
         # destination file already exists
         if sDestFile == self.__sFile:
            bSuccess = False
            sResult  = f"Source file and destination file are the same: '{self.__sFile}'. Therefore nothing to do."
            sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
            return bSuccess, sResult

         if bOverwrite is True:
            bDeleteDestFile = True
         else:
            bSuccess = False
            sResult  = f"Not allowed to overwrite existing destination file '{sDestFile}'. Therefore nothing to do."
            sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
            return bSuccess, sResult
      else:
         # destination file not yet exists
         # (we assume here that the destination shall be a file because we already have figured out that the destination is not a folder)
         # => we have to check if the path to the file exists
         sDestFilePath = os.path.dirname(sDestFile)
         if os.path.isdir(sDestFilePath) is True:
            bDeleteDestFile = False
         else:
            bSuccess = False
            sResult  = f"The destination path '{sDestFilePath}' does not exist. The file '{self.__sFile}' cannot be copied."
            sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
            return bSuccess, sResult

      # eof else - if os.path.isfile(sDestFile) is True:

      # analysis done, now the action

      bSuccess, sResult = self.Close()
      if bSuccess is not True:
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      if bDeleteDestFile is True:
         # To delete the destination file explicitely before executing any copy-function is an addon here in this library.
         # The purpose is to be independend from the way the used copy function is handling existing destination files.
         # But this makes only sense under Windows and not under Linux, because Windows is much more strict with access
         # violations than Linux. Therefore we avoid such kind of additional steps in case of the platform is not Windows.
         if platform.system() == "Windows":
            try:
               os.remove(sDestFile)
               bSuccess = True
               sResult  = f"File '{sDestFile}' deleted."
            except Exception as reason:
               bSuccess = None
               sResult  = f"Exception while deleting destination file '{sDestFile}'.\nReason: " + str(reason)
               sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
               return bSuccess, sResult

      try:
         shutil.copyfile(self.__sFile, sDestFile)
         bSuccess = True
         sResult  = f"File '{self.__sFile}' copied to '{sDestFile}'."
      except Exception as reason:
         bSuccess = None
         sResult  = f"Exception while copying file '{self.__sFile}' to '{sDestFile}'.\nReason: " + str(reason)

      sResult = CString.FormatResult(sMethod, bSuccess, sResult)
      return bSuccess, sResult

   # eof def CopyTo(self, sDestination=None, bOverwrite=False):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

   def MoveTo(self, sDestination=None, bOverwrite=False):
      """
|

Moves the current file to ``sDestination``, that can either be a path without file name or a path together with a file name.

In case of the destination file already exists and ``bOverwrite`` is ``True``, than the destination file will be overwritten.

In case of the destination file already exists and ``bOverwrite`` is ``False`` (default), than the destination file will not be overwritten
and ``CopyTo`` returns ``bSuccess = False``.

Returns ``bSuccess`` and ``sResult`` (feedback).

|
      """

      sMethod = "CFile::MoveTo"

      bSuccess, sResult = self.CopyTo(sDestination, bOverwrite)
      if bSuccess is not True:
         sResult = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult

      if os.path.isfile(self.__sLastDestination) is False:
         # the copied file should exist at new location
         bSuccess = None
         sResult  = f"Someting went wrong while copying the file '{self.__sFile}' to '{self.__sLastDestination}'. Aborting."
         sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
         return bSuccess, sResult
      else:
         bSuccess, sResult = self.Delete()
         if bSuccess is not True:
            sResult = CString.FormatResult(sMethod, bSuccess, sResult)
            return bSuccess, sResult

      bSuccess = True
      sResult  = f"File moved from '{self.__sFile}' to '{self.__sLastDestination}'"
      sResult  = CString.FormatResult(sMethod, bSuccess, sResult)
      return bSuccess, sResult

   # eof def MoveTo(self, sDestination=None, bOverwrite=False):

   # --------------------------------------------------------------------------------------------------------------
   # TM***

# eof class CFile(object):

# **************************************************************************************************************


