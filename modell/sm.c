#include <avr/io.h>
#include <inttypes.h>

#include "sm.h"
#include "define.h"

void sm_init(uint8_t i)
{
  switch(i)
  {
    case 0:
      M0_DDR |= (1 << M0_CK | 1 << M0_HALF | 1 << M0_ENABLE | 1 << M0_CCW);
      break;

    case 1:
      M1_DDR |= (1 << M1_CK | 1 << M1_HALF | 1 << M1_ENABLE | 1 << M1_CCW);
      break;

    case 2:
      M2_DDR |= (1 << M2_CK | 1 << M2_HALF | 1 << M2_ENABLE | 1 << M2_CCW);
      break;
  }
}

void sm_step(uint8_t i)
{
  switch(i)
  {
    case 0:
      M0_PORT ^= (1 << M0_CK);
      break;
    case 1:
      M1_PORT ^= (1 << M1_CK);
      break;
    case 2:
      M2_PORT ^= (1 << M2_CK);
      break;
  }
}

void sm_enable(uint8_t motor, uint8_t ccw)
{
  switch(motor)
  {
    case 0:
      M0_PORT |= (1 << M0_HALF | 1 << M0_ENABLE);
      
      if(ccw)
        M0_PORT |=  (1 << M0_CCW);
      else
        M0_PORT &= ~(1 << M0_CCW);
      
      break;

    case 1:
      M1_PORT |= (1 << M1_HALF | 1 << M1_ENABLE);

      if(ccw)
        M1_PORT |=  (1 << M1_CCW);
      else
        M1_PORT &= ~(1 << M1_CCW);
      
      break;
    
    case 2:
      M2_PORT |= (1 << M2_HALF | 1 << M2_ENABLE);
      
      if(ccw)
        M2_PORT |=  (1 << M2_CCW);
      else
        M2_PORT &= ~(1 << M2_CCW);
      
      break;
  }
}

void sm_stop(uint8_t i)
{
  switch(i)
  {
    case 0:
      M0_PORT &= ~(1 << M0_HALF | 1 << M0_CCW);
      break;

    case 1:
      M1_PORT &= ~(1 << M1_HALF | 1 << M1_CCW);
      break;

    case 2:
      M2_PORT &= ~(1 << M2_HALF | 1 << M2_CCW);
      break;
  }
}

void sm_disable(uint8_t i)
{
  sm_stop(i);

  switch(i)
  {
    case 0:
      M0_PORT &= ~(1 << M0_ENABLE);
      break;

    case 1:
      M1_PORT &= ~(1 << M1_ENABLE);
      break;

    case 2:
      M2_PORT &= ~(1 << M2_ENABLE);
      break;
  }
}
