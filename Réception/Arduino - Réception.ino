const int sync = 10;
int photoPin = A4; 
bool receive = false;

int middleValue;
int DIFFERENCE=10;
int sensorValue;

String data_raw = "";
String data_final = "";

char inByte;

void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(10);
  receive = true;


  checkMiddle();
}

void loop()
{
  if (receive)
  {
    while(analogRead(A2)>middleValue){ 
     GetData();
    }
  }
}


void checkMiddle() 
{ 
  int difference; 
  middleValue = analogRead(photoPin); 
  do{ 
    sensorValue=analogRead(photoPin); 
    difference= sensorValue - middleValue;
    delay(2); 
    }
  while(difference<DIFFERENCE && difference>-DIFFERENCE); 
  middleValue = (sensorValue + middleValue)/2; 
}

void GetData()
{
    String datastring = "";
    while (analogRead(A2) > middleValue)
    {
      
      if (analogRead(A4) > middleValue)
      {
        datastring += "1";
      }
      else
      {
        datastring += "0";
      }
      delay(sync);
    }
    if (datastring != "")
     {Serial.println(datastring);}
  
}

