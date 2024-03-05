.. Copyright 2020-2024 Robert Bosch GmbH

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

* **Test PEC_0400**

  [CSTRING / GOODCASE]

   **StringFilter: Skip blank strings**

   Expected: Returned: False

----

* **Test PEC_0401**

  [CSTRING / GOODCASE]

   **StringFilter: Blank strings not skipped**

   Expected: Returned: True

----

* **Test PEC_0402**

  [CSTRING / GOODCASE]

   **StringFilter: String commented out (1)**

   Expected: Returned: False

----

* **Test PEC_0403**

  [CSTRING / GOODCASE]

   **StringFilter: String commented out (2)**

   Expected: Returned: False

----

* **Test PEC_0404**

  [CSTRING / GOODCASE]

   **StringFilter: String commented out (3)**

   Expected: Returned: False

----

* **Test PEC_0405**

  [CSTRING / GOODCASE]

   **StringFilter: String commented out (4)**

   Expected: Returned: False

----

* **Test PEC_0406**

  [CSTRING / GOODCASE]

   **StringFilter: String commented out (5)**

   Expected: Returned: False

----

* **Test PEC_0407**

  [CSTRING / GOODCASE]

   **StringFilter: String commented out (6)**

   Expected: Returned: True

----

* **Test PEC_0408**

  [CSTRING / GOODCASE]

   **StringFilter: String starts with ...**

   Expected: Returned: True

----

* **Test PEC_0409**

  [CSTRING / GOODCASE]

   **StringFilter: String ends with ...**

   Expected: Returned: True

----

* **Test PEC_0410**

  [CSTRING / GOODCASE]

   **StringFilter: String starts not with ...**

   Expected: Returned: False

----

* **Test PEC_0411**

  [CSTRING / GOODCASE]

   **StringFilter: String ends not with ...**

   Expected: Returned: False

----

* **Test PEC_0412**

  [CSTRING / GOODCASE]

   **StringFilter: String contains ... (1)**

   Expected: Returned: True

----

* **Test PEC_0413**

  [CSTRING / GOODCASE]

   **StringFilter: String contains ... (2)**

   Expected: Returned: True

----

* **Test PEC_0414**

  [CSTRING / GOODCASE]

   **StringFilter: String contains ... and contains not ...**

   Expected: Returned: False

----

* **Test PEC_0415**

  [CSTRING / GOODCASE]

   **StringFilter: String contains not ...**

   Expected: Returned: False

----

* **Test PEC_0416**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations; case sensitive**

   Expected: Returned: False

----

* **Test PEC_0417**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations; not case sensitive**

   Expected: Returned: True

----

* **Test PEC_0418**

  [CSTRING / GOODCASE]

   **StringFilter: Inclusive by regular expression (1)**

   Expected: Returned: True

----

* **Test PEC_0419**

  [CSTRING / GOODCASE]

   **StringFilter: Inclusive by regular expression (2)**

   Expected: Returned: False

----

* **Test PEC_0420**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations (1)**

   Expected: Returned: False

----

* **Test PEC_0421**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations (2)**

   Expected: Returned: False

----

* **Test PEC_0422**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations (3)**

   Expected: Returned: False

----

* **Test PEC_0423**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations (4)**

   Expected: Returned: False

----

* **Test PEC_0424**

  [CSTRING / GOODCASE]

   **StringFilter: Exclusive by regular expression (1)**

   Expected: Returned: False

----

* **Test PEC_0425**

  [CSTRING / GOODCASE]

   **StringFilter: Exclusive by regular expression (2)**

   Expected: Returned: True

----

* **Test PEC_0426**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations (5)**

   Expected: Returned: True

----

* **Test PEC_0427**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations (6)**

   Expected: Returned: False

----

* **Test PEC_0428**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations (7)**

   Expected: Returned: False

----

* **Test PEC_0429**

  [CSTRING / GOODCASE]

   **StringFilter: Filter combinations (8)**

   Expected: Returned: False

----

* **Test PEC_0430**

  [CSTRING / GOODCASE]

   **StringFilter: Handling of blanks (1)**

   Expected: Returned: False

----

* **Test PEC_0431**

  [CSTRING / GOODCASE]

   **StringFilter: Handling of blanks (2)**

   Expected: Returned: True

----

* **Test PEC_0432**

  [CSTRING / GOODCASE]

   **StringFilter: Filter string lists (1)**

   Expected: Returned: True

----

* **Test PEC_0433**

  [CSTRING / GOODCASE]

   **StringFilter: Filter string lists (2)**

   Expected: Returned: True

----

* **Test PEC_0434**

  [CSTRING / GOODCASE]

   **StringFilter: Filter string lists (3)**

   Expected: Returned: True

