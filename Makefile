CC = gcc
CFLAGS = -Wall -Wextra -std=c99

TARGET = parser
OBJS = csv_parser.o parser.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

csv_parser.o: csv_parser.c csv_parser.h
	$(CC) $(CFLAGS) -c csv_parser.c

parser.o: parser.c csv_parser.h
	$(CC) $(CFLAGS) -c parser.c

clean:
	rm -f $(OBJS) $(TARGET)
