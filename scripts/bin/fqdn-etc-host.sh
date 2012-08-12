#!/bin/bash
# Author: Steven Shiau <steven _at_ nchc org tw>
# License: GPL

# Load DRBL setting and functions
DRBL_SCRIPT_PATH="${DRBL_SCRIPT_PATH:-/usr/share/drbl}"

. $DRBL_SCRIPT_PATH/sbin/drbl-conf-functions

#
eth_wan_port="$1"
[ -z "$eth_wan_port" ] && exit 1
eth_wan_ip="$(drbl-get-ipadd $eth_wan_port)"

# authough RH-like hostname will give FQDN name, but it is not in Debian.
hostnm="$(hostname | cut -d"." -f1)"
dnsdomainnm="$(dnsdomainname)"
fqdn="$hostnm.$dnsdomainnm"
echo "$eth_wan_ip $fqdn $hostnm"
