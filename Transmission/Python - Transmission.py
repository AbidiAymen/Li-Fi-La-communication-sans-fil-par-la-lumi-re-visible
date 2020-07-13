import serial
import binascii
import sys
import random
from tqdm import tqdm
import base64
import time

def pic(s):
   
    with open(s,"rb") as imageFile:
        strr = base64.b64encode(imageFile.read())
        print(str(strr)[2:-1])
        return str(strr)[2:-1]
def bin_str(s):
    
    data = ""
    for i in s:
        temp = str(bin(ord(i)))[2:]
        data +=temp.rjust(8,'0')
    return data

ser = serial.Serial('COM6',115200,timeout=.1) 
print("######################################################\n"
      "##--------------------Debut-------------------------##\n"
      "######################################################\n"
      "##-----------------Transmetteur---------------------##\n"
      "##--------------------------------------------------##\n"
      "##----------Commencement de transmission------------##\n"
      "##--------------------------------------------------##\n"
      "######################################################\n"
      )

img_link="C:\exp4.jpg"
test = ["I  P  E  S  T",
        "IPEST",
        ":-)",
        "Happy",
        "6666",
        "2018-2019",
        "I P E S T"]

while(not "DONE".encode() in ser.readline()):
    pass
flag = False
while True:
    a = input()
    
    if (a=="i"):
        print(
            "##-------------Transmitting Image Mode--------------##\n"
            "##--------------------------------------------------##\n"
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
            "                                                      \n"
        )
        pbar = tqdm(total=100)   
        t0 = time.clock()        
        data = bin_str(pic(img_link))
        temp = len(data)
        
        data = [ data[i:i+15] for i in range(0, len(data), 15) ]
        
        ser.write(bytes("{0:b}".format(temp//8).rjust(15,'0')+"\n",encoding="ascii"))
        print(temp//8)
        ser.flush()
        print(len(data))
        
        while(not "DONE".encode() in ser.readline()):
            pass
        
        for i in range(len(data)):
            ser.write(bytes(data[i]+"\n",encoding="ascii"))
            ser.flush()
            pbar.update((1/len(data))*100)
            while(not "DONE".encode() in ser.readline()):
                pass
            print("Done ")
        print(bin_str(pic(img_link)))
        print(time.clock()-t0)
                        
    if(a=="t"):
        print(
            "##-----------Mode de transmission d'image-----------##\n"
            "##--------------------------------------------------##\n"
            "##        Ecrire ce que vous voulez envoyer         ##\n"
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
            "                                                      \n"
        )
        count = 0
        while(1):
            data = input()
            print("No."+str(count)+" -- Raw Data: ")
            
            ser.write(bytes("00010\n",encoding="ascii"))
            ser.flush()
            while(not "DONE".encode() in ser.readline()):
                    pass
            
            for i in data:
                ser.write(bytes(str(bin(ord(i))).rjust(8,'0')+"\n",encoding="ascii"))
                ser.flush()
                print(bytes(str(bin(ord(i))).rjust(8,'0'), encoding="ascii"),end="")
                while(not "DONE".encode() in ser.readline()):
                    pass
            
            ser.write(bytes("00011\n",encoding="ascii"))
            ser.flush()
            print()
            count+=1
            while(not "DONE".encode() in ser.readline()):
                    pass
    if (a=="auto"):
        print(
            "##----------Auto Transmitting Text Mode-------------##\n"
            "##--------------------------------------------------##\n"
            "||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
            "VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV\n"
            "                                                      "
        )
        last = -1
        count = 0
        while (1):
            
            temp = random.randint(0, len(test) - 1)
            while(temp ==last):
                temp = random.randint(0, len(test) - 1)
            last = temp
            data = test[temp]
           
            print("No."+str(count)+"--->   "+str(data))
            count+=1
            ser.write(bytes("00010\n", encoding="ascii"))
            ser.flush()
            while (not "DONE".encode() in ser.readline()):
                pass
            for i in data:
                ser.write(bytes(str(bin(ord(i))).rjust(8, '0') + "\n", encoding="ascii"))
                ser.flush()
                while (not "DONE".encode() in ser.readline()):
                    pass

            ser.write(bytes("00011\n", encoding="ascii"))
            ser.flush()
            while (not "DONE".encode() in ser.readline()):
                pass
            time.sleep(1)
