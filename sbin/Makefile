# Makefile
#
# License: GPL
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.
#
all: sbin

sbin:
	ln -fs drbl-fuh drbl-cp
	ln -fs drbl-fuh drbl-cp-host
	ln -fs drbl-fuh drbl-host-cp

	ln -fs drbl-fuh drbl-get-host
	ln -fs drbl-fuh drbl-host-get

	ln -fs drbl-fuh drbl-host-rm
	ln -fs drbl-fuh drbl-rm-host

	ln -fs drbl-fuh drbl-fuh-put
	ln -fs drbl-fuh drbl-fuh-get
	ln -fs drbl-fuh drbl-fuh-rm

	ln -fs drbl-fuu drbl-cp-user
	ln -fs drbl-fuu drbl-user-cp

	ln -fs drbl-fuu drbl-rm-user
	ln -fs drbl-fuu drbl-user-rm

	ln -fs drbl-fuu drbl-get-user
	ln -fs drbl-fuu drbl-user-get

	ln -fs drbl-fuu drbl-fuu-put
	ln -fs drbl-fuu drbl-fuu-get
	ln -fs drbl-fuu drbl-fuu-rm

	ln -fs drbl-useradd-file  drbl-userdel-file
	ln -fs drbl-useradd-list  drbl-userdel-list
	ln -fs drbl-useradd-range drbl-userdel-range

	ln -fs drbl-client-switch dcs

clean:
	rm -f  drbl-cp
	rm -f  drbl-cp-host
	rm -f  drbl-host-cp

	rm -f  drbl-get-host
	rm -f  drbl-host-get

	rm -f  drbl-host-rm
	rm -f  drbl-rm-host

	rm -f  drbl-cp-user
	rm -f  drbl-user-cp

	rm -f  drbl-rm-user
	rm -f  drbl-user-rm

	rm -f  drbl-get-user
	rm -f  drbl-user-get

	rm -f  drbl-fuh-put
	rm -f  drbl-fuh-get
	rm -f  drbl-fuh-rm
	rm -f  drbl-fuu-put
	rm -f  drbl-fuu-get
	rm -f  drbl-fuu-rm
	rm -f  drbl-userdel-file
	rm -f  drbl-userdel-list
	rm -f  drbl-userdel-range

	rm -f  dcs
