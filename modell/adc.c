#include <avr/io.h>
#include <inttypes.h>

#include "adc.h"
#include "define.h"

uint16_t adc_read(uint8_t channel)
{
  uint8_t  i;
  uint16_t result = 0;
  
  // ADC aktivieren; teilungsfaktor 32
  ADCSRA = (1 << ADEN | 1 << ADPS2 | 1 << ADPS0);

  ADMUX = channel;

  // 5V referenzspannung
  ADMUX |= (1 << REFS0);
  
  // ADC initialisieren und Dummyreadout machen
  ADCSRA |= (1 << ADSC);
  while(ADCSRA & (1 << ADSC));
  
  for(i = 0; i < ADC_MEASUREMENTS; i++)
  {
    ADCSRA |= (1 << ADSC);
    while(ADCSRA & (1<<ADSC));
    
    result += ADCW;
  }
  
  // ADC wieder deaktivieren
  ADCSRA &= ~(1 << ADEN);
  
  result /= ADC_MEASUREMENTS;
  
  return result;
}
