#!/usr/bin/env bash

rm -rf dist
rm -rf build
rm -f web-console.spec
rm -f web-console_*.dsc
rm -f web-console_*.tar.gz
rm -f web-console_*.changes
rm -f web-console_*.deb

pyinstaller web_console/app.py -F --name web-console
cp -f config.ini dist/
cp -f web-console.service dist/
cp -f cacert.pem dist/
cp -Rf debian dist/
(cd dist ; dpkg-buildpackage -us -uc)
