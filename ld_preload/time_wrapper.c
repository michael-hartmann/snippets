/* Compile with:
 * gcc -o time_wrapper.so -shared time_wrapper.c -ldl
 */

#include <stdio.h>
#include <sys/time.h>

/* new gettimeofday function */
int gettimeofday(struct timeval *tv, struct timezone *tz)
{
    tv->tv_sec  = 9999;
    tv->tv_usec = 0;

    return 0;
}
