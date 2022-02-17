@echo off
"%ROBOTPYTHONPATH%/python.exe" -m pytest -k "not _Linux_" --show-capture=all --junitxml="./SessionInfo.xml" "./test_CString.py"
echo ------------------------------
echo pytest returned ERRORLEVEL : %ERRORLEVEL%
echo ------------------------------

