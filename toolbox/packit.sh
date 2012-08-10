#!/bin/bash
# generate the ChangeLog.txt and create the tarball

set -e
#
VER="$(LC_ALL=C head -n 1 debian/changelog  | grep -i "^drbl" | grep -E -o "\(.*\)" | sed -r -e "s/\(//g" -e "s/\)//g" | cut -d"-" -f1)"
[ -z "$VER" ] && echo "No version found in debian/changelog! Program terminated!"
echo "VER: $VER"

#
cat <<EOF > doc/ChangeLog.txt
DRBL project.
Author: Steven Shiau <steven _at_ nchc org tw>, Blake, Kuo-Lien Huang (klhaung _at_ gmail com), Ceasar Sun (ceasar _at_ nchc org tw), Jazz Wang (jazz _at_ nchc org tw) and Thomas Tsai (thomas _at_ nchc org tw)
License: GPL
http://drbl.org
http://drbl.sourceforge.net
http://drbl.nchc.org.tw

EOF

cat debian/changelog >> doc/ChangeLog.txt

#
td=drbl"-""$VER"
[ -d "$td" ] && rm -rf $td
mkdir -p $td
# Clean stale files in debian
rm -rf debian/{drbl,tmp}
cp -ar Makefile drbl.spec sbin bin doc lang pkg scripts themes conf image pki setup prerun postrun $td/

echo $VER > $td/doc/VERSION.$VER
tar cvjf $td.tar.bz2 --owner=root --group=root $td
rm -rf $td
