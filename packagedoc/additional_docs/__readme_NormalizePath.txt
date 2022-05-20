**************************************************************************************************************

Additional hints to Python function 'normpath':

28.10.2021

--------------------------------------------------------------------------------------------------------------

Python provides at least two implementations of 'normpath':

1.) os.path.normpath
2.) ntpath.normpath

The results of the first implementation (os.path.normpath) are different in Windows and Linux.

Therefore the implementation of CString::NormalizePath uses the second implementation (ntpath.normpath).

Purpose: collapse redundant separators and up-level references.

Both implementations are not able to handle the separators of web addresses and local network resource paths.

Therefore additional steps are necessary in CString::NormalizePath to solve this problem.

--------------------------------------------------------------------------------------------------------------

Below listings:
- Example test code
- Windows console output
- Linux console output

--------------------------------------------------------------------------------------------------------------

Example test code:
==================

print()
sPathIn   = r"\\server.com\\abc//xyz\mno/..\\xyz2"
sPathOut1 = os.path.normpath(sPathIn)
sPathOut2 = ntpath.normpath(sPathIn)
print(f"* In : {sPathIn}")
print(f"Out1 : {sPathOut1}")
print(f"Out2 : {sPathOut2}")
print()
sPathIn   = r"//server.com\\abc//xyz\mno/..\\xyz2"
sPathOut1 = os.path.normpath(sPathIn)
sPathOut2 = ntpath.normpath(sPathIn)
print(f"* In : {sPathIn}")
print(f"Out1 : {sPathOut1}")
print(f"Out2 : {sPathOut2}")
print()
sPathIn   = r"\\\server.com\\abc//xyz\mno/..\\xyz2"
sPathOut1 = os.path.normpath(sPathIn)
sPathOut2 = ntpath.normpath(sPathIn)
print(f"* In : {sPathIn}")
print(f"Out1 : {sPathOut1}")
print(f"Out2 : {sPathOut2}")
print()
sPathIn   = r"///server.com\\abc//xyz\mno/..\\xyz2"
sPathOut1 = os.path.normpath(sPathIn)
sPathOut2 = ntpath.normpath(sPathIn)
print(f"* In : {sPathIn}")
print(f"Out1 : {sPathOut1}")
print(f"Out2 : {sPathOut2}")
print()
sPathIn   = r"https:\\server.com\\abc//xyz\mno/..\\xyz2"
sPathOut1 = os.path.normpath(sPathIn)
sPathOut2 = ntpath.normpath(sPathIn)
print(f"* In : {sPathIn}")
print(f"Out1 : {sPathOut1}")
print(f"Out2 : {sPathOut2}")
print()
sPathIn   = r"https://server.com\\abc//xyz\mno/..\\xyz2"
sPathOut1 = os.path.normpath(sPathIn)
sPathOut2 = ntpath.normpath(sPathIn)
print(f"* In : {sPathIn}")
print(f"Out1 : {sPathOut1}")
print(f"Out2 : {sPathOut2}")
print()

--------------------------------------------------------------------------------------------------------------

Windows console output:
=======================

* In : \\server.com\\abc//xyz\mno/..\\xyz2
Out1 : \server.com\abc\xyz\xyz2
Out2 : \server.com\abc\xyz\xyz2

* In : //server.com\\abc//xyz\mno/..\\xyz2
Out1 : \server.com\abc\xyz\xyz2
Out2 : \server.com\abc\xyz\xyz2

* In : \\\server.com\\abc//xyz\mno/..\\xyz2
Out1 : \server.com\abc\xyz\xyz2
Out2 : \server.com\abc\xyz\xyz2

* In : ///server.com\\abc//xyz\mno/..\\xyz2
Out1 : \server.com\abc\xyz\xyz2
Out2 : \server.com\abc\xyz\xyz2

* In : https:\\server.com\\abc//xyz\mno/..\\xyz2
Out1 : https:\server.com\abc\xyz\xyz2
Out2 : https:\server.com\abc\xyz\xyz2

* In : https://server.com\\abc//xyz\mno/..\\xyz2
Out1 : https:\server.com\abc\xyz\xyz2
Out2 : https:\server.com\abc\xyz\xyz2

--------------------------------------------------------------------------------------------------------------

Linux console output:
=====================

* In : \\server.com\\abc//xyz\mno/..\\xyz2
Out1 : \\server.com\\abc/xyz\mno/..\\xyz2
Out2 : \server.com\abc\xyz\xyz2

* In : //server.com\\abc//xyz\mno/..\\xyz2
Out1 : //server.com\\abc/xyz\mno/..\\xyz2
Out2 : \server.com\abc\xyz\xyz2

* In : \\\server.com\\abc//xyz\mno/..\\xyz2
Out1 : \\\server.com\\abc/xyz\mno/..\\xyz2
Out2 : \server.com\abc\xyz\xyz2

* In : ///server.com\\abc//xyz\mno/..\\xyz2
Out1 : /server.com\\abc/xyz\mno/..\\xyz2
Out2 : \server.com\abc\xyz\xyz2

* In : https:\\server.com\\abc//xyz\mno/..\\xyz2
Out1 : https:\\server.com\\abc/xyz\mno/..\\xyz2
Out2 : https:\server.com\abc\xyz\xyz2

* In : https://server.com\\abc//xyz\mno/..\\xyz2
Out1 : https:/server.com\\abc/xyz\mno/..\\xyz2
Out2 : https:\server.com\abc\xyz\xyz2

--------------------------------------------------------------------------------------------------------------




