#include<stdio.h>
#include <limits.h>

int reverse(int x)
{
    printf("%d\n", INT_MAX);
    printf("%d\n", INT_MIN);

    int r = 0;
    while (x != 0)
    {
        if ((r > (INT_MAX / 10)) || (r < (INT_MIN / 10)))
        {
            printf("%d\n", r);
            return 0;
        }

        r = r * 10 + x % 10;
        x = x / 10;
    }
        
    return r;
}

int main()
{
    int x;
    scanf("%d", &x);
    printf("%d\n", reverse(x));
    printf("%d\n", -103%10);
}