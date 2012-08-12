#!/bin/bash
# Steven Shiau <steven _at_ nchc org tw>
# License: GPL
# Description: To parse the /etc/apt/sourcesl.list and get the installed pacakge
# Usage: $0 PKGNAME
# Ex: $0 glibc

# Load DRBL setting and functions
DRBL_SCRIPT_PATH="${DRBL_SCRIPT_PATH:-/usr/share/drbl}"

. $DRBL_SCRIPT_PATH/sbin/drbl-conf-functions

#
usage() {
 echo Usage: $0 [OPTION] PKGNAME
 echo "OPTION:"
 echo " -a|--append DIRNAME  set the DIRNAME to append in the URL"
 echo " -r|--arch ARCH  set the search CPU type as ARCH (like i586, i686)"
 echo " -n|--no-specific-ver Do not match the running version."
 echo Ex: $0 -p RPMS.base -p RPMS.update -r i586 -n glibc
 echo "This will try to search the URL found in /etc/apt/sources.list with URL/RPMS.base and URL/RPMS.update, and the version no. is not important."
}

# option
DIRNAME=
while [ $# -gt 0 ]; do
  case "$1" in
    -a|--append)
            shift; DIRNAME="$DIRNAME $1"
	    if [ -z "$DIRNAME" ]; then
              usage >& 2
              exit 2
	    fi
	    shift;;
    -r|--arch)
            shift; arch="$1"
	    if [ -z "$arch" ]; then
              usage >& 2
              exit 2
	    fi
	    shift;;
    -n|--no-specific-ver)
            specivic_ver="no"
	    shift;;
    -*)	    echo "${0}: ${1}: invalid option" >&2
	    usage >& 2
	    exit 2 ;;
    *)	    break ;;
  esac
done
pkg=$1

[ -z "$pkg" ] && exit 0
[ -z "$arch" ] && exit 0

if [ "$specivic_ver" = "no" ]; then
  pkg_ver_filter="grep -iE ^${pkg}-[0-9]+"
else
  pkg_ver="$(rpm -q $pkg 2>/dev/null)"
  if [ -n "$pkg_ver" ]; then
   pkg_ver_filter="grep -iE ^$pkg_ver"
  else
   exit 2
  fi
fi
arch_filter="grep -iE ^.*.${arch}.rpm"

#
for im in $DIRNAME; do
  # it's like: rpm ftp://ftp.gwdg.de/pub/linux/suse/apt SuSE/9.3-i386 base
  url=$(grep -E "^[[:space:]]*rpm .* ${im/RPMS./}.*" /etc/apt/sources.list | awk -F" " '{print $2"/"$3}')
  for iurl in $url; do
   pkg_rpm="$(LC_ALL=C list_available_rpm $iurl/${im} | $pkg_ver_filter | $arch_filter)"
   if [ -n "$pkg_rpm" ];then
     echo "$iurl/${im}/$pkg_rpm"
     break
   fi
  done
   [ -n "$pkg_rpm" ] && break
done
