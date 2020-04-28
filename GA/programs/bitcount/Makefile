FILE = bitcnt_1.c bitcnt_2.c bitcnt_3.c bitcnt_4.c bitcnts.c bitfiles.c bitstrng.c bstr_i.c 

bitcnts: ${FILE} Makefile
	gcc ${FILE} -o output/$(OUTPUT) -lm -O3 $(CFLAGS)
bitcnts_O0: ${FILE} Makefile
	gcc ${FILE} -o output/bitcnts_O0 -lm -O0
bitcnts_O1: ${FILE} Makefile
	gcc ${FILE} -o output/bitcnts_O1 -lm -O1
bitcnts_O2: ${FILE} Makefile
	gcc ${FILE} -o output/bitcnts_O2 -lm -O2
bitcnts_O3: ${FILE} Makefile
	gcc ${FILE} -o output/bitcnts_O3 -lm -O3

clean:
	rm -rf output/*
