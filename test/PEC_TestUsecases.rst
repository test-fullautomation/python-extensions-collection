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

Generated: 07.08.2023 - 16:19:07

