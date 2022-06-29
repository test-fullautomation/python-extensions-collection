.. Copyright 2020-2022 Robert Bosch GmbH

.. Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

.. http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

Path normalization
------------------

It's not easy to handle paths - and especially the path separators - independend from the operating system.

Under Linux it is obvious that single slashes are used as separator within paths. Whereas the Windows explorer
uses single backslashes. In both operating systems web addresses contains single slashes as separator
when displayed in web browsers.

Using single backslashes within code - as content of string variables - is dangerous because the combination
of a backslash and a letter can be interpreted as escape sequence - and this is maybe not the effect a user wants to have.

To avoid unwanted escape sequences backslashes have to be masked (by the usage of two of them: ``\\``). But also this
could not be the best solution because there are also applications (like the Windows explorer) that are not able to handle
masked backslashes. They expect to get single backslashes within a path.

Preparing a path for best usage within code also includes collapsing redundant separators and up-level references.
Python already provides functions to do this, but the outcome (path contains slashes or backslashes) depends on the
operating system. And like already mentioned above also under Windows backslashes might not be the preferred choice.

It also has to be considered that redundant separators at the beginning of an address of a local network resource
(like ``\\server.com``) and or inside an internet address (like ``https:\\server.com``) must **not** be collapsed!
Unfortunately the Python function ``normpath`` does not consider this context.

To give the user full control about the format of a path, independend from the operating system and independend if it's
a local path, a path to a local network resource or an internet address, the function ``CString::NormalizePath()`` provides
lot's of parameters to influence the result.


File access with CFile
----------------------

The motivation for the CFile module contains two main topics:

1. More user control by introducing further parameter for file access functions. With high priority ``CFile`` enables the user
   to take care about that nothing existing is overwritten accidently.
2. Hide the file handles und use the mechanism of class variables to avoid access violations independend from
   the way different operation systems like Windows and Unix are handling this.

This shortens the code, eases the implementation and makes tests (in which this module is used) more stable.

*Define two variables with path and name of test files.*

Under Windows:

.. code:: python

   sFile_1 = r"%TMP%\CFile_TestFile_1.txt"
   sFile_2 = r"%TMP%\CFile_TestFile_2.txt"

Or under Linux:

.. code:: python

   sFile_1 = r"/tmp/CFile_TestFile_1.txt"
   sFile_2 = r"/tmp/CFile_TestFile_2.txt"

*The first class instance:*

.. code:: python

   oFile_1 = CFile(sFile_1)

``oFile_1`` is the instance of a class - *and not the file handle*. The file handle is hidden, the user has nothing to do with it.

Every class instance can work with one single file only (during the complete instance lifetime) and has exclusive access to this file.

No other class instance is allowed to use this file. Therefore the second line in the following code throws an exception:

.. code:: python

   oFile_1_A = CFile(sFile_1)
   oFile_1_B = CFile(sFile_1)

It's more save to implement in this way:

.. code:: python

   try:
      oFile_1 = CFile(sFile_1)
   except Exception as reason:
      print(str(reason))

For writing content to files two methods are available: ``Write()`` and ``Append()``.

Using ``Write()`` causes the class to open the file for writing ('w') - in case of the file is not already opened for writing.
Using ``Append()`` causes the class to open the file for appending ('a') - in case of the file is not already opened for appending.

Switching between ``Write()`` and ``Append()`` causes an intermediate file handle ``close()`` internally!

*Write some content to file:*

.. code:: python

   bSuccess, sResult = oFile_1.Write("A B C")
   print(f"> sResult oFile_1.Write : '{sResult}' / bSuccess : {bSuccess}")

Most of the functions returns at least ``bSuccess`` and ``sResult``.

* ``bSuccess`` is ``True`` in case of no error occurred.
* ``bSuccess`` is ``False`` in case of an error occurred.
* ``bSuccess`` is ``None`` in case of a very fatal error occurred (exceptions).
* ``sResult`` contains details about what happens during computation.

It is possible now to continue with using ``oFile_1.Write("...")``; the content will be appended - as long as the file
is still open for writing.

Some functions close the file handle (e.g. ``ReadLines()``). Therefore sequences like

.. code:: python

   oFile_1.Write("...")
   oFile_1.Readlines("...")
   oFile_1.Write("...")

should be avoided - because the ``Write()`` after the ``ReadLines()`` starts the file from scratch and the file content
written by the previous ``Write()`` calls is lost.

For appending content to a file use the function ``Append()``.

*Append content to file:*

.. code:: python

   bSuccess, sResult = oFile_1.Append("A B C")

For reading content from a file use the function ``ReadLines()``.

*Read from file:*

.. code:: python

   listLines_1, bSuccess, sResult = oFile_1.ReadLines()
   for sLine in listLines_1:
      print(f"{sLine}")

Additionally to ``bSuccess`` and ``sResult`` the function returnes a list of lines.

Internally ``ReadLines()`` takes care about:

* Closing the file - in case the file is still opened
* Opening the file for reading
* Reading the content line by line until the end of file is reached
* Closing the file

