.. Copyright 2020-2023 Robert Bosch GmbH

.. Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

.. http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

Test Use Cases
==============

* **Test PEC_0001**

  [CFILE / GOODCASE]

   **Write and Read with explicit Close**

   Expected: Teststring is written to file and read from this file

----

* **Test PEC_0002**

  [CFILE / GOODCASE]

   **Write and Read without explicit Close**

   Expected: Teststring is written to file and read from this file

----

* **Test PEC_0003**

  [CFILE / GOODCASE]

   **Delete a file**

   Expected: File is deleted

----

* **Test PEC_0004**

  [CFILE / GOODCASE]

   **Append and Read with explicit Close**

   Expected: Lines are appended and read

----

* **Test PEC_0005**

  [CFILE / GOODCASE]

   **Append and Read without explicit Close**

   Expected: Lines are appended and read

----

* **Test PEC_0006**

  [CFILE / GOODCASE]

   **Write to new file; repeated ReadLines with filter**

   Expected: Lines are read depending on filter settings

----

* **Test PEC_0007**

  [CFILE / GOODCASE]

   **ReadLines; skip blank lines**

   Expected: Lines are read depending on filter settings

----

* **Test PEC_0008**

  [CFILE / GOODCASE]

   **Write, Append and ReadLines combinations**

   Expected: Lines are read depending on previous Write or Append

----

* **Test PEC_0009**

  [CFILE / GOODCASE]

   **Write and ReadLines of composite data types: list, tuple, set and dict**

   Expected: Content of composite data is resolved and written to file line by line separately

----

* **Test PEC_0010**

  [CFILE / GOODCASE]

   **Write: Prefix and additional vertical space**

   Expected: Prefix and additional vertical space are added to written content

----

* **Test PEC_0011**

  [CFILE / GOODCASE]

   **CopyTo, MoveTo and GetFileInfo**

   Expected: File is copied, moved and file info is correct

----

* **Test PEC_0012**

  [CFILE / GOODCASE]

   **ConfirmDelete**

   Expected: Returns True or False depending on deletion has to be confirmed or not

----

* **Test PEC_0050**

  [CFILE / BADCASE]

   **Path to source file does not exist**

   Expected: Source file not written, not deleted, not copied, not moved

----

* **Test PEC_0051**

  [CFILE / BADCASE]

   **Path to destination file does not exist**

   Expected: Source file not copied and not moved to destination

----

* **Test PEC_0052**

  [CFILE / BADCASE]

   **source file == destination file**

   Expected: Source file not copied and not moved to destination

----

* **Test PEC_0053**

  [CFILE / BADCASE]

   **bOverwrite and access violations**

   Expected: Existing files are not overwritten, if not allowed; no multiple class instances pointing to the same file

----

* **Test PEC_0100**

  [CFOLDER / GOODCASE]

   **Create a folder, bOverwrite=False**

   Expected: New folder is created, but existing folder is not overwritten

----

* **Test PEC_0101**

  [CFOLDER / GOODCASE]

   **Create a folder, bOverwrite=True**

   Expected: New folder is created, existing folder is overwritten

----

* **Test PEC_0102**

  [CFOLDER / GOODCASE]

   **Create and delete a folder, bRecursive=True**

   Expected: Entire path to folder is created; folder is deleted

----

* **Test PEC_0103**

  [CFOLDER / GOODCASE]

   **Delete a folder with content write protected**

   Expected: Write protection is removed, folder is deleted

----

* **Test PEC_0104**

  [CFOLDER / GOODCASE]

   **Copy a folder**

   Expected: Folder is copied

----

* **Test PEC_0105**

  [CFOLDER / GOODCASE]

   **Copy a folder, destination folder already exists**

   Expected: Destination folder is overwritten or not, depending on bOverwrite

----

* **Test PEC_0150**

  [CFOLDER / BADCASE]

   **Copy a folder, source and destination are same folder**

   Expected: Nothing is copied; error message

----

* **Test PEC_0151**

  [CFOLDER / BADCASE]

   **Copy a folder, destination path does not exist**

   Expected: Nothing is copied; error message

----

* **Test PEC_0152**

  [CFOLDER / BADCASE]

   **Copy a folder, destination folder already in use by another instance**

   Expected: Nothing is copied; error message

----

* **Test PEC_0153**

  [CFOLDER / BADCASE]

   **Copy a folder, source folder does not exist**

   Expected: Nothing is copied; error message

----

* **Test PEC_0154**

  [CFOLDER / BADCASE]

   **Create a folder, bOverwrite=True, open file handle**

   Expected: Windows: Access violation; not possible to delete the folder (BADCASE) / Linux: Folder is deleted (GOODCASE)

   *Hint: Platform specific; under Windows test needs some seconds (because of an internal loop of tries)*

