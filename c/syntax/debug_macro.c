// https://stackoverflow.com/questions/13892191/empty-macro-definition-in-c
// gcc debug_macro.c -DDEBUG
#include <stdio.h>

#ifdef DEBUG
#define DEBUG_MSG(x) printf("%s\n", x)
#else
#define DEBUG_MSG(x) do {} while(0)
#endif

int main(){
    DEBUG_MSG("Entering main");
    printf("Hello world\n");
}