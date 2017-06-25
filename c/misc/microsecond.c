#include <stdio.h>
#include <sys/time.h>
#include <math.h>
#include <stdint.h>

uint64_t GetTimeStamp()
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec*(uint64_t)1000000 + tv.tv_usec;
}

int main()
{
	uint64_t s = GetTimeStamp();
	double result;
	for(int i=0;i<10000000;i++)
	{
		result = sqrt((double)i);
	}
	uint64_t e = GetTimeStamp();
	printf("%lu\n", s);
	printf("%lu\n", e);
	printf("%lu\n", e-s);

	return 0;
}
