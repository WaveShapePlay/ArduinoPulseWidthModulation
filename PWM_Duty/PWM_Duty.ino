int LED_Pin_3 = 3;
char userInput;
int dutyCycleVal;
int pwm_val = 0;
int pwmMaxValue = 255;
int user_value_flag = 0;

// Setup() - Initilization of PWM output pin and Serial connection
void setup() {
  pinMode(LED_Pin_3, OUTPUT);
  Serial.begin(9600);
}

// getDuty() - Read in user's String value, convert to int and return for 
// pwm output value
int getDuty(){
    String userInput_duty;
    int dutyCycle;
    userInput_duty = Serial.readString();
    dutyCycle = userInput_duty.toInt();
    return dutyCycle;
}

/* loop() - Checks/monitors for user data via Serial.available()
 *  If data is transfered using pyserial, then the values will
 *  be checked. The values contain the mode (followed by user value if applicable). 
 *  The modes are:
 *    'd' = data mode waits for the user to input the desired pwm value
 *    'f' = fade mode runs a incrementing/decrimenting pwm loop once
 */
void loop() {

  if(Serial.available()>0){
    userInput = Serial.read();
    Serial.println(userInput);
    if(userInput == 'd'){
      Serial.println("Enter Duty Cycle");
      user_value_flag = 0;
        while(user_value_flag == 0){
          if(Serial.available()>0){
            dutyCycleVal = getDuty();
            Serial.println(dutyCycleVal);
            analogWrite(LED_Pin_3,dutyCycleVal);
            user_value_flag = 1;
          } // Enter Duty Cycle
        }
      } // if 'd'
    if(userInput == 'f'){
      for(int i = 0; i< 256; i ++){
        analogWrite(LED_Pin_3,i);
        delay(10);
      }
      for(int y = 0; y < 256; y++){
        pwm_val = pwmMaxValue - y;
        analogWrite(LED_Pin_3, pwm_val);
        delay(10);
      }
    } // if 'f'
    } // First If available
  } // Main Loop 

