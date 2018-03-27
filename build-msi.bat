@echo off

rd /s/q dist
rd /s/q build
del /f web-console.spec
del /f web-console.wixobj
del /f WebConsoleInstaller.msi
del /f WebConsoleInstaller.wixpdb

pyinstaller web_console/app.py -F --name web-console
copy /y config.ini dist\config.ini
copy /y cacert.pem dist\cacert.pem

"C:\Program Files (x86)\WiX Toolset v3.11\bin\candle.exe" -arch x86 web-console.wxs
"C:\Program Files (x86)\WiX Toolset v3.11\bin\Light.exe" -out "WebConsoleInstaller.msi" web-console.wixobj
