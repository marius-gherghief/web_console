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

version=`cat web_console/VERSION`
dist_folder = "dist/web-console-$version"

mv "!($dist_folder) $dist_folder"

(cd dist ; zip -r "web-console-$version.zip $dist_folder")
