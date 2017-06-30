#pragma once

#define WHITE   RgbColor(HIGH, HIGH, HIGH)
#define OFF     RgbColor(LOW,  LOW,  LOW )
#define RED     RgbColor(HIGH, LOW,  LOW )
#define GREEN   RgbColor(LOW,  HIGH, LOW )
#define BLUE    RgbColor(LOW,  LOW,  HIGH)
#define LBLUE   RgbColor(LOW,  HIGH, HIGH)
#define PINK    RgbColor(HIGH, LOW,  HIGH)
#define YELLOW  RgbColor(HIGH, HIGH, LOW )


class RgbColor{
private:
  unsigned char r;
  unsigned char g;
  unsigned char b;

public:
  RgbColor(){
    r = 0;
    g = 0;
    b = 0;
  }
  RgbColor(unsigned char r,
      	   unsigned char g,
           unsigned char b){
    this->r = r;
    this->g = g;
    this->b = b;
  }

  unsigned char getR() { return r; }
  unsigned char getG() { return g; }
  unsigned char getB() { return b; }

  bool operator ==(RgbColor const &elem)
  {
    return r == elem.r &&
           g == elem.g &&
           b == elem.b;
  }

};

class RgbLed{
private:
  unsigned char rPin;
  unsigned char gPin;
  unsigned char bPin;
  bool isCC; 	     //true if LED is Common Cathode. Default - true
  RgbColor currentColor;
  
  unsigned char inverse(unsigned char sig){
    if(isCC)
      return sig;
    if(sig == LOW)
      return HIGH;
    return LOW;    
  }

public:
  RgbLed( unsigned char rPin,
          unsigned char gPin,
          unsigned char bPin,
          bool isCC){
    this->rPin = rPin;          
    this->gPin = gPin;
    this->bPin = bPin;
    this->isCC = isCC;
    pinMode(rPin, OUTPUT);
    pinMode(gPin, OUTPUT);
    pinMode(bPin, OUTPUT);
    writeSimpleColor(OFF);  
  }

  RgbLed( unsigned char rPin,
          unsigned char gPin,
          unsigned char bPin){
    RgbLed(rPin, gPin, bPin, true);
  }

  void writeSimpleColor(RgbColor color){
    currentColor = color;
    digitalWrite(rPin, inverse(color.getR()));
    digitalWrite(gPin, inverse(color.getG()));
    digitalWrite(bPin, inverse(color.getB()));
  }

  bool isLights(){
    return !(currentColor==OFF);
  }
};
