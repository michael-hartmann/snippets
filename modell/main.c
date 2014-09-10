#include <avr/io.h>
#include <avr/interrupt.h>
#include <inttypes.h>

#include "define.h"
#include "main.h"
#include "mp3.h"
#include "sm.h"
#include "tasklist.h"
#include "adc.h"
#include "delay.h"

#include <util/delay.h>


volatile uint32_t time;
volatile uint8_t  lock = 0;
struct task cur_task[3];

volatile char sync_m1;
volatile char sync_m2;


int main(void)
{
  // schrittmotoren initialisieren, also die DDRs richtig setzen
  sm_init(0);
  sm_init(1);
  sm_init(2);
  
  // DDR fuer knopf und mp3-player setzen
  BUTTON_DDR  &= ~(1 << BUTTON);
  BUTTON_PORT |=  (1 << BUTTON);
  LED_DDR     |=  (1 << LED);
  mp3_init();

  // die aufgabenliste initialisieren...
  tasklist_init();

  // ...und mit aufgaben fuellen: 
  // (motor, startzeit, schritte, geschwindigkeit, drehrichtung)
  
  /* Alle 0,5ms wird ein Interrupt generiert. D.h. die maximale Geschwindigkeit
   * betraegt /einen/ (Schritt nur bei GND-Flanke! 2x toggeln = 1 Schritt)
   * Schritt in einer Milisekunde, also 1000 Schritte pro Sekunde. 
   *
   * Schritt = 0,9°
   *
   * Schritte pro Sekunde  = 1000 / Geschwindigkeit        [1/s]
   * Winkelgeschwindigkeit = 1000 / Geschwindigkeit * 0,9° [°/s]
   */

  // 2112 * 124/1000 = 262s (Schritte * Sekunden/Schritt = Sekunden)
  //tasklist_add(0,  2*SECONDS, 4224*STEPS, 124, CCW); // putzfrau (262s lang)
  //tasklist_add(1,  2*SECONDS, 4224*STEPS, 124, CCW); // putzfrau (262s lang)
  //tasklist_add(2,  2*SECONDS, 4224*STEPS, 124, CCW); // putzfrau (262s lang)

  tasklist_add(0,   2*SECONDS, 4224*STEPS, 124,  CW); // putzfrau (262s lang)

  tasklist_add(1,  50*SECONDS,  267*STEPS, 180, CCW); // patient vorwaerts
//  tasklist_add(1, 263*SECONDS,  257*STEPS, 180,  CW); // patient rueckwaerts

  tasklist_add(2,  70*SECONDS, 80*STEPS,   116, CW); // arzt
  tasklist_add(2,  94*SECONDS, 80*STEPS,   116, CW); // pfleger
  tasklist_add(2, 126*SECONDS, 80*STEPS,   116, CW); // therapeuth
  tasklist_add(2, 163*SECONDS, 80*STEPS,   116, CW); // sozialdienst
  tasklist_add(2, 208*SECONDS, 78*STEPS,   116, CW); // lehrer

  // mp3-player einschalten
  mp3_power();

  // syncen
  start(1);

  while(1)
  {
    // wenn das modell gerade nichts tut (also kein lock gesetzt; lock = 0),
    // dann koennen wir testen, ob die taste gedrueckt wurde. wenn dies der
    // fall ist, koennen wir mit dem durchlauf anfangen (start()). start()
    // kuemmert sich auch um den lock (lock = 1)
    if(lock == 0)
    {
      if(!bit_is_set (BUTTON_PIN, BUTTON))
        start(0);
    }
    else
    {
      if(sync_m1 && (adc_read(M1_LICHTSCHRANKE_CHANNEL) > 700))
        sync_m1 = 0;
    
      if(sync_m2 && (adc_read(M2_LICHTSCHRANKE_CHANNEL) > 800))
        sync_m2 = 0;
    }
  }

  return 0;
}


