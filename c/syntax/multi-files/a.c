#include <stdio.h>

typedef struct {
    char *name;
    int age;
} S;

void func(S *s) {
    printf("I am %d years old!\n", s->age);
}
