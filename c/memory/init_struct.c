//https://stackoverflow.com/questions/330793/how-to-initialize-a-struct-in-accordance-with-c-programming-language-standards
#include <stdio.h>

typedef struct Item
{
    int a;
    float b;
    char* name;
} Item;

int main(void)
{
    Item item1 = { 5, 2.2, "George" };
    printf("item1: %d, %f, %s\n", item1.a, item1.b, item1.name);

    Item item2 = { .name="Mark", .b=2.3 };
    printf("item2: %d, %f, %s\n", item2.a, item2.b, item2.name);

    return 0;
}