ALL: zturnSoft.exe

zturnSoft.exe: ./bin/main.o ./bin/matlablite.o
		gcc -o zturnSoft.exe ./bin/main.o ./bin/matlablite.o -lm
./bin/main.o : main.c
	gcc -o ./bin/main.o -c main.c 
./bin/matlablite.o : matlablite.c
	gcc -o ./bin/matlablite.o -c matlablite.c 


clean:
	rd bin
mrpropoer: clean
	rm -rf zturnSoft.exe
