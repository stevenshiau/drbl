#!/bin/bash
# Steven Shiau <steven _at_ nchc org tw)
#

set -e
PKG="drbl"
#
VER="$(LC_ALL=C head -n 1 debian/changelog  | grep -i "^drbl" | grep -E -o "\(.*\)" | sed -r -e "s/\(//g" -e "s/\)//g" | cut -d"-" -f1)"
[ -z "$VER" ] && echo "No version found in debian/changelog! Program terminated!"
echo "VER: $VER"

#
TARBALL=${PKG}-${VER}.tar.bz2
TARBALL_ORIG=${PKG}_${VER}.orig.tar.bz2

# check
[ ! -f "$TARBALL" ] && echo "Can NOT find file $TARBALL! Did you forget to update the rdate in file drbl.spec ? Program Stop!!!" && exit 1

# mkdir for build
rm -rf debforge 
mkdir debforge
(cd debforge; ln -fs ../$TARBALL $TARBALL_ORIG)
tar -xvjf $TARBALL -C debforge/
cp -a debian debforge/drbl-$VER/
cd debforge/drbl-$VER
debuild --no-tgz-check --no-lintian
rm -f $TARBALL_ORIG
