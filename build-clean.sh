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

