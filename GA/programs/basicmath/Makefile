FILE1 = basicmath_small.c   rad2deg.c  cubic.c   isqrt.c
FILE2 = basicmath_large.c   rad2deg.c  cubic.c   isqrt.c

all: basicmath_small basicmath_large

basicmath_small: ${FILE1} Makefile
	gcc ${FILE1} -o basicmath_small -lm -O3 $(CFLAGS)
basicmath_large: ${FILE2} Makefile
	gcc ${FILE2} -o basicmath_large -lm -O3 $(CFLAGS)

clean:
	rm -rf basicmath_small.exe basicmath_large.exe output*
