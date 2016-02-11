/** A nice example of undefined behaviour in C
 *
 * If compiled using
 * $ clang -Wall -Oz truefalse.c -o truefalse
 * the program will print:
 * $ ./truefalse
 * false
 * false
 * 
 * The reason for this odd behaviour is the undefined value of the variable
 * boolean in line 33. Using uninitialized variables is undefined behaviour
 * according to the C standard.
 *
 * I stepped about this issued reading a blog post from Mark Shroyer,
 * https://markshroyer.com/2012/06/c-both-true-and-false/. However, I
 * had to adjust a bit his code in order that it "worked" for me.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void f(bool b)
{
    if(b)
        printf("true\n");
    else
        printf("false\n");
}

int main(int argc, char *argv[])
{
    bool *p = (bool *)malloc(sizeof(bool));
    bool boolean = *p;

    f(boolean);
    f(!boolean);

    return 0;
}
