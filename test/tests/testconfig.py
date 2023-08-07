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
# 07.08.2023
#
# --------------------------------------------------------------------------------------------------------------

listofdictUsecases = []

# the following keys are optional, all other keys are mandatory.
# dictUsecase['HINT']         = None
# dictUsecase['COMMENT']      = None

# --------------------------------------------------------------------------------------------------------------
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