// jemand hat den knopf gedrueckt - los geht's!
void start(char sync)
{
  uint8_t motor;

  // das modell ist beschaeftigt: lock
  lock = 1;

  // LEDs fuer lichtschranken einschalten
  PORTA |= (1 << M1_LICHTSCHRANKE_LED | 1 << M2_LICHTSCHRANKE_LED);

  LED_PORT |= (1 << LED);

  // unsere aufgabenliste zuruecksetzen - wir haben noch nichts abgearbeitet
  tasklist_reset();

  if(sync == 0)
    time = 0;
  else
    time = SYNC_TIME - 2;

  // mp3-player zuruecksetzen: brauchen wir nicht, weil nur ein song auf dem
  // mp3-player ist
  // mp3_back();

  // wir haben noch keine aktuelle aufgabe, also evtl. noch verbleibende alte
  // zuruecksetzen
  for(motor = 0; motor < 3; motor++)
  {
    cur_task[motor].steps  = 0;
    cur_task[motor].modulo = 0;
    cur_task[motor].ccw    = 0;
    cur_task[motor].idle   = 0;
  }

  // prescaler 64: 
  // 16'000kHz/1024 = 15,625kHz; d.h.: alle 64 mikrosekunden
  TCCR2 = (1 << CS20 | 1 << CS22 | 1 << WGM21);

  // bis 200 hochzaehlen:
  // 15'625Hz/200 = 78 Hz; d.h. jede 12,8te milisekunde
  OCR2  = 250;

  TCNT2 = 0;

  // interrupt enable: die ISR wird jede halbe milisekunde aufgerufen
  TIMSK |= (1 << OCIE2);

  if(sync == 0)
  {
    // und action! mp3-player faengt an zu spielen...
    mp3_play();
  }
  //else
  //{
    // warten bis LEDs an sind
  //  sleep(100);
  //}

  // alle interrupts global aktivieren
  sei();
}

void stop(void)
{
  // zuerst interrupts deaktivieren, damit die ISR nicht weiter aufgerufen wird
  cli();

  // LEDs fuer lichtschranken ausschalten
  PORTA &= ~(1 << M1_LICHTSCHRANKE_LED | 1 << M2_LICHTSCHRANKE_LED);

  LED_PORT &= ~(1 << LED);

  TIMSK &= ~(1 << OCIE2);

  // kurz warten, damit nach dem syncen die scheiben auch wirklich stehen
  // bleiben
  //XXX sleep(2000);

  // alle motoren stoppen, also v.a. sie ausschalten
  sm_disable(0);
  //sm_disable(1);
  sm_disable(2);

  // ok wir sind fertig, wir koennen den lock loesen
  lock = 0;
}


// ISR, die jede halbe milisekunde aufgerufen wird, wenn aktiv
SIGNAL(SIG_OUTPUT_COMPARE2)
{
  uint8_t motor;

  // zeit hochzaehlen 
  time++;

  // evtl nur noch syncen
  if(time >= SYNC_TIME)
  {
    if(time == SYNC_TIME)
    {
      sm_enable(1, CW);
      sm_enable(2, CCW);
      sleep(100);
    }

    if(time % 180 == 0)
    {
      if(sync_m1)
        sm_step(1);
    }

    if(time % 3 == 0)
    {
      if(sync_m2)
        sm_step(2);
    }

    if(!sync_m1 && !sync_m2 && time > MAX_TIME)
      stop();
  }
  else
  {
    sync_m1 = 1;
    sync_m2 = 1;

    // folgendes fuer jeden der drei schrittmotoren machen...
    for(motor = 0; motor < 3; motor++)
    {
      // wenn steps 0 ist, so hat der schrittmotor seine letzte aufgabe
      // abgearbeitet; also schauen, ob es eine neue fuer ihn gibt
      if(cur_task[motor].steps == 0)
      {
        // wenn es eine neue aufgabe gibt, den motor "starten"; d.h. drehrichtung
        // setzen, einschalten usw...
        if(tasklist_get(motor, time, &cur_task[motor]))
          sm_enable(motor, cur_task[motor].ccw);
        // ansonsten pruefen, ob wir den motor schon ausschalten koennen
        else 
        {
          if(cur_task[motor].idle <= IDLE)
            cur_task[motor].idle++;
          else
          {
            if(motor == 2)
              sm_disable(2);
          }
        }
      }
  
      // wenn wir noch eine alte aufgabe (oder eine neue) haben, dann evtl einen
      // schritt machen, wenn modulo == 0
      if(cur_task[motor].steps > 0)
      {
        if(time % cur_task[motor].modulo == 0)
        {
          cur_task[motor].steps--;
          sm_step(motor);
        }
      }
    }
  }
}
