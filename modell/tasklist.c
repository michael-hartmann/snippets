#include <avr/io.h>
#include <inttypes.h>

#include "tasklist.h"

struct tasklist tasklist[3];

// tasklist initialisieren; .cur und .count initialisieren mit 0
void tasklist_init(void)
{
  uint8_t i;

  for(i = 0; i < 3; i++)
  {
    tasklist[i].cur   = 0;
    tasklist[i].count = 0;
  }
}

void tasklist_reset(void)
{
  uint8_t i;

  for(i = 0; i < 3; i++)
    tasklist[i].cur = 0;
}

// eine aufgabe hinzufuegen
void tasklist_add(uint8_t motor, uint32_t time, uint16_t steps, uint8_t modulo, uint8_t ccw)
{
  uint8_t count;
  
  count = tasklist[motor].count++;

  tasklist[motor].tasks[count].time   = time;
  tasklist[motor].tasks[count].steps  = steps;
  tasklist[motor].tasks[count].modulo = modulo;
  tasklist[motor].tasks[count].ccw    = ccw;
}

// die naechste anstehende aufgabe abholen
// wenn es keine gibt, wird 0 returned
uint8_t tasklist_get(uint8_t motor, uint32_t time, struct task *p)
{
  uint8_t cur, count;

  cur   = tasklist[motor].cur;
  count = tasklist[motor].count;

  if(cur < count && tasklist[motor].tasks[cur].time <= time)
  {
    *p  = tasklist[motor].tasks[cur];
    tasklist[motor].cur++;

    return 1;
  }

  return 0;
}
