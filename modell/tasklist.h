#include "define.h"

struct task
{
  uint32_t time;
  uint16_t steps;  // anzahl der schritte
  uint16_t idle;
  uint8_t  modulo; // jede modulo-te Milisekunde einen Takt
  uint8_t  ccw;
};

struct tasklist
{
  uint8_t cur;
  uint8_t count;
  struct task tasks[MAX_TASKS_PER_MOTOR];
};

void tasklist_init(void);
void tasklist_reset(void);
void tasklist_add(uint8_t motor, uint32_t time, uint16_t steps, uint8_t modulo, uint8_t ccw);
uint8_t tasklist_get(uint8_t motor, uint32_t time, struct task *p);
