#include <stdio.h>
#include <unistd.h>

int main()
{
    char buf[20];
    gethostname(buf, 20);
    printf(buf);
}
