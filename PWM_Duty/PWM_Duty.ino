int LED_Pin_3 = 3;
char userInput;
int dutyCycleVal;
int pwm_val = 0;
int pwmMaxValue = 255;

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
    if(userInput == 'l'){
      for(int i = 0; i< 256; i ++){
        analogWrite(LED_Pin_3,i);
        delay(10);
      }
      for(int y = 0; y < 256; y++){
        pwm_val = pwmMaxValue - y;
        analogWrite(LED_Pin_3, pwm_val);
        delay(10);
      }
    } // if 'l'
    } // First If available
  } // Main Loop 

