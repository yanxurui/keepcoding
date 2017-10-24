#include <stdio.h>
#include <unistd.h>

static int a;
int main()
{
    int pid, i=0;
    for (i =0; i< 3; i++)
    {
        pid = fork();
        if (pid == 0)
        {
            printf("child: pid=%d, a=%d, addr=%p\n", getpid(), a, &a);
            a = i;
            printf("child: pid=%d, a=%d, addr=%p\n", getpid(), a, &a);
        }
        else if (pid < 0)
        {
            printf("error\n");
        }
    }
    sleep(1);
    return 0;
}
