// 16MHz Taktrate
#define F_CPU 16000000ULL

#define MAX_TASKS_PER_MOTOR 10

// der Interrupt wird jede halbe Milisekunde aufgerufen (2000Hz)
// die MP3 ist 293 Sekunden lang
#define SECONDS      4000UL
//#define MAX_TIME     293*SECONDS
#define MAX_TIME     293*SECONDS
#define SYNC_TIME    263*SECONDS

// zweimal toggeln ergibt ein schritt
#define STEPS        2

#define IDLE 5000

#define CW  0
#define CCW 1

#define ADC_MEASUREMENTS 3

#define M1_LICHTSCHRANKE_LED     PA0
#define M1_LICHTSCHRANKE_CHANNEL 2
#define M2_LICHTSCHRANKE_LED     PA1
#define M2_LICHTSCHRANKE_CHANNEL 3

#define MP3_DDR      DDRB
#define MP3_PORT     PORTB
#define MP3_PLAY     PB1
#define MP3_BACK     PB2

#define LED          PD6
#define LED_PORT     PORTD
#define LED_DDR      DDRD

#define BUTTON       PB4
#define BUTTON_PIN   PINB
#define BUTTON_PORT  PORTB
#define BUTTON_DDR   DDRB

#define M0_DDR       DDRD
#define M0_PORT      PORTD
#define M0_CK        PD5
#define M0_CCW       PD4
#define M0_HALF      PD3
#define M0_ENABLE    PD2

#define M1_DDR       DDRC
#define M1_PORT      PORTC
#define M1_CK        PC0
#define M1_CCW       PC1
#define M1_HALF      PC3
#define M1_ENABLE    PC2

#define M2_DDR       DDRC
#define M2_PORT      PORTC
#define M2_CK        PC4
#define M2_CCW       PC5
#define M2_HALF      PC7
#define M2_ENABLE    PC6
