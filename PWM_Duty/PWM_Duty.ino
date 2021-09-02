/* This Arduino code is design to interface with the Python Tkinter PWM_GUI.py user interface.
 * It uses Pluse Width Modulation to control the intensity of an LED. This code waits for
 * the mode/value to be sent (via pyserial) and then updates the PWM output value.
 * 
 * Python code: https://github.com/WaveShapePlay/ArduinoPulseWidthModulation/blob/master/PWM_GUI.py
 */
 
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

/*  loop() 
 *  
 *  Function checks/monitors user data via Serial.available(). If data is transfered 
 *  using pyserial, then the mode will be checked. First the mode is sent, followed 
 *  by user value if applicable. 
 *  
 *  Modes:
 *    'd' = Data mode waits for the user to input the desired pwm value. After
 *          'd' is recived 'user_value_flag' is set to zero, which is the conditional
 *          for the while loop. Once the user updates the value, we output the
 *          value to the Arduino PWM pin and exit the while loop.
 *     
 *    'f' = Fade mode runs a incrementing loop followed by a decrimenting loop.
 *    The index of each loop is the PWM output value. The net effect is a gradual
 *    fade of an LED. The delay() value controls the duration of the fade, after  
 *    each updated PWM value.
 */ 
void loop() {

  if(Serial.available()>0){
    userInput = Serial.read();
    Serial.println(userInput);
    if(userInput == 'd'){
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

