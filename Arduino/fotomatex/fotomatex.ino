
/*
  FOTOMATEX

	Created 8/06/2021
	By @javimogan

	https://github.com/javimogan/Fotomatex

*/
#define LED_LOCKED 6
#define LED_UNLOCKED 7
#define BUTTON 8
// If does not receive the command to unlock, do it in XXXX milliseconds
#define MAX_LOCKED_TIME 8000

bool locked = false;
unsigned long currentLockedTime = 0;

void setup()
{

  pinMode(BUTTON, INPUT);
  pinMode(LED_LOCKED, OUTPUT);
  pinMode(LED_UNLOCKED, OUTPUT);
  changeState();
  Serial.begin(115200);
}

void loop()
{
  //Check how long the microcontroller has been locked
  if ((millis() - currentLockedTime) >= MAX_LOCKED_TIME)
    unlock();
  // Unlock
  if (Serial.available() > 0 && Serial.read() == 'c')
    unlock();
  // Is the button is pressed in the unlocked state
  if (digitalRead(BUTTON) == HIGH && !locked)
  {
    //Block the microcontroller
    currentLockedTime = millis();
    locked = true;
    changeState();
    //Send command to take a photo
    Serial.println("f");
  }
}
// Unlock the microcontroller
void unlock()
{
  locked = false;
  changeState();
  currentLockedTime = 0;
}
// Change the state of the LEDs
void changeState()
{
  /*if(locked){
    digitalWrite(LED_LOCKED, 1);
    digitalWrite(LED_UNLOCKED, 0);
    }else{
      digitalWrite(LED_LOCKED, 0);
    digitalWrite(LED_UNLOCKED, 1);
    }*/
  digitalWrite(LED_LOCKED, locked);
  digitalWrite(LED_UNLOCKED, !locked);
}
