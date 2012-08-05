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
			if [ -n "$(LC_ALL=C file -L $${SCRIPT} | grep -i "Bourne-Again shell script text executable")" ]; then
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
	cp -a setup $(DESTDIR)/$(SHAREDIR)/setup/
	# install other shared files
	cp -a scripts conf lang doc pkg pki image $(DESTDIR)/$(SHAREDIR)/
	cp -a sbin/* $(DESTDIR)/usr/sbin/
	cp -a bin/* $(DESTDIR)/usr/bin/
	install -d $(DESTDIR)/etc/drbl/
	cp -a conf/* $(DESTDIR)/etc/drbl/
	# install themes
	install -d $(DESTDIR)/usr/share/gdm/themes/drbl-gdm
	cp -a themes/* $(DESTDIR)/usr/share/gdm/themes/drbl-gdm/
	# fix erased files which should be useful
	ln -s /usr/bin/ipcalc       $(DESTDIR)/$(SHAREDIR)/bin/drbl-ipcalc
	ln -s /usr/bin/wakeonlan    $(DESTDIR)/$(SHAREDIR)/bin/drbl-wakeonlan
	ln -s /usr/bin/isohybrid.pl $(DESTDIR)/$(SHAREDIR)/bin/isohybrid
	ln -s /usr/bin/sha1pass     $(DESTDIR)/$(SHAREDIR)/bin/drbl-sha1pass
	# erase an extra COPYING
	rm -f $(DESTDIR)/$(SHAREDIR)/doc/COPYING
	# fix wrong interpreter path
	for f in $$(find $(DESTDIR)/$(SHAREDIR)/setup -name "linuxrc*drbl"); do\
	  sed -e 's%#!/static/ash%#!/bin/ash%'  -e 's%#!/static/sh%#!/bin/sh%' $$f > $$f.tmp && mv $$f.tmp $$f; \
	done
	# fix executable flags
	for f in $$(find $(DESTDIR)/$(SHAREDIR)/lang -type f); do \
	  if grep -q '#!/bin/.*sh' $$f; then chmod +x $$f; fi; \
	done
	for f in $$(find $(DESTDIR)/$(SHAREDIR)/sbin \
	                 $(DESTDIR)/$(SHAREDIR)/bin \
	                 $(DESTDIR)/$(SHAREDIR)/setup ); \
	do \
	  if [ -f $$f ] && head -n 1 $$f | grep -q /bin/bash; then \
	    chmod +x $$f; \
	  fi; \
	done
	chmod -x $(DESTDIR)/$(SHAREDIR)/sbin/drbl*functions
	for f in $$(find $(DESTDIR)/$(SHAREDIR)/setup -name "*drbl"); do \
	  chmod +x $$f; \
	  echo "+x : $$f"; \
	done
	# remove the interpreter's magic number
	for f in $(DESTDIR)/$(SHAREDIR)/sbin/drbl-perl-functions; do \
	  tail -n +2 $$f > $$f.tmp && mv $$f.tmp $$f; \
	done
	# create symlinks to configuration files
	mkdir -p $(DESTDIR)/$(SHAREDIR)/conf
	ln -s /etc/drbl/drbl.conf $(DESTDIR)/$(SHAREDIR)/conf

	# Installing shared data
	# Installing executables
	# Installing documentation
	# Installing manpages
clean:
	$(MAKE) -C sbin clean
	$(MAKE) -C lang clean
	# erase files which are available in other packages
	cd bin; rm -f drbl-ipcalc drbl-wakeonlan isohybrid drbl-sha1pass \
	  list_available* list_latest* pkg-ver-latest
