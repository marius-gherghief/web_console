#!/usr/bin/env bash

# Remove PyInstaller tmp files
rm -rf dist
rm -rf build
rm -f web-console.spec

pyinstaller web_console/app.py -F --name web-console
cp -f config.ini dist/
cp -f web-console.service dist/
cp -f cacert.pem dist/
cp -f debian/postinst dist/
cp -f web_console/VERSION dist/

version=`cat web_console/VERSION`
mkdir dist/tmp-build

find dist/ ! -regex "dist/tmp-build/.*" ! -regex "dist/tmp-build" ! -regex 'dist/' -exec mv '{}' "dist/tmp-build" \;
mv dist/tmp-build dist/web-console
(cd dist ; zip -r "web-console-$version.zip" "web-console")