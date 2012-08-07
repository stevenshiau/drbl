#!/bin/bash
# generate the ChangeLog.txt from drbl.spec
SPEC_FILE="drbl.spec"

set -e
#
[ ! -e "$SPEC_FILE" ] && exit 1
[ -f "doc/ChangeLog.txt" ] && rm -f doc/ChangeLog.txt
line_begin="$(grep -n "%changelog" $SPEC_FILE | awk -F":" '{print $1}')"
line_eng="$(wc -l $SPEC_FILE | awk -F" " '{print $1}')"
lines=$(($line_eng - $line_begin))
cat <<EOF > doc/ChangeLog.txt
DRBL for Debian/Ubuntu/RedHat/Fedora/CentOS/SuSE
Author: Steven Shiau <steven _at_ nchc org tw>, Blake, Kuo-Lien Huang (klhaung _at_ gmail com), H. T. Wang (c00wht00 _at_ nchc org tw), Ceasar Sun (ceasar _at_ nchc org tw), Jazz Wang (jazz _at_ nchc org tw) and Thomas Tsai (thomas _at_ nchc org tw)
License: GPL
http://drbl.org
http://drbl.nchc.org.tw
http://drbl.sourceforge.net

EOF

tail -n $lines $SPEC_FILE >> doc/ChangeLog.txt

#
VER=`grep ^Version $SPEC_FILE |sed -e "s/\t/ /g" -e "s/ \+/ /g" |cut  -d":" -f2 |tr -d " "`
echo "VER: $VER"

#
td=drbl"-""$VER"
[ -d "$td" ] && rm -rf $td
mkdir -p $td
# Clean stale files in debian
rm -rf debian/{drbl,tmp}
cp -r Makefile drbl.spec sbin bin doc lang pkg scripts themes conf image pki setup prerun postrun $td/

echo $VER > $td/doc/VERSION.$VER
tar cvjf $td.tar.bz2 --owner=root --group=root $td
rm -rf $td
