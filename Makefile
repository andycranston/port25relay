All: $(HOME)/.forward smua spool
	@sleep 1
	touch All

$(HOME)/.forward: forward.template
	cat forward.template | sed "s:HOMEDIR:$(HOME):g" > $(HOME)/.forward

smua: smua.c
	gcc -DSMUA_SUBDIR='"port25relay/spool"' -o smua smua.c

spool:
	mkdir spool
