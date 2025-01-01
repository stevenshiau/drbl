#!/bin/bash
# generate the ChangeLog.txt and create the tarball

# Settings
PKG="drbl"
FILES_DIRS="Makefile drbl.spec sbin bin doc lang pkg scripts themes conf image pki setup prerun postrun"
# SPEC_FILE="$PKG.spec"

set -e
#
VER="$(LC_ALL=C head -n 1 debian/changelog  | grep -i "^${PKG}" | grep -E -o "\(.*\)" | sed -r -e "s/\(//g" -e "s/\)//g" | cut -d"-" -f1)"
[ -z "$VER" ] && echo "No version found in debian/changelog! Program terminated!"
echo "VER: $VER"
# RPM_VER=`grep ^Version $SPEC_FILE |sed -e "s/\t/ /g" -e "s/ \+/ /g" |cut  -d":" -f2 |tr -d " "`
# echo "RPM VER: $RPM_VER"
# if [ "$VER" != "$RPM_VER" ]; then
#   echo "Versions do not match!"
#   echo "Program terminated!"
#   exit 1
# fi

# Create the ChangeLog file
cat <<EOF > doc/ChangeLog.txt
DRBL project.
Authors: Steven Shiau <steven _at_ clonezilla org>, Blake, Kuo-Lien Huang (klhaung _at_ gmail com), Ceasar Sun (ceasar _at_ nchc org tw), Jazz Wang (jazz _at_ nchc org tw) and Thomas Tsai (thomas _at_ nchc org tw)
License: GPL
http://drbl.org
http://drbl.sourceforge.net
http://drbl.nchc.org.tw

EOF

cat debian/changelog >> doc/ChangeLog.txt

td="${PKG}-${VER}"

#
[ -d "$td" ] && rm -rf $td
mkdir -p $td
# Clean stale files in debian
cp -ar $FILES_DIRS $td/

echo $VER > $td/doc/VERSION
tar cJf $td.tar.xz --owner=root --group=root $td
rm -rf $td
