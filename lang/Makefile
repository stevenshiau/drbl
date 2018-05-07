# Makefile
#
# License: GPL
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.
#
all: bash-lang perl-lang

bash-lang:
	( cd bash; \
	ln -fs de_DE de_DE.UTF-8; \
	ln -fs en_US en_US.UTF-8; \
	ln -fs hu_HU hu_HU.UTF-8; \
	ln -fs it_IT it_IT.UTF-8; \
	ln -fs ca_ES ca_ES.UTF-8; \
	ln -fs es_ES es_ES.UTF-8; \
	ln -fs pl_PL pl_PL.UTF-8; \
	ln -fs pt_BR pt_BR.UTF-8; \
	ln -fs sk_SK sk_SK.UTF-8; \
	ln -fs tr_TR tr_TR.UTF-8; \
	ln -fs fr_FR fr_FR.UTF-8 )

perl-lang:
	( cd perl; \
	ln -fs de_DE de_DE.UTF-8; \
	ln -fs en_US en_US.UTF-8; \
	ln -fs hu_HU hu_HU.UTF-8; \
	ln -fs it_IT it_IT.UTF-8; \
	ln -fs ca_ES ca_ES.UTF-8; \
	ln -fs es_ES es_ES.UTF-8; \
	ln -fs pl_PL pl_PL.UTF-8; \
	ln -fs pt_BR pt_BR.UTF-8; \
	ln -fs sk_SK sk_SK.UTF-8; \
	ln -fs tr_TR tr_TR.UTF-8; \
	ln -fs fr_FR fr_FR.UTF-8 )

clean:
	( cd bash; rm -f en_US.UTF-8 fr_FR.UTF-8 hu_HU.UTF-8 it_IT.UTF-8 ca_ES.UTF-8 es_ES.UTF-8 pl_PL.UTF-8 pt_BR.UTF-8 de_DE.UTF-8 sk_SK.UTF-8 tr_TR.UTF-8)
	( cd perl; rm -f en_US.UTF-8 fr_FR.UTF-8 hu_HU.UTF-8 it_IT.UTF-8 ca_ES.UTF-8 es_ES.UTF-8 pl_PL.UTF-8 pt_BR.UTF-8 de_DE.UTF-8 sk_SK.UTF-8 tr_TR.UTF-8)
