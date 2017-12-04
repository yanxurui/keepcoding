SRC = $(wildcard *.c)
BIN = $(SRC:.c=)

.PHONY: all clean

all: $(BIN)

clean:
	rm -rf $(BIN)

%.out: %.c
	$(CC) -o $@ $<