To avoid code like this

.. code:: python

   for sLine in listLines_1:
      print(f"{sLine}")

it is also possible to let ``ReadLines()`` do this:

.. code:: python

   listLines_1, bSuccess, sResult = oFile_1.ReadLines(bToScreen=True)

A function to read a single line from file only is not available, but it is possible to use some filter parameter of ``ReadLines()``
to reduce the amount of content already during the file is read. This prevents the user from implementing further loops.

Let's assume the following:

* The file ``sFile_1`` contains empty lines
* The file ``sFile_1`` contains also lines, that are commented out (with a hash '``#``' at the beginning)
* We want ``ReadLines()`` to skip empty lines and lines that are commented out

This can be imlemented in the following way.

*Read a subset of file content:*

.. code:: python

   listLines_1, bSuccess, sResult = oFile_1.ReadLines(bSkipBlankLines=True,
                                                      sComment='#')

It is a good practice to close file handles as soon as possible. Therefore ``CFile`` provides the possibility to do this explicitely.

*Close a file handle:*

.. code:: python

   bSuccess, sResult = oFile_1.Close()

This makes sense in case of later again access to this file is needed.

Additionally to that the file handle is closed implicitely:

* in case of it is required (e.g. when switching between read and write access),
* in case of the class instance is destoyed.

Therefore an alternative to the ``Close()`` function is the deletion of the class instance:

.. code:: python

   del oFile_1

This makes sense in case of access to this file is not needed any more.

It is recommended to prefer ``del`` (instead of ``Close()``) to avoid to keep too much not used objects for a too long length of time in memory.

A file can be copied to another file.

*Copy a file:*

.. code:: python

   bSuccess, sResult = oFile_1.CopyTo(sFile_2)

The destination (``sFile_2`` in the example above) can either be a full path and name of a file or the path only.

It makes a difference if the destination file exists or not. The optional parameter ``bOverwrite`` controls the behavior of ``CopyTo()``.

The default is that it is not allowed to overwrite an existing destination file: ``bOverwrite`` is ``False``. ``CopyTo()`` returns
``bSuccess = False`` in this case.

In case the user want to allow ``CopyTo()`` to overwrite existing destination files, it has to be coded explicitely:

.. code:: python

   bSuccess, sResult = oFile_1.CopyTo(sFile_2, bOverwrite=True)

A file can be moved to another file.

*Move a file:*

.. code:: python

   bSuccess, sResult = oFile_1.MoveTo(sFile_2)

Also ``MoveTo()`` supports ``bOverwrite``. The behavior is the same as ``CopyTo()``.

A file can be deleted.

*Delete a file:*

.. code:: python

   bSuccess, sResult = oFile_1.Delete()

It is possible to distinguish between two different motivations to delete a file:

1. *Explicitely do a deletion*

   This requires that the file to be deleted, does exist.

2. *Making sure only that the files does not exist*

   In this case it doesn't matter that maybe there is nothing to delete because the file already does not exist.

The optional parameter ``bConfirmDelete`` controls this behavior.

Default is that ``Delete()`` requires an existing file to delete:

.. code:: python

   bSuccess, sResult = oFile_1.Delete(bConfirmDelete=True)

In case of the file does not exist, ``Delete()`` returns ``bSuccess = False``.

``Delete()`` also returns ``bSuccess = False|None`` in case of an existing file cannot be deleted (e.g. because of an access violation).

If it doesn't matter it the file exists or not, it has to be coded explicitely:

.. code:: python

   bSuccess, sResult = oFile_1.Delete(bConfirmDelete=False)

In this case ``Delete()`` only returns ``bSuccess = False|None`` in case of an existing file cannot be deleted (e.g. because of an access violation).

**Avoid access violations**

Like already mentioned above every instance of ``CFile`` has an exclusive access to it's own file.

Only in case of ``CopyTo()`` and ``MoveTo()`` other files are involved: the destination files.

To avoid access violations it is not possible to copy or move a file to another file, that is under access of another instance of ``CFile``.

In the following example ``oFile_1.CopyTo(sFile_2)`` returns ``bSuccess = False`` because ``sFile_2`` is already in access by ``oFile_2``.

.. code:: python

   oFile_1 = CFile(sFile_1)
   bSuccess, sResult = oFile_1.Write("A B C")

   oFile_2 = CFile(sFile_2)
   listLines_2, bSuccess, sResult = oFile_2.ReadLines()   

   bSuccess, sResult = oFile_1.CopyTo(sFile_2)

   del oFile_1
   del oFile_2

The solution is to delete the class instances as early as possible.

In the following example the copying is successful:

.. code:: python

   oFile_1 = CFile(sFile_1)
   bSuccess, sResult = oFile_1.Write("A B C")

   oFile_2 = CFile(sFile_2)
   listLines_2, bSuccess, sResult = oFile_2.ReadLines()   
   del oFile_2

   bSuccess, sResult = oFile_1.CopyTo(sFile_2)
   del oFile_1

