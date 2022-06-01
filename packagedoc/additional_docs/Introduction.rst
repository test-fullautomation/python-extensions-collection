The Python Extensions Collection package extends the functionality of Python by some useful functions
that are not available in Python immediately.

This covers for example string operations like normalizing a path or searching
for parent directories within a path.

The Python Extensions Collection contains several Python modules and every module has to be imported separately
in case of the functions inside are needed.

**Module import**

The modules of the Python Extension Collection and their methods can be accessed in the following ways:

*CFile*

.. code:: python

   from PythonExtensionsCollection.File.CFile import CFile
   ...
   sFile = r"%TMP%\File.txt"
   oFile = CFile(sFile)

Please consider that ``oFile`` is an instance of the class ``CFile`` - *and not a file handle*.

*CString*

.. code:: python

   from PythonExtensionsCollection.String.CString import CString
   ...
   sPath = CString.NormalizePath(sPath)
   ...
   bAck = CString.StringFilter(sString, ...)
   ...
   sResult = CString.FormatResult(sMethod="", bSuccess=True, sResult="")

*CUtils*

.. code:: python

   from PythonExtensionsCollection.Utils.CUtils import *
   ...
   PrettyPrint(oData)

