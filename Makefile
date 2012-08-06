# Makefile
#
# License: GPL
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.
#
SHELL := sh -e
DESTDIR =
SHAREDIR = /usr/share/drbl/

VISIBLE_COMMANDS = sbin/drblsrv

SCRIPTS = bin/* sbin/* share/bin/* $(SHAREDIR)/sbin/* $(SHAREDIR)/bin/*

all: drbl-sbin-link languages

test:
	@echo -n "Checking for syntax errors"

	@if [ -x /usr/bin/checkbashisms ]; \
	then \
		@echo -n "Checking for bashisms"
		for SCRIPT in $(SCRIPTS); \
		do \
			if [ -n "$(LC_ALL=C /usr/bin/file -L $${SCRIPT} | grep -i "Bourne-Again shell script text executable")" ]; then
				checkbashisms -f -x $${SCRIPT}; \
				echo -n "."; \
			fi
		done; \
	else \
		echo "WARNING: skipping bashism test - you need to install devscripts."; \
	fi

	@echo " done."

build:
	@echo "Nothing to build."

drbl-sbin-link:
	@echo "Files linking..."
	$(MAKE) -C sbin all

languages:
	@echo "Files linking..."
	$(MAKE) -C lang all

install:
	# install setup dir
	install -d $(DESTDIR)/$(SHAREDIR)/
	cp -a setup $(DESTDIR)/$(SHAREDIR)/
	# install other shared files
	cp -a scripts conf lang doc pkg pki image $(DESTDIR)/$(SHAREDIR)/
	install -d $(DESTDIR)/usr/
	cp -a sbin $(DESTDIR)/usr/
	cp -a bin $(DESTDIR)/usr//
	install -d $(DESTDIR)/etc/drbl/
	cp -a conf/* $(DESTDIR)/etc/drbl/
	# install themes
	install -d $(DESTDIR)/usr/share/gdm/themes/drbl-gdm
	cp -a themes/* $(DESTDIR)/usr/share/gdm/themes/drbl-gdm/
	# erase an extra COPYING
	rm -f $(DESTDIR)/$(SHAREDIR)/doc/COPYING

clean:
	$(MAKE) -C sbin clean
	$(MAKE) -C lang clean
