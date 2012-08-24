#!/bin/bash
file2do="$1"
[ -z "$file2do" ] && echo "No file specified! Program stop" && exit 1
[ ! -e "$file2do" ] && echo "$file2do not found!" && exit 1
prefix=`echo $file2do | sed -e "s/\.UTF-8//g"`
target_fn=$prefix.BIG5
iconv -f UTF-8 -t BIG5 -o $target_fn $file2do
