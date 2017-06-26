// https://stackoverflow.com/questions/330793/how-to-initialize-a-struct-in-accordance-with-c-programming-language-standards
#include <stdio.h>

typedef struct
{
   int id;
   char* name;
   int age;
}employee;


int main()
{
    // If you don't initialize the values in your struct, all variables will contain "garbage values".
    employee emp0;
    printf("%d,%s,%d\n", emp0.id, emp0.name, emp0.age);

    // In contrast, you initialize even one object/variable in the struct,
    // all of its other variables will be initialized to default value.

    // designated initializer(C99)
    employee emp1 = {.id=1, .name="foo"};
    printf("%d,%s,%d\n", emp1.id, emp1.name, emp1.age);

    employee emp2;
    emp2 = (employee){.id=2, .name="bar"};
    printf("%d,%s,%d\n", emp2.id, emp2.name, emp2.age);

    employee emp3;
    emp3 = (employee){3, "baz"};
    printf("%d,%s,%d\n", emp3.id, emp3.name, emp3.age);

    // C 89
    employee emp4 = {100, "Tom"};
    printf("%d,%s,%d\n", emp4.id, emp4.name, emp4.age);


    return 0;
}