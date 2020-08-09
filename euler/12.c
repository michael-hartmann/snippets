#include <inttypes.h>
#include <stdio.h>
#include <stdint.h>

uint64_t Tn(uint64_t n)
{
    return (n*(n+1))/2;
}

int factors(uint64_t n)
{
    int c = 0;
    for(uint64_t i = 1; i <= n; i++)
    {
        if((n%i) == 0)
            c++;
    }
    return c;
}

int main(void)
{
    for(int n = 0; 1; n++)
    {
        uint64_t x = Tn(n);
        int c = factors(x);

        if(c > 500)
        {
            printf("%d, %" PRIu64 " %d\n", n, x, c);
            break;
        }
    }
}
