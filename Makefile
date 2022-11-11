All: $(HOME)/.forward smua extractcontent spool
	@sleep 1
	touch All

$(HOME)/.forward: forward.template
	cat forward.template | sed "s:HOMEDIR:$(HOME):g" > $(HOME)/.forward

smua: smua.c
	gcc -DSMUA_SUBDIR='"port25relay/spool"' -o smua smua.c

smua.c:

extractcontent: extractcontent.c
	gcc -o extractcontent extractcontent.c

extractcontent.c:

spool:
	mkdir spool
