int LED_Pin_3 = 3;
char userInput;
int dutyCycleVal;
void setup() {
  pinMode(LED_Pin_3, OUTPUT);
  Serial.begin(9600);
}

int getDuty(){
    String userInput_duty;
    int dutyCycle;
    
    userInput_duty = Serial.readString();
    dutyCycle = userInput_duty.toInt();
    return dutyCycle;
}
void loop() {

  if(Serial.available()>0){
    userInput = Serial.read();
    Serial.println(userInput);
    if(userInput == 'd'){
      Serial.println("Enter Duty Cycle");
        while(1){
          if(Serial.available()>0){
            dutyCycleVal = getDuty();
            Serial.println(dutyCycleVal);
            analogWrite(LED_Pin_3,dutyCycleVal);
          } // Enter Duty Cycle
        }
      } // if 'd'
    } // First If available
  } // Main Loop 

