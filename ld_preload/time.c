/* Compile with
 * gcc -Wall -O2 time.c -o time
 *
 * michael@mobile:/tmp$ LD_PRELOAD=./time_wrapper.so ./time
 * time = 9999.000
 */
#include <sys/time.h>
#include <stdio.h>

// int gettimeofday(struct timeval *tv, struct timezone *tz);


int main(int argc, char *argv[])
{
    struct timeval tv;
    double time;

    gettimeofday(&tv, NULL);
    time = tv.tv_sec + tv.tv_usec/1e6;

    printf("time = %.3lf\n", time);

    return 0;
}
