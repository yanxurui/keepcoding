#include <stdio.h>
#include <endian.h>

int main()
{
	#if __BYTE_ORDER == __LITTLE_ENDIAN
		printf("little edian\n");
	#elif __BYTE_ORDER == __BIG_ENDIAN
	    printf("big edian\n");
	#else
	    printf("error\n");
	#endif
	return 0;
}