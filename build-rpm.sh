#!/usr/bin/env bash

# Remove PyInstaller tmp files
rm -rf dist
rm -rf build
rm -f web-console.spec

# Remove dpkg-buildpackage tmp files
pyinstaller web_console/app.py -F --name web-console
cp -f config-sample.ini dist/
cp -f web-console.service dist/
cp -f cacert.pem dist/

tar -czvf web-console.tar.gz dist/

# mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp -Rf rpmbuild dist/
echo '%_topdir %(echo $PWD)/dist/rpmbuild' > ~/.rpmmacros


(cd dist/rpmbuild/SPECS ; rpmbuild -ba web-console.spec)
