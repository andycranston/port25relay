All: $(HOME)/.forward smua
	@sleep 1
	touch All

$(HOME)/.forward: forward.template
	cat forward.template | sed "s:HOMEDIR:$(HOME):g" > $(HOME)/.forward

smua: smua.c
	gcc -o smua smua.c
