#include "rgbLed.h"
//RgbColor a[]={OFF, WHITE, RED, GREEN, BLUE, LBLUE, PINK, YELLOW};
#define CHANGE_COLOR_TIME 10000
#define RED_SHIFT_PERIOD 90
#define GREEN_SHIFT_PERIOD 65

RgbLed led1(7,6,5,false);
RgbLed led2(4,3,2,false);
RgbLed *greenLed = &led1;
RgbLed *redLed = &led2;

unsigned long LastChangeColorTime;
unsigned long LastRedColorChange;
unsigned long LastGreenColorChange;

void setup() {
  LastChangeColorTime = 
    LastRedColorChange = 
    LastGreenColorChange = millis();                
}

void loop() {
  // swap colors
  if(millis() - LastChangeColorTime > CHANGE_COLOR_TIME){
    RgbLed *t = greenLed;
    greenLed = redLed;
    redLed = t;
    LastChangeColorTime = millis();
  }
  if(millis() - LastRedColorChange > RED_SHIFT_PERIOD){
    redLed->isLights() ? redLed->writeSimpleColor(OFF) : redLed->writeSimpleColor(RED);
    LastRedColorChange = millis();
  }
  if(millis() - LastGreenColorChange > GREEN_SHIFT_PERIOD){
    greenLed->isLights() ? greenLed->writeSimpleColor(OFF) : greenLed->writeSimpleColor(GREEN);
    LastGreenColorChange = millis();
  }  

}
