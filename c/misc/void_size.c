#include <stdio.h>

int main()
{
	// if you are using 32 bit CPU, it outputs 4
	// if you are using 64 bit CPU, it outputs 8
    printf("%d\n", sizeof(void *));
}
