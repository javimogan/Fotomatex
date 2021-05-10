const int boton = 2;
const int led = 3;
const int ledR = 4;
void setup() {
  
  pinMode(boton, INPUT);
  pinMode(led, OUTPUT);
  pinMode(ledR, OUTPUT);

  Serial.begin(9600);
  
  // put your setup code here, to run once:

}

bool estado = true;
int botonPulsado = false;

void loop() {
      botonPulsado = digitalRead(2);
      if (Serial.available()>0){
         char option = Serial.read();
          //Cambiamos el estado
          if(option == 'c'){
            estado = !estado;
          }         
   }

      if(estado){
        digitalWrite(led, HIGH);
        digitalWrite(ledR,LOW);
      }else{
        digitalWrite(led, LOW);
        digitalWrite(ledR, HIGH);
      }
    
      if(botonPulsado == HIGH && estado){
        estado = false;
        digitalWrite(led, LOW);
        digitalWrite(ledR, HIGH);
        Serial.println("f");
        delay(1000);
          
      }
  
  
}
