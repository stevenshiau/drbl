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
	ln -fs ca_ES ca_ES.UTF-8; \
	ln -fs cs_CZ cs_CZ.UTF-8; \
	ln -fs de_DE de_DE.UTF-8; \
	ln -fs el_GR.UTF-8 el_GR; \
	ln -fs en_US en_US.UTF-8; \
	ln -fs es_ES es_ES.UTF-8; \
	ln -fs fr_FR fr_FR.UTF-8; \
	ln -fs hu_HU hu_HU.UTF-8; \
	ln -fs id_ID id_ID.UTF-8; \
	ln -fs it_IT it_IT.UTF-8; \
	ln -fs ja_JP.UTF-8 ja_JP; \
	ln -fs ko_KR.UTF-8 ko_KR; \
	ln -fs nl_NL nl_NL.UTF-8; \
	ln -fs pl_PL pl_PL.UTF-8; \
	ln -fs pt_BR pt_BR.UTF-8; \
	ln -fs ru_RU.UTF-8 ru_RU; \
	ln -fs sk_SK sk_SK.UTF-8; \
	ln -fs th_TH th_TH.UTF-8; \
	ln -fs tr_TR tr_TR.UTF-8; \
	ln -fs uk_UA uk_UA.UTF-8; \
	ln -fs vi_VN vi_VN.UTF-8; \
	ln -fs zh_CN.UTF-8 zh_CN; \
	ln -fs zh_TW.UTF-8 zh_TW)

perl-lang:
	( cd perl; \
	ln -fs ca_ES ca_ES.UTF-8; \
	ln -fs cs_CZ cs_CZ.UTF-8; \
	ln -fs de_DE de_DE.UTF-8; \
	ln -fs el_GR.UTF-8 el_GR; \
	ln -fs en_US en_US.UTF-8; \
	ln -fs es_ES es_ES.UTF-8; \
	ln -fs fr_FR fr_FR.UTF-8; \
	ln -fs hu_HU hu_HU.UTF-8; \
	ln -fs id_ID id_ID.UTF-8; \
	ln -fs it_IT it_IT.UTF-8; \
	ln -fs ja_JP.UTF-8 ja_JP; \
	ln -fs ko_KR.UTF-8 ko_KR; \
	ln -fs nl_NL nl_NL.UTF-8; \
	ln -fs pl_PL pl_PL.UTF-8; \
	ln -fs pt_BR pt_BR.UTF-8; \
	ln -fs ru_RU.UTF-8 ru_RU; \
	ln -fs sk_SK sk_SK.UTF-8; \
	ln -fs th_TH th_TH.UTF-8; \
	ln -fs tr_TR tr_TR.UTF-8; \
	ln -fs uk_UA uk_UA.UTF-8; \
	ln -fs vi_VN vi_VN.UTF-8; \
	ln -fs zh_CN.UTF-8 zh_CN; \
	ln -fs zh_TW.UTF-8 zh_TW)

check:
	( cd bash; LANG=en_US.UTF-8 ./check-bash-lang )
	( cd perl; LANG=en_US.UTF-8 ./check-perl-lang )

clean:
	( cd bash; rm -f ca_ES.UTF-8 cs_CZ.UTF-8 de_DE.UTF-8 el_GR en_US.UTF-8 es_ES.UTF-8 fr_FR.UTF-8 hu_HU.UTF-8 id_ID.UTF-8 it_IT.UTF-8 ja_JP ko_KR nl_NL.UTF-8 pl_PL.UTF-8 pt_BR.UTF-8 ru_RU sk_SK.UTF-8 th_TH.UTF-8 tr_TR.UTF-8 uk_UA.UTF-8 vi_VN.UTF-8 zh_CN zh_TW )
	( cd perl; rm -f ca_ES.UTF-8 cs_CZ.UTF-8 de_DE.UTF-8 el_GR en_US.UTF-8 es_ES.UTF-8 fr_FR.UTF-8 hu_HU.UTF-8 id_ID.UTF-8 it_IT.UTF-8 ja_JP ko_KR nl_NL.UTF-8 pl_PL.UTF-8 pt_BR.UTF-8 ru_RU sk_SK.UTF-8 th_TH.UTF-8 tr_TR.UTF-8 uk_UA.UTF-8 vi_VN.UTF-8 zh_CN zh_TW )

.PHONY: all bash-lang perl-lang check clean
