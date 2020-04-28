FILE1 = qsort_small.c
FILE2 = qsort_large.c

all: qsort_small qsort_large

qsort_small: qsort_small.c Makefile
	gcc qsort_small.c -o output/$(OUTPUT) -lm -O3 $(CFLAGS)
qsort_large: qsort_large.c Makefile
	gcc qsort_large.c -o output/$(OUTPUT) -lm -O3 $(CFLAGS)

qsort_small_O0: qsort_small.c Makefile
	gcc qsort_small.c -o output/qsort_small_O0 -lm -O0
qsort_small_O1: qsort_small.c Makefile
	gcc qsort_small.c -o output/qsort_small_O1 -lm -O1
qsort_small_O2: qsort_small.c Makefile
	gcc qsort_small.c -o output/qsort_small_O2 -lm -O2
qsort_small_O3: qsort_small.c Makefile
	gcc qsort_small.c -o output/qsort_small_O3 -lm -O3

qsort_large_O0: qsort_large.c Makefile
	gcc qsort_large.c -o output/qsort_large_O0 -lm -O0
qsort_large_O1: qsort_large.c Makefile
	gcc qsort_large.c -o output/qsort_large_O1 -lm -O1
qsort_large_O2: qsort_large.c Makefile
	gcc qsort_large.c -o output/qsort_large_O2 -lm -O2
qsort_large_O3: qsort_large.c Makefile
	gcc qsort_large.c -o output/qsort_large_O3 -lm -O3

clean:
	rm -rf output/*
