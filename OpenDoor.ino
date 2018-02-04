/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
const int inpin = 4;
const int servo = 9;


void setup() {
  
  myservo.attach(servo);  // attaches the servo on pin 9 to the servo object

  pinMode(inpin, INPUT);

  //Serial.begin(9600);
}

void loop() {
  int ready_me;
  //Serial.println("FUCK 1");
  ready_me = digitalRead(inpin);
  if (ready_me == HIGH){
    //Serial.println(ready_me);
    //while(true);
    for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(15);                       // waits 15ms for the servo to reach the position
    }
    delay(1000);
    for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
      myservo.write(pos);              // tell servo to go to position in variable 'pos'
      delay(15);                       // waits 15ms for the servo to reach the position
    }
    //ready_me = LOW;
  }
}

