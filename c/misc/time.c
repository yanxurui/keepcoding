#include <stdio.h>
#include <time.h>

int main()
{
    time_t t = time(NULL); // time stamp
    printf("%s", ctime(&t));
    return 0;
}