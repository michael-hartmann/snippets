#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

uint64_t isqrt(uint64_t a, bool* isinteger)
{
    uint64_t x = sqrt(a);

    *isinteger = x*x == a;

    return x;
}


int main(void)
{
    uint64_t sum = 0;

    for(uint64_t a = 1; true; a++)
    {
        uint64_t array[2] = { a-1, a+1 };

        for(int i = 0; i < 2; i++)
        {
            uint64_t c = array[i];
            bool isinteger;

            uint64_t value = isqrt(4*a*a-c*c, &isinteger);

            // A * 4
            uint64_t A4 = value*c;

            uint64_t U = a+a+c;
            if(U >= 1000000000)
                goto out;

            if(isinteger && A4 && (A4 % 4) == 0)
                sum += U;
        }
    }

out:
    printf("%llu\n", (long long unsigned)sum);

    return 0;
}
