all: bash-lang perl-lang

bash-lang:
	( cd bash; \
	ln -fs de_DE de_DE.UTF-8; \
	ln -fs en_US en_US.UTF-8; \
	ln -fs it_IT it_IT.UTF-8; \
	ln -fs es_ES es_ES.UTF-8; \
	ln -fs pt_BR pt_BR.UTF-8; \
	ln -fs fr_FR fr_FR.UTF-8 )

perl-lang:
	( cd perl; \
	ln -fs de_DE de_DE.UTF-8; \
	ln -fs en_US en_US.UTF-8; \
	ln -fs it_IT it_IT.UTF-8; \
	ln -fs es_ES es_ES.UTF-8; \
	ln -fs pt_BR pt_BR.UTF-8; \
	ln -fs fr_FR fr_FR.UTF-8 )

clean:
	( cd bash; rm -f en_US.UTF-8 fr_FR.UTF-8 it_IT.UTF-8 es_ES.UTF-8 pt_BR.UTF-8 de_DE.UTF-8)
	( cd perl; rm -f en_US.UTF-8 fr_FR.UTF-8 it_IT.UTF-8 es_ES.UTF-8 pt_BR.UTF-8 de_DE.UTF-8)
