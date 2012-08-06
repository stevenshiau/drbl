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

SCRIPTS = bin/* sbin/* $(SHAREDIR)/sbin/* $(SHAREDIR)/bin/*

all: drbl-sbin-link languages fail-mbr

build:
	@echo "Nothing to build."

drbl-sbin-link:
	@echo "Files linking..."
	$(MAKE) -C sbin all

fail-mbr:
	@echo "Creating fail-mbr.bin..."
	$(MAKE) -C pkg/misc all

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
