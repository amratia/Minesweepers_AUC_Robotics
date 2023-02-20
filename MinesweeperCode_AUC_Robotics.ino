 #include <SPI.h>
#include <Ethernet.h>

// Ethernet settings
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192,168,1,177);
EthernetServer server(80);

// Pin settings
// PWM pins are 3,5,6 --> (2,3) for motor ,(4,5) for motor, (6,7) for motor 
int arm_DIR = 2;
int arm_PWM = 3;     //PWM
int RIGHT_DIR = 4;
int RIGHT_PWM = 5;   //PWM
int LEFT_PWM = 6;    //PWM
int LEFT_DIR = 7;

//---------------------------------------------
void setup() {
  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.begin(9600);

  pinMode(arm_DIR,OUTPUT);    
  pinMode(arm_PWM,OUTPUT);    
  pinMode(RIGHT_DIR,OUTPUT);   
  pinMode(RIGHT_PWM,OUTPUT);   
  pinMode(LEFT_PWM,OUTPUT);    
  pinMode(LEFT_DIR,OUTPUT);    

}
//---------------------------------------------
void loop() {

  EthernetClient client = server.available();
  
  if (client) {
    int incomingData = client.read();
    // set the pin value
    if (incomingData == '1') { // W --> Move Forward
      move_forward();
      delay(30);
      Serial.println("Signal for 'w' received");
    }
    else if (incomingData == '2') { // A --> Move Left
      move_left();
      delay(30);
      Serial.println("Signal for 'a' received");
    }
    else if (incomingData == '3') { // S --> Move Back
      move_back();
      delay(30);
      Serial.println("Signal for 's' received");
    }
    else if (incomingData == '4') { // D --> Move Right
      move_right();
      delay(30);
      Serial.println("Signal for 'd' received");
    }
    else move_stop();
  }
  else move_stop();

}



//---------------------------------------------
void move_forward(){
  digitalWrite(LEFT_DIR,HIGH);
  digitalWrite(RIGHT_DIR,HIGH);
  analogWrite(LEFT_PWM,200);
  analogWrite(RIGHT_PWM,200);
}
void move_back(){
  digitalWrite(LEFT_DIR,LOW);
  digitalWrite(RIGHT_DIR,LOW);
  analogWrite(LEFT_PWM,200);
  analogWrite(RIGHT_PWM,200);
}
void move_left(){
  digitalWrite(LEFT_DIR,LOW);
  digitalWrite(RIGHT_DIR,HIGH);
  analogWrite(LEFT_PWM,0);
  analogWrite(RIGHT_PWM,200);
}
void move_right(){
  digitalWrite(LEFT_DIR,HIGH);
  digitalWrite(RIGHT_DIR,LOW);
  analogWrite(LEFT_PWM,200);
  analogWrite(RIGHT_PWM,0);
}
void move_stop(){
  digitalWrite(LEFT_DIR,LOW);
  digitalWrite(RIGHT_DIR,LOW);
  analogWrite(LEFT_PWM,0);
  analogWrite(RIGHT_PWM,0);
}
void motor_up(){
  //gg
}
void motor_down(){
  //kk
}
