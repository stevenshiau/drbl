#!/bin/bash
# Steven Shiau <steven _at_ nchc org tw)
#
PKG="drbl"
SPEC_FILE="$PKG.spec"

set -e
#
[ ! -f "$SPEC_FILE" ] && echo "Can NOT find spec file $SPEC_FILE" && exit 1

#
VER=`grep ^Version $SPEC_FILE |sed -e "s/\t/ /g" -e "s/ \+/ /g" |cut  -d":" -f2 |tr -d " "`
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
