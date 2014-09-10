/* COMPILE
 * gcc -Wall -O2 backlight.c -o backlight
 *
 * DESCRIPTION
 * This program adjusts the brightness of my laptop screen.
 * ./backlight ARG
 * ARG is a number between 0 (completely dark) to 976 (maximum brightness)
 */
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PATH "/sys/class/backlight/intel_backlight/brightness"

void usage(FILE *stream, int argc, char *argv[])
{
    fprintf(stream, "Usage: %s VALUE\n", argv[0]);
    fprintf(stream, "\tVALUE is a number between 0 (screen dark) and 976 (maximum brightness)\n");
}

int main(int argc, char *argv[])
{
    int value, err;
    FILE *fh;

    /* check if we have at least 1 argument */
    if(argc < 2)
    {
        fprintf(stderr, "Command line option missing\n\n");
        usage(stderr, argc, argv);
        return EXIT_FAILURE;
    }

    /* convert argument to an integer */
    if(sscanf(argv[1], "%d", &value) != 1)
    {
        fprintf(stderr, "Command line option missing\n\n");
        usage(stderr, argc, argv);
        return EXIT_FAILURE;
    }

    /* open file, write value to it and close it again */
    if((fh = fopen(PATH, "w")) == NULL)
    {
        err = errno;
        fprintf(stderr, "Can't open %s: %s (%d)\n", PATH, strerror(err), err);
        return EXIT_FAILURE;
    }
    fprintf(fh, "%d\n", value);
    fclose(fh);

    return EXIT_SUCCESS;
}
