#!/bin/bash

# To deploy testing codes , Via Ceasar Sun

[ "$UID" != "0" ] && echo "Need ROOT privilege. Run 'sudo $0' !" && exit 0;

[ ! -e "./.git/config" ] && echo "Not found ~drbl-core.cb  ?" && exit 1;

rsync -avP conf/drbl.conf /etc/drbl/drbl.conf
rsync -avP sbin/drblsrv /usr/sbin/drblsrv
rsync -avP sbin/drblpush /usr/sbin/drblpush
rsync -avP sbin/drbl-login-switch  /usr/sbin/drbl-login-switch
rsync -avP scripts/sbin/drbl-functions /usr/share/drbl/sbin/drbl-functions
rsync -avP setup/files/misc/init.drbl /usr/share/drbl/setup/files/misc/init.drbl
rsync -avP setup/files/DBN/DBN-TU/firstboot.DBN-TU.drbl /usr/share/drbl/setup/files/DBN/DBN-TU/firstboot.DBN-TU.drbl
rsync -avP setup/files/LinuxMint /usr/share/drbl/setup/files/

exit 0
