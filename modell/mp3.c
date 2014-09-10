#include <avr/io.h>

#include "define.h"
#include "delay.h"


#define DELAY_PRESS  200
#define DELAY_POWER 1500


void mp3_init(void)
{
  MP3_DDR |= (1 << MP3_PLAY | 1 << MP3_BACK);
}

void mp3_power(void)
{
  MP3_PORT |=  (1 << MP3_PLAY);
  sleep(DELAY_POWER);
  MP3_PORT &= ~(1 << MP3_PLAY);
  sleep(5000);
}

void mp3_play(void)
{
  MP3_PORT |=  (1 << MP3_PLAY);
  sleep(DELAY_PRESS);
  MP3_PORT &= ~(1 << MP3_PLAY);
}

void mp3_pause(void)
{
  mp3_play();
}

void mp3_back(void)
{
  MP3_PORT |=  (1 << MP3_BACK);
  sleep(DELAY_PRESS);
  MP3_PORT &= ~(1 << MP3_BACK);
}
