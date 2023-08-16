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
# 16.08.2023
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











