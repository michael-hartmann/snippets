#include "define.h"

#include <util/delay.h>

void sleep(unsigned int i)
{
  while(i--)
    _delay_ms(1);
}
