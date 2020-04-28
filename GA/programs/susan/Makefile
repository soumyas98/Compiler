susan: susan.c Makefile
	gcc -o output/$(OUTPUT) susan.c -lm -O3 $(CFLAGS)

susan_O0: susan.c Makefile
	gcc -o output/susan_O0 susan.c -lm -O0

susan_O1: susan.c Makefile
	gcc -o output/susan_O1 susan.c -lm -O1

susan_O2: susan.c Makefile
	gcc -o output/susan_O2 susan.c -lm -O2

susan_O3: susan.c Makefile
	gcc -o output/susan_O3 susan.c -lm -O3

clean:
	rm -rf output/*