----

* **Test PEC_0435**

  [CSTRING / GOODCASE]

   **StringFilter: Filter string lists (4)**

   Expected: Returned: False

----

* **Test PEC_0436**

  [CSTRING / GOODCASE]

   **StringFilter: Filter string lists (5)**

   Expected: Returned: True

----

* **Test PEC_0437**

  [CSTRING / GOODCASE]

   **StringFilter: Filter string lists (6)**

   Expected: Returned: False

----

* **Test PEC_0438**

  [CSTRING / GOODCASE]

   **StringFilter: Filter string lists (7)**

   Expected: Returned: True

----

* **Test PEC_0500**

  [CSTRING / GOODCASE]

   **FormatResult: Success (1)**

   Expected: Message formatted as success, with method

----

* **Test PEC_0501**

  [CSTRING / GOODCASE]

   **FormatResult: Success (2)**

   Expected: Message formatted as success, without method

----

* **Test PEC_0502**

  [CSTRING / GOODCASE]

   **FormatResult: Error (1)**

   Expected: Message formatted as error, with method

----

* **Test PEC_0503**

  [CSTRING / GOODCASE]

   **FormatResult: Error (2)**

   Expected: Message formatted as error, without method

----

* **Test PEC_0504**

  [CSTRING / GOODCASE]

   **FormatResult: Exception (1)**

   Expected: Message formatted as exception, with method

----

* **Test PEC_0505**

  [CSTRING / GOODCASE]

   **FormatResult: Exception (2)**

   Expected: Message formatted as exception, without method

----

* **Test PEC_0600**

  [CCOMPARISON / GOODCASE]

   **Compare two files (with same content; no pattern)**

   Expected: Result: Files have same content

----

* **Test PEC_0601**

  [CCOMPARISON / GOODCASE]

   **Compare two files (with different content; no pattern)**

   Expected: Result: Files have different content

----

* **Test PEC_0602**

  [CCOMPARISON / GOODCASE]

   **Compare two files (with same content; with pattern)**

   Expected: Result: Files have same content

----

* **Test PEC_0603**

  [CCOMPARISON / GOODCASE]

   **Compare two files (with different content; with pattern)**

   Expected: Result: Files have different content

----

* **Test PEC_0604**

  [CCOMPARISON / GOODCASE]

   **Compare two files (with different content; with pattern and ignore pattern)**

   Expected: Result: Files have same content (because the different lines are ignored)

----

* **Test PEC_0650**

  [CCOMPARISON / BADCASE]

   **Compare two files (with same path and name)**

   Expected: No comparison; error message instead

----

* **Test PEC_0651**

  [CCOMPARISON / BADCASE]

   **Compare two files (first file not given)**

   Expected: No comparison; error message instead

----

* **Test PEC_0652**

  [CCOMPARISON / BADCASE]

   **Compare two files (second file not given)**

   Expected: No comparison; error message instead

----

* **Test PEC_0653**

  [CCOMPARISON / BADCASE]

   **Compare two files (first file not existing)**

   Expected: No comparison; error message instead

----

* **Test PEC_0654**

  [CCOMPARISON / BADCASE]

   **Compare two files (second file not existing)**

   Expected: No comparison; error message instead

----

* **Test PEC_0655**

  [CCOMPARISON / BADCASE]

   **Compare two files (pattern file not existing)**

   Expected: No comparison; error message instead

----

* **Test PEC_0656**

  [CCOMPARISON / BADCASE]

   **Compare two files (ignore pattern file not existing)**

   Expected: No comparison; error message instead

----

* **Test PEC_0700**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'int'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0701**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'float'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0702**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'str'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0703**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'bool'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0704**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'None'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0705**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'list'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0706**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'tuple'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0707**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'set'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0708**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'dict'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0709**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'dotdict'**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0710**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of nested types**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0711**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'list'; output indented by 5 blanks**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0712**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of type 'list'; output indented by 2 blanks and with prefix**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0713**

  [CUTILS / GOODCASE]

   **PrettyPrint: Input parameter of nested types; output indented by 2 blanks and with prefix; strings in hexadecimal format**

   Expected: Input parameter is pretty printed

----

* **Test PEC_0800**

  [CUTILS / GOODCASE]

   **GetInstalledPackages: Default usage**

   Expected: List of installed Python packages created

   *Hint: This sometimes needs some time*

----

* **Test PEC_0801**

  [CUTILS / GOODCASE]

   **GetInstalledPackages: List written to output file**

   Expected: List of installed Python packages created and written to output file

   *Hint: This sometimes some time*

----

Generated: 08.09.2023 - 17:36:34

