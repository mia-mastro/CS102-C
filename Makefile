TARGET = puzzles
CC = gcc
CFLAGS = -Wall -g

$(TARGET): main.o puzzles.o
	$(CC) $(CFLAGS) -o $(TARGET) main.o puzzles.o

main.o: main.c puzzles.h
	$(CC) $(CFLAGS) -c main.c

puzzles.o: puzzles.c puzzles.h
	$(CC) $(CFLAGS) -c puzzles.c

clean:
	rm -f *.o $(TARGET)
