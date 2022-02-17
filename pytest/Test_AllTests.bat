@echo off
"%RobotPythonPath%/python.exe" -m pytest -k "not _Linux_" --show-capture=all --junitxml="./SessionInfo_AllTests.xml" "."
echo ------------------------------
echo pytest returned ERRORLEVEL : %ERRORLEVEL%
echo ------------------------------

