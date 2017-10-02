#include <stdio.h>
#include <stdlib.h>

int main()
{
	double d;
	// system load in the past 1 minute
	if(getloadavg(&d, 1)==1)
	{
		printf("%lf", d);
	}
}
