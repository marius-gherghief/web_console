#!/usr/bin/env bash

# Remove PyInstaller tmp files
rm -rf dist
rm -rf build
rm -f web-console.spec

# Remove dpkg-buildpackage tmp files
rm -f web-console_*.dsc
rm -f web-console_*.tar.gz
rm -f web-console_*.changes
rm -f web-console_*.deb

pyinstaller web_console/app.py -F --name web-console
cp -f config-sample.ini dist/
cp -f web-console.service dist/
cp -f cacert.pem dist/
cp -Rf debian dist/
(cd dist ; dpkg-buildpackage -us -uc)
