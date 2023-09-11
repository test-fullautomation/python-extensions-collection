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
# testconfig.py
#
# XC-CT/ECA3-Queckenstedt
#
# --------------------------------------------------------------------------------------------------------------
#
# 08.09.2023
#
# --------------------------------------------------------------------------------------------------------------

listofdictUsecases = []

# the following keys are optional, all other keys are mandatory.
# dictUsecase['HINT']         = None
# dictUsecase['COMMENT']      = None

# --------------------------------------------------------------------------------------------------------------
# CFile
#TM***
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0001"
dictUsecase['DESCRIPTION']       = "Write and Read with explicit Close"
dictUsecase['EXPECTATION']       = "Teststring is written to file and read from this file"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0002"
dictUsecase['DESCRIPTION']       = "Write and Read without explicit Close"
dictUsecase['EXPECTATION']       = "Teststring is written to file and read from this file"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0003"
dictUsecase['DESCRIPTION']       = "Delete a file"
dictUsecase['EXPECTATION']       = "File is deleted"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0004"
dictUsecase['DESCRIPTION']       = "Append and Read with explicit Close"
dictUsecase['EXPECTATION']       = "Lines are appended and read"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0005"
dictUsecase['DESCRIPTION']       = "Append and Read without explicit Close"
dictUsecase['EXPECTATION']       = "Lines are appended and read"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0006"
dictUsecase['DESCRIPTION']       = "Write to new file; repeated ReadLines with filter"
dictUsecase['EXPECTATION']       = "Lines are read depending on filter settings"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0007"
dictUsecase['DESCRIPTION']       = "ReadLines; skip blank lines"
dictUsecase['EXPECTATION']       = "Lines are read depending on filter settings"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0008"
dictUsecase['DESCRIPTION']       = "Write, Append and ReadLines combinations"
dictUsecase['EXPECTATION']       = "Lines are read depending on previous Write or Append"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0009"
dictUsecase['DESCRIPTION']       = "Write and ReadLines of composite data types: list, tuple, set and dict"
dictUsecase['EXPECTATION']       = "Content of composite data is resolved and written to file line by line separately"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0010"
dictUsecase['DESCRIPTION']       = "Write: Prefix and additional vertical space"
dictUsecase['EXPECTATION']       = "Prefix and additional vertical space are added to written content"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0011"
dictUsecase['DESCRIPTION']       = "CopyTo, MoveTo and GetFileInfo"
dictUsecase['EXPECTATION']       = "File is copied, moved and file info is correct"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0012"
dictUsecase['DESCRIPTION']       = "ConfirmDelete"
dictUsecase['EXPECTATION']       = "Returns True or False depending on deletion has to be confirmed or not"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0050"
dictUsecase['DESCRIPTION']       = "Path to source file does not exist"
dictUsecase['EXPECTATION']       = "Source file not written, not deleted, not copied, not moved"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0051"
dictUsecase['DESCRIPTION']       = "Path to destination file does not exist"
dictUsecase['EXPECTATION']       = "Source file not copied and not moved to destination"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0052"
dictUsecase['DESCRIPTION']       = "source file == destination file"
dictUsecase['EXPECTATION']       = "Source file not copied and not moved to destination"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0053"
dictUsecase['DESCRIPTION']       = "bOverwrite and access violations"
dictUsecase['EXPECTATION']       = "Existing files are not overwritten, if not allowed; no multiple class instances pointing to the same file"
dictUsecase['SECTION']           = "CFILE"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# CFolder
#TM***
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0100"
dictUsecase['DESCRIPTION']       = "Create a folder, bOverwrite=False"
dictUsecase['EXPECTATION']       = "New folder is created, but existing folder is not overwritten"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0101"
dictUsecase['DESCRIPTION']       = "Create a folder, bOverwrite=True"
dictUsecase['EXPECTATION']       = "New folder is created, existing folder is overwritten"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0102"
dictUsecase['DESCRIPTION']       = "Create and delete a folder, bRecursive=True"
dictUsecase['EXPECTATION']       = "Entire path to folder is created; folder is deleted"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0103"
dictUsecase['DESCRIPTION']       = "Delete a folder with content write protected"
dictUsecase['EXPECTATION']       = "Write protection is removed, folder is deleted"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0104"
dictUsecase['DESCRIPTION']       = "Copy a folder"
dictUsecase['EXPECTATION']       = "Folder is copied"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0105"
dictUsecase['DESCRIPTION']       = "Copy a folder, destination folder already exists"
dictUsecase['EXPECTATION']       = "Destination folder is overwritten or not, depending on bOverwrite"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0150"
dictUsecase['DESCRIPTION']       = "Copy a folder, source and destination are same folder"
dictUsecase['EXPECTATION']       = "Nothing is copied; error message"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0151"
dictUsecase['DESCRIPTION']       = "Copy a folder, destination path does not exist"
dictUsecase['EXPECTATION']       = "Nothing is copied; error message"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0152"
dictUsecase['DESCRIPTION']       = "Copy a folder, destination folder already in use by another instance"
dictUsecase['EXPECTATION']       = "Nothing is copied; error message"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0153"
dictUsecase['DESCRIPTION']       = "Copy a folder, source folder does not exist"
dictUsecase['EXPECTATION']       = "Nothing is copied; error message"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0154"
dictUsecase['DESCRIPTION']       = "Create a folder, bOverwrite=True, open file handle"
dictUsecase['EXPECTATION']       = "Windows: Access violation; not possible to delete the folder (BADCASE) / Linux: Folder is deleted (GOODCASE)"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = "Platform specific; under Windows test needs some seconds (because of an internal loop of tries)"
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0155"
dictUsecase['DESCRIPTION']       = "Multiple CFolder instances of same folder"
dictUsecase['EXPECTATION']       = "Error message"
dictUsecase['SECTION']           = "CFOLDER"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# CString
#TM***
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0200"
dictUsecase['DESCRIPTION']       = "NormalizePath: Resolve environment variables"
dictUsecase['EXPECTATION']       = "String with resolved environment variable is not expected to be the same as the input string"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0201"
dictUsecase['DESCRIPTION']       = "NormalizePath: Resolving of environment variables deactivated"
dictUsecase['EXPECTATION']       = "String with environment variable is returned unresolved"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0202"
dictUsecase['DESCRIPTION']       = "NormalizePath: Convert backslashes"
dictUsecase['EXPECTATION']       = "All backslashes replaced by single slashes"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0203"
dictUsecase['DESCRIPTION']       = "NormalizePath: Strip surrounding quotes and spaces"
dictUsecase['EXPECTATION']       = "Surrounding quotes and spaces are removed"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0204"
dictUsecase['DESCRIPTION']       = "NormalizePath: Path with redundant path separators"
dictUsecase['EXPECTATION']       = "Redundant path separators removed; all backslashes replaced by single slashes"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0205"
dictUsecase['DESCRIPTION']       = "NormalizePath: Path with redundant path separators; bWin=True"
dictUsecase['EXPECTATION']       = "Redundant path separators removed; remaining separators are masked backslashes"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0206"
dictUsecase['DESCRIPTION']       = "NormalizePath: Path with up-level references"
dictUsecase['EXPECTATION']       = "All backslashes replaced by single slashes; up-level references resolved"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0207"
dictUsecase['DESCRIPTION']       = "NormalizePath: Path with up-level references; bWin=True"
dictUsecase['EXPECTATION']       = "All slashes replaced by double (masked) backslashes; up-level references resolved"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0208"
dictUsecase['DESCRIPTION']       = "NormalizePath: Path with up-level references; bWin=True; bMask=False"
dictUsecase['EXPECTATION']       = "All slashes replaced by single (unmasked) backslashes; up-level references resolved"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0209"
dictUsecase['DESCRIPTION']       = "NormalizePath: Relative input path with absolute reference path"
dictUsecase['EXPECTATION']       = "Resulting absolute path is a merge of the absolute reference path and the relative input path; single slashes as separator"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0210"
dictUsecase['DESCRIPTION']       = "NormalizePath: Relative input path with absolute reference path; bWin=True; bMask=True"
dictUsecase['EXPECTATION']       = "Resulting absolute path is a merge of the absolute reference path and the relative input path; masked backslashes as separator"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0211"
dictUsecase['DESCRIPTION']       = "NormalizePath: Path with blanks inside; bConsiderBlanks=True"
dictUsecase['EXPECTATION']       = "Paths with blanks inside are encapsulated in quotes; single slashes as separator; up-level references resolved"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0212"
dictUsecase['DESCRIPTION']       = "NormalizePath: Path without blanks inside; bConsiderBlanks=True"
dictUsecase['EXPECTATION']       = "Paths without blanks inside are not encapsulated in quotes; single slashes as separator"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0213"
dictUsecase['DESCRIPTION']       = "NormalizePath: Local network resource paths"
dictUsecase['EXPECTATION']       = "Resulting local network resource path contains single slashes as separator"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0214"
dictUsecase['DESCRIPTION']       = "NormalizePath: Local network resource paths in web browser format"
dictUsecase['EXPECTATION']       = "Resulting local network resource path (web browser format) contains single slashes as separator; bWin has no effect"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0215"
dictUsecase['DESCRIPTION']       = "NormalizePath: Internet addresses"
dictUsecase['EXPECTATION']       = "Resulting internet address contains single backslashes as separator; bWin has no effect"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
#TM***
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0300"
dictUsecase['DESCRIPTION']       = "DetectParentPath: Search for a single folder"
dictUsecase['EXPECTATION']       = "Path to folder found within start path"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0301"
dictUsecase['DESCRIPTION']       = "DetectParentPath: Search for two folders"
dictUsecase['EXPECTATION']       = "Expected paths detected one and two levels up"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0302"
dictUsecase['DESCRIPTION']       = "DetectParentPath: Search for two folders; with one folder does not exist"
dictUsecase['EXPECTATION']       = "Expected path to existing folder detected one level up"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0303"
dictUsecase['DESCRIPTION']       = "DetectParentPath: Search for two folders; both folders do not exist"
dictUsecase['EXPECTATION']       = "No path detected"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0304"
dictUsecase['DESCRIPTION']       = "DetectParentPath: Search for a single folder; additionally search for a file"
dictUsecase['EXPECTATION']       = "Expected path to folder detected one level up; one file found"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0305"
dictUsecase['DESCRIPTION']       = "DetectParentPath: Search for a single folder; additionally search for a file"
dictUsecase['EXPECTATION']       = "Expected path to folder detected one level up; file not found"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
#TM***
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0400"
dictUsecase['DESCRIPTION']       = "StringFilter: Skip blank strings"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0401"
dictUsecase['DESCRIPTION']       = "StringFilter: Blank strings not skipped"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0402"
dictUsecase['DESCRIPTION']       = "StringFilter: String commented out (1)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0403"
dictUsecase['DESCRIPTION']       = "StringFilter: String commented out (2)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0404"
dictUsecase['DESCRIPTION']       = "StringFilter: String commented out (3)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0405"
dictUsecase['DESCRIPTION']       = "StringFilter: String commented out (4)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0406"
dictUsecase['DESCRIPTION']       = "StringFilter: String commented out (5)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0407"
dictUsecase['DESCRIPTION']       = "StringFilter: String commented out (6)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0408"
dictUsecase['DESCRIPTION']       = "StringFilter: String starts with ..."
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0409"
dictUsecase['DESCRIPTION']       = "StringFilter: String ends with ..."
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0410"
dictUsecase['DESCRIPTION']       = "StringFilter: String starts not with ..."
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0411"
dictUsecase['DESCRIPTION']       = "StringFilter: String ends not with ..."
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0412"
dictUsecase['DESCRIPTION']       = "StringFilter: String contains ... (1)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0413"
dictUsecase['DESCRIPTION']       = "StringFilter: String contains ... (2)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0414"
dictUsecase['DESCRIPTION']       = "StringFilter: String contains ... and contains not ..."
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0415"
dictUsecase['DESCRIPTION']       = "StringFilter: String contains not ..."
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0416"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations; case sensitive"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0417"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations; not case sensitive"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0418"
dictUsecase['DESCRIPTION']       = "StringFilter: Inclusive by regular expression (1)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0419"
dictUsecase['DESCRIPTION']       = "StringFilter: Inclusive by regular expression (2)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0420"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations (1)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0421"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations (2)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0422"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations (3)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0423"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations (4)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0424"
dictUsecase['DESCRIPTION']       = "StringFilter: Exclusive by regular expression (1)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0425"
dictUsecase['DESCRIPTION']       = "StringFilter: Exclusive by regular expression (2)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0426"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations (5)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0427"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations (6)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0428"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations (7)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0429"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter combinations (8)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0430"
dictUsecase['DESCRIPTION']       = "StringFilter: Handling of blanks (1)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0431"
dictUsecase['DESCRIPTION']       = "StringFilter: Handling of blanks (2)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0432"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter string lists (1)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0433"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter string lists (2)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0434"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter string lists (3)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0435"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter string lists (4)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0436"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter string lists (5)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0437"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter string lists (6)"
dictUsecase['EXPECTATION']       = "Returned: False"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0438"
dictUsecase['DESCRIPTION']       = "StringFilter: Filter string lists (7)"
dictUsecase['EXPECTATION']       = "Returned: True"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0500"
dictUsecase['DESCRIPTION']       = "FormatResult: Success (1)"
dictUsecase['EXPECTATION']       = "Message formatted as success, with method"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0501"
dictUsecase['DESCRIPTION']       = "FormatResult: Success (2)"
dictUsecase['EXPECTATION']       = "Message formatted as success, without method"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0502"
dictUsecase['DESCRIPTION']       = "FormatResult: Error (1)"
dictUsecase['EXPECTATION']       = "Message formatted as error, with method"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0503"
dictUsecase['DESCRIPTION']       = "FormatResult: Error (2)"
dictUsecase['EXPECTATION']       = "Message formatted as error, without method"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0504"
dictUsecase['DESCRIPTION']       = "FormatResult: Exception (1)"
dictUsecase['EXPECTATION']       = "Message formatted as exception, with method"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0505"
dictUsecase['DESCRIPTION']       = "FormatResult: Exception (2)"
dictUsecase['EXPECTATION']       = "Message formatted as exception, without method"
dictUsecase['SECTION']           = "CSTRING"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# CComparison
#TM***
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------

dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0600"
dictUsecase['DESCRIPTION']       = "Compare two files (with same content; no pattern)"
dictUsecase['EXPECTATION']       = "Result: Files have same content"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0601"
dictUsecase['DESCRIPTION']       = "Compare two files (with different content; no pattern)"
dictUsecase['EXPECTATION']       = "Result: Files have different content"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0602"
dictUsecase['DESCRIPTION']       = "Compare two files (with same content; with pattern)"
dictUsecase['EXPECTATION']       = "Result: Files have same content"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0603"
dictUsecase['DESCRIPTION']       = "Compare two files (with different content; with pattern)"
dictUsecase['EXPECTATION']       = "Result: Files have different content"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0604"
dictUsecase['DESCRIPTION']       = "Compare two files (with different content; with pattern and ignore pattern)"
dictUsecase['EXPECTATION']       = "Result: Files have same content (because the different lines are ignored)"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0650"
dictUsecase['DESCRIPTION']       = "Compare two files (with same path and name)"
dictUsecase['EXPECTATION']       = "No comparison; error message instead"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0651"
dictUsecase['DESCRIPTION']       = "Compare two files (first file not given)"
dictUsecase['EXPECTATION']       = "No comparison; error message instead"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0652"
dictUsecase['DESCRIPTION']       = "Compare two files (second file not given)"
dictUsecase['EXPECTATION']       = "No comparison; error message instead"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0653"
dictUsecase['DESCRIPTION']       = "Compare two files (first file not existing)"
dictUsecase['EXPECTATION']       = "No comparison; error message instead"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0654"
dictUsecase['DESCRIPTION']       = "Compare two files (second file not existing)"
dictUsecase['EXPECTATION']       = "No comparison; error message instead"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0655"
dictUsecase['DESCRIPTION']       = "Compare two files (pattern file not existing)"
dictUsecase['EXPECTATION']       = "No comparison; error message instead"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0656"
dictUsecase['DESCRIPTION']       = "Compare two files (ignore pattern file not existing)"
dictUsecase['EXPECTATION']       = "No comparison; error message instead"
dictUsecase['SECTION']           = "CCOMPARISON"
dictUsecase['SUBSECTION']        = "BADCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# CUtils
#TM***
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0700"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'int'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0701"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'float'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0702"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'str'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0703"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'bool'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0704"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'None'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0705"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'list'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0706"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'tuple'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0707"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'set'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0708"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'dict'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0709"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'dotdict'"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0710"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of nested types"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0711"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'list'; output indented by 5 blanks"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0712"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of type 'list'; output indented by 2 blanks and with prefix"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0713"
dictUsecase['DESCRIPTION']       = "PrettyPrint: Input parameter of nested types; output indented by 2 blanks and with prefix; strings in hexadecimal format"
dictUsecase['EXPECTATION']       = "Input parameter is pretty printed"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = None
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
#TM***
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0800"
dictUsecase['DESCRIPTION']       = "GetInstalledPackages: Default usage"
dictUsecase['EXPECTATION']       = "List of installed Python packages created"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = "This sometimes needs some time"
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------
dictUsecase = {}
dictUsecase['TESTID']            = "PEC_0801"
dictUsecase['DESCRIPTION']       = "GetInstalledPackages: List written to output file"
dictUsecase['EXPECTATION']       = "List of installed Python packages created and written to output file"
dictUsecase['SECTION']           = "CUTILS"
dictUsecase['SUBSECTION']        = "GOODCASE"
dictUsecase['HINT']              = "This sometimes some time"
dictUsecase['COMMENT']           = None
listofdictUsecases.append(dictUsecase)
del dictUsecase
# --------------------------------------------------------------------------------------------------------------








