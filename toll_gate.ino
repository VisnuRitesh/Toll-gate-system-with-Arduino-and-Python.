int sensorVa1=LOW , sensorVa2=LOW  , sensorVa3=LOW ;
void setup() 
{
  Serial.begin(9600);

  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);

}

void loop()
{

  int sensorVa1 = digitalRead(2);
  int sensorVa2 = digitalRead(3);
  int sensorVa3 = digitalRead(4);

 if(sensorVa1==LOW && sensorVa2==LOW  && sensorVa3==HIGH)
   {
    Serial.println("1");
  delay(1000);
  }
  else if (sensorVa1==LOW && sensorVa2==HIGH  && sensorVa3==HIGH)
  {
    Serial.println("2");
    delay(1000);
 }
   else if(sensorVa1==HIGH && sensorVa2==HIGH  && sensorVa3==HIGH)
  {
    Serial.println("3");
    delay(1000);
 }
 else
 {
   Serial.println("0");
   delay(1000);
  }
}