----

* **Test PEC_0155**

  [CFOLDER / BADCASE]

   **Multiple CFolder instances of same folder**

   Expected: Error message

----

* **Test PEC_0200**

  [CSTRING / GOODCASE]

   **NormalizePath: Resolve environment variables**

   Expected: String with resolved environment variable is not expected to be the same as the input string

----

* **Test PEC_0201**

  [CSTRING / GOODCASE]

   **NormalizePath: Resolving of environment variables deactivated**

   Expected: String with environment variable is returned unresolved

----

* **Test PEC_0202**

  [CSTRING / GOODCASE]

   **NormalizePath: Convert backslashes**

   Expected: All backslashes replaced by single slashes

----

* **Test PEC_0203**

  [CSTRING / GOODCASE]

   **NormalizePath: Strip surrounding quotes and spaces**

   Expected: Surrounding quotes and spaces are removed

----

* **Test PEC_0204**

  [CSTRING / GOODCASE]

   **NormalizePath: Path with redundant path separators**

   Expected: Redundant path separators removed; all backslashes replaced by single slashes

----

* **Test PEC_0205**

  [CSTRING / GOODCASE]

   **NormalizePath: Path with redundant path separators; bWin=True**

   Expected: Redundant path separators removed; remaining separators are masked backslashes

----

* **Test PEC_0206**

  [CSTRING / GOODCASE]

   **NormalizePath: Path with up-level references**

   Expected: All backslashes replaced by single slashes; up-level references resolved

----

* **Test PEC_0207**

  [CSTRING / GOODCASE]

   **NormalizePath: Path with up-level references; bWin=True**

   Expected: All slashes replaced by double (masked) backslashes; up-level references resolved

----

* **Test PEC_0208**

  [CSTRING / GOODCASE]

   **NormalizePath: Path with up-level references; bWin=True; bMask=False**

   Expected: All slashes replaced by single (unmasked) backslashes; up-level references resolved

----

* **Test PEC_0209**

  [CSTRING / GOODCASE]

   **NormalizePath: Relative input path with absolute reference path**

   Expected: Resulting absolute path is a merge of the absolute reference path and the relative input path; single slashes as separator

----

* **Test PEC_0210**

  [CSTRING / GOODCASE]

   **NormalizePath: Relative input path with absolute reference path; bWin=True; bMask=True**

   Expected: Resulting absolute path is a merge of the absolute reference path and the relative input path; masked backslashes as separator

----

* **Test PEC_0211**

  [CSTRING / GOODCASE]

   **NormalizePath: Path with blanks inside; bConsiderBlanks=True**

   Expected: Paths with blanks inside are encapsulated in quotes; single slashes as separator; up-level references resolved

----

* **Test PEC_0212**

  [CSTRING / GOODCASE]

   **NormalizePath: Path without blanks inside; bConsiderBlanks=True**

   Expected: Paths without blanks inside are not encapsulated in quotes; single slashes as separator

----

* **Test PEC_0213**

  [CSTRING / GOODCASE]

   **NormalizePath: Local network resource paths**

   Expected: Resulting local network resource path contains single slashes as separator

----

* **Test PEC_0214**

  [CSTRING / GOODCASE]

   **NormalizePath: Local network resource paths in web browser format**

   Expected: Resulting local network resource path (web browser format) contains single slashes as separator; bWin has no effect

----

* **Test PEC_0215**

  [CSTRING / GOODCASE]

   **NormalizePath: Internet addresses**

   Expected: Resulting internet address contains single backslashes as separator; bWin has no effect

----

* **Test PEC_0300**

  [CSTRING / GOODCASE]

   **DetectParentPath: Search for a single folder**

   Expected: Path to folder found within start path

----

* **Test PEC_0301**

  [CSTRING / GOODCASE]

   **DetectParentPath: Search for two folders**

   Expected: Expected paths detected one and two levels up

----

* **Test PEC_0302**

  [CSTRING / GOODCASE]

   **DetectParentPath: Search for two folders; with one folder does not exist**

   Expected: Expected path to existing folder detected one level up

----

* **Test PEC_0303**

  [CSTRING / GOODCASE]

   **DetectParentPath: Search for two folders; both folders do not exist**

   Expected: No path detected

----

* **Test PEC_0304**

  [CSTRING / GOODCASE]

   **DetectParentPath: Search for a single folder; additionally search for a file**

   Expected: Expected path to folder detected one level up; one file found

----

* **Test PEC_0305**

  [CSTRING / GOODCASE]

   **DetectParentPath: Search for a single folder; additionally search for a file**

   Expected: Expected path to folder detected one level up; file not found

----

Generated: 16.08.2023 - 14:53:58

