
int LED_Pin_3 = 3;

void setup() {
  pinMode(LED_Pin_3, OUTPUT);
}

void loop() {
  //int i = 0;
  for(int i=0; i<225;i++){
    analogWrite(LED_Pin_3,i);
    delay(10);                      // milli seconds
  }
  
}
