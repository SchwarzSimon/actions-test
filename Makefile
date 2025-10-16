main: main.c
	gcc -Wall -O2 main.c -o main

test: main
	./main

clean:
	rm -f main