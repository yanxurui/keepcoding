// https://stackoverflow.com/questions/18749349/finding-offset-of-a-structure-element-in-c
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

int
main(void)
{
   struct s {
       int i;
       char c;
       double d;
       char a[];
   };

   /* Output is compiler dependent */

   printf("offsets: i=%ld; c=%ld; d=%ld a=%ld\n",
           (long) offsetof(struct s, i),
           (long) offsetof(struct s, c),
           (long) offsetof(struct s, d),
           (long) offsetof(struct s, a));
   printf("sizeof(struct s)=%ld\n", (long) sizeof(struct s));

   // 指向成员的运算符->的优先级比取地址运算符&高
   printf("%p\n", &((struct s *)NULL)->a);
   
   exit(EXIT_SUCCESS);
}