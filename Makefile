main: y.tab.o lex.yy.o
	gcc -o parser lex.yy.o y.tab.o -ly 

y.tab.o: y.tab.c
	gcc -c y.tab.c

y.tab.c: src/main.yacc
	yacc -d src/main.yacc

lex.yy.o: lex.yy.c
	gcc -c lex.yy.c

lex.yy.c: src/main.lex
	lex src/main.lex

clean:
	rm -rf lex.yy.c y.tab.c y.tab.h *.o parser
