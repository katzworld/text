//simple macro button using a attiny85 dev USB board and a simple arcade style button 

#include "DigiKeyboard.h" 
#define BUTTON_PIN 2
#define LED_PIN 1

void setup(void) {
   pinMode(BUTTON_PIN, INPUT_PULLUP);
   pinMode(LED_PIN,OUTPUT);
}

void loop(void) {
  if(digitalRead(BUTTON_PIN)== LOW){
    digitalWrite(LED_PIN,HIGH);
//  <MENU>   ALT + A , <TAB>, "JACK", <ENTER>
    DigiKeyboard.sendKeyStroke(0x65); //MENU 
    //DigiKeyboard.delay(100);
    DigiKeyboard.sendKeyStroke(MOD_ALT_RIGHT); //ALT 
    //DigiKeyboard.delay(100);
    DigiKeyboard.sendKeyStroke(KEY_A); //A? 
    //DigiKeyboard.delay(100);
    DigiKeyboard.sendKeyStroke(0x2B); //<TAB>
    //DigiKeyboard.delay(100);
    DigiKeyboard.print("JACK"); //string
    DigiKeyboard.sendKeyStroke(KEY_ENTER); //SEND IT
    DigiKeyboard.delay(250);
    digitalWrite(LED_PIN,LOW); //lights off 
  }
 DigiKeyboard.delay(100);   
}
