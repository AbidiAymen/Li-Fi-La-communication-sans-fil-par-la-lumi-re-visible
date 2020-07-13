String data = "";
String packet_size = "";
int sync = 10;
bool thresholdCheck = true;
bool receive = false;
char inByte;
int ledPin = 12; 
int ledPin2 =8; 
int mode = -1;

void setup(){
Serial.begin(115200);
Serial.setTimeout(10);
Serial.println("DONE");
pinMode(ledPin,OUTPUT); 
pinMode(ledPin2,OUTPUT); 
randomSeed(analogRead(5));
receive = true;
mode = 0;
}

void loop(){
  while (Serial.available()>0){
    String s = Serial.readString();
    int temp = s.length();
    s = s.substring(0,temp-1);
    if(receive){
      if(s.length()>15){
        while (s.length()>0){
          if(s.length()>15){
            data = s.substring(0,15);
            s = s.substring(15);
            Transm();
            ResetLight();
            delayMicroseconds(2000);
          }else{
            data = s;
            s="";
            Transm();
            ResetLight();
          }
        }
        Serial.println("DONE");
        }else{
          data = s;
          s="";
          Transm();
          ResetLight();
          Serial.println("DONE");
        }
    }
  }
}
void Transm(){
    if(data.length()>0){
      Serial.println(data);
      SendData();
    }
  }
  

void ResetLight(){
  if(mode == 0){
   digitalWrite(ledPin, LOW);
   digitalWrite(ledPin2, LOW); 
  } 
}


void SendData()
{
  if(mode ==0){
  digitalWrite(ledPin2, HIGH);
  for(int i = 0; i < data.length(); i++){
    if(data[i] == '1')
    {
      digitalWrite(ledPin, HIGH);
      delay(sync); 
      digitalWrite(ledPin, LOW);
    }
    else
    {
     digitalWrite(ledPin, LOW);
     delay(sync); 
    }
    digitalWrite(ledPin, LOW);
    }
  }
}
