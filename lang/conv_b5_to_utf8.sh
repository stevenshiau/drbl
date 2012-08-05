#!/bin/bash
file2do="$1"
[ -z "$file2do" ] && echo "No file specified! Program stop" && exit 1
[ ! -e "$file2do" ] && echo "$file2do not found!" && exit 1
prefix=`echo $file2do | sed -e "s/\.BIG5//g"`
target_fn=$prefix.UTF-8
iconv -f BIG5 -t UTF-8 -o $target_fn $file2do
