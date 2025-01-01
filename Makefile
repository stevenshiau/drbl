# Makefile
#
# License: GPL
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.
#
SHELL := bash -e
DESTDIR =
SHAREDIR = /usr/share/drbl/

SCRIPTS = bin/* sbin/* $(SHAREDIR)/sbin/* $(SHAREDIR)/bin/*

all: drbl-sbin-link languages pkg-misc

build:
	@echo "Nothing to build."

drbl-sbin-link:
	@echo "Files linking..."
	$(MAKE) -C sbin all

languages:
	@echo "Files linking..."
	$(MAKE) -C lang all

pkg-misc:
	@echo "Files in pkg-misc..."
	$(MAKE) -C pkg/misc all

install:
	# install exec files
	install -d $(DESTDIR)/usr/
	cp -a sbin bin $(DESTDIR)/usr/
	rm -f $(DESTDIR)/usr/sbin/Makefile
	# install setup dir
	install -d $(DESTDIR)/$(SHAREDIR)/
	cp -a setup $(DESTDIR)/$(SHAREDIR)/
	# install other shared files
	cp -a lang doc pkg pki image prerun postrun scripts/sbin scripts/bin $(DESTDIR)/$(SHAREDIR)/
	# erase an extra COPYING
	rm -f $(DESTDIR)/$(SHAREDIR)/pkg/misc/COPYING
	rm -f $(DESTDIR)/$(SHAREDIR)/pkg/misc/Makefile $(DESTDIR)/$(SHAREDIR)/lang/Makefile
	# install config files
	install -d $(DESTDIR)/etc/drbl/
	cp -a conf/* $(DESTDIR)/etc/drbl/
	# install themes
	install -d $(DESTDIR)/usr/share/gdm/themes/drbl-gdm
	cp -a themes/* $(DESTDIR)/usr/share/gdm/themes/drbl-gdm/

clean:
	$(MAKE) -C sbin clean
	$(MAKE) -C lang clean
