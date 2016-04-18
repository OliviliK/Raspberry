#include <stdio.h>
#include <wiringPi.h>

// LED Pin - wiringPi pin 4 is physical pin 16, BCM pin GPIO 23

#define LED     4

int main (void) {
  printf ("Raspberry Pi blink\n") ;

  wiringPiSetup ();
  pinMode (LED, OUTPUT) ;

  for (;;) {
    digitalWrite (LED, HIGH);   // On
    delay (500) ;               // mS
    digitalWrite (LED, LOW);    // Off
    delay (500) ;
  }
  return 0;
}
