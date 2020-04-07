FILE1 = basicmath_small.c   rad2deg.c  cubic.c   isqrt.c
FILE2 = basicmath_large.c   rad2deg.c  cubic.c   isqrt.c

all: basicmath_small basicmath_large

basicmath_small: ${FILE1} Makefile
	gcc ${FILE1} -o output/$(OUTPUT) -lm -O3 $(CFLAGS)
basicmath_large: ${FILE2} Makefile
	gcc ${FILE2} -o output/$(OUTPUT) -lm -O3 $(CFLAGS)
basicmath_O1_small: ${FILE1} Makefile
	gcc ${FILE1} -o output/o1_small -lm -O1
basicmath_O2_small: ${FILE1} Makefile
	gcc ${FILE1} -o output/o2_small -lm -O2
basicmath_O3_small: ${FILE1} Makefile
	gcc ${FILE1} -o output/o3_small -lm -O3 
basicmath_NO_OP_small: ${FILE1} Makefile
	gcc ${FILE1} -o output/no_op_small -lm 

clean:
	rm -rf output/*
