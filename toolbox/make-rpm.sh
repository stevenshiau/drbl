#!/bin/bash
# Steven Shiau <steven _at_ nchc org tw)
#
PKG="drbl"
RPMBUILD="${HOME}/rpmbuild/"
SPEC_FILE="$PKG.spec"

#
set -e
#
[ ! -f "$SPEC_FILE" ] && echo "Can NOT find spec file $SPEC_FILE" && exit 1

#
VER=`grep ^Version $SPEC_FILE |sed -e "s/\t/ /g" -e "s/ \+/ /g" |cut  -d":" -f2 |tr -d " "`
RELEASE=`grep ^Release $SPEC_FILE |sed -e "s/\t/ /g" -e "s/ \+/ /g" |cut  -d":" -f2 |tr -d " "`
echo "VER, RELEASE: $VER, $RELEASE"

#
TARBALL=drbl-$VER.tar.bz2

# check
[ ! -f "$TARBALL" ] && echo "Can NOT find file $TARBALL! Did you forget to update the rdate in file drbl.spec ? Program Stop!!!" && exit 1

# mkdir for build
mkdir -p $RPMBUILD/SOURCES/$PKG-$VER

cp -f $TARBALL $RPMBUILD/SOURCES/$PKG-$VER/
rpmbuild -ba $SPEC_FILE

#
[ -d RPMS.drbl-test ] && rm -rf RPMS.drbl-test
mkdir RPMS.drbl-test
cp -v $RPMBUILD/SRPMS/$PKG-$VER-$RELEASE.src.rpm $RPMBUILD/RPMS/$PKG-$VER-$RELEASE.*.rpm RPMS.drbl-test
[ ! -d old ] && mkdir old
cp -af $TARBALL RPMS.drbl-test
#mv -f $TARBALL old
cp -fv doc/{GPL,ChangeLog.txt,RELEASE-NOTES,Known_issues*.txt} RPMS.drbl-test
