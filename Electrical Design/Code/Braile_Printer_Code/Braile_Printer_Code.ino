#include <Servo.h>

Servo servo_one;
Servo servo_two;

int pos_1 = 0;
int pos_2 = 0;

//array for the pins
int LED[] = {2,3,5,4,6,7};

//the input value to be displayed
int input[] = {1,1,1,1,1,1};

//the length of the input array             
int input_len = sizeof(input) / sizeof(int);
int refresh_rate = input_len / 6;
void motion();
void setup() {
  Serial.begin(9600);
  //initializing the pins as output
  for (int i = 0; i < 6; i++){
      pinMode(LED[i], OUTPUT);
  }

  
  //initializing the servo motor in pin 9 and pin 10
  servo_one.attach(9);
  servo_two.attach(10);

  servo_one.write(0);
  servo_two.write(0);
}

void loop() {
  //used for serial communication
  char serialdata = '0';
  if (Serial.available() > 0){
    serialdata = Serial.read();
    delay(10);
    if (serialdata == '1'){
        motion();
    }else{
        for (int k = 0; k < 6; k++){
              digitalWrite(LED[k], LOW);
        }
    }
  }
}
void motion(){
    for (int i = 0; i < refresh_rate; i++){
    delay(100);
    servo_one.write(0);
    servo_two.write(0);
    for (int k = 0; k < 6; k++){
        digitalWrite(LED[k], LOW);
    }
    delay(100);
    int temp[6];
    for (int j = 0; j < 6; j++){
        temp[j] = input[(j + (6 * i))];
    }
    delay(100);
    for (int k = 0; k <= 6; k++){
        if (k == 0){
            servo_one.write(0);
            servo_two.write(0);
            delay(400);
            digitalWrite(LED[k], temp[k]);
            delay(400);
        }else if (k == 1){
            servo_one.write(90);
            //servo_two.write(0);
            delay(400);
            digitalWrite(LED[k], temp[k]);
            delay(400);
        }else if (k == 2){
            //servo_one.write(0);
            servo_two.write(90);
            delay(400);
            digitalWrite(LED[k], temp[k]);
            delay(400);
        }else if (k == 3){
            servo_one.write(180);
            //servo_two.write(0);
            delay(400);
            digitalWrite(LED[k], temp[k]);
            delay(400);
        }else if (k == 4){
            //servo_one.write(0);
            servo_two.write(180);
            delay(400);
            digitalWrite(LED[k], temp[k]);
            delay(400);
        }else if (k == 5){
            servo_one.write(90);
            //servo_two.write(0);
            delay(400);
            digitalWrite(LED[k], temp[k]);
            delay(400);
        }        
    }
    delay(500);
}
}

