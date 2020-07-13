import serial
import binascii
import sys
import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tqdm import tqdm

ser = serial.Serial('COM16', 115200, timeout=.1) 

print("######################################################\n"
      "##--------------------Debut-------------------------##\n"
      "######################################################\n"
      "##-------------------Recepteur----------------------##\n"
      "##--------------------------------------------------##\n"
      "##------------Commencement de reception-------------##\n"
      "##--------------------------------------------------##\n"
      "######################################################\n"
      )
a = input()

if (a == "i"):
    print(
      "##------------Mode de recpetion d'image--------------##\n"
      "##--------------------------------------------------##\n"
      "||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
      "                                                      \n"
     )
    flag = False
    while True:
        a = ser.readline()
        data = a
        if (len(a) > 0):
            pbar = tqdm(total=100)
            if (not flag):
                n = int(a, 2)
                print(n)
                pic = ""
                picdata = ""
                count = 0
                while len(pic) < n * 8:
                    
                    a = ser.readline()
                    if (len(str(a)) > 15):
                        pic += str(a)[2:17]
                        pbar.update(15 / n / 8 * 100)
                        print('')
                    elif (len(str(a)) > 3):
                        pic += str(a)[2:-5]
                        pbar.update((len(str(a)) - 7) / n / 8 * 100)
                        print('')
                print(pic)
                i = 0
                
                data = [pic[i:i + 8] for i in range(0, len(pic), 8)]
                print(len(data))
                for i in data:
                    data_part = i
                    x = int(data_part, 2)
                    message = chr(x)
                    picdata += message
                print(picdata)
                
                picdata = base64.standard_b64decode(picdata)
                
                fh = open("im.jpg", "wb")
                fh.write(picdata)
                fh.close()
                img = mpimg.imread("im.jpg")
                plt.imshow(img)
                plt.show()
if a=="t" :
    print(
        "##-----------Mode de recpetion de texte-------------##\n"
        "##--------------------------------------------------##\n"
        "||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
        "                                                      \n"
    )
    count = 0
    while(1):
        a = ser.readline()
        data = a
        if(str(data)[2:-5]=="00010"):
            
         print("----------------> No."+(str(count)),"  ",end="")
         while(1):
                a = ser.readline()
                data = a
                if(str(data)[2:-5]=="00011"):
                    print()
                    count+=1
                    break
                if(len(data)>3):
                                        
                    print(chr(int(data,2)),end="")
                    sys.stdout.flush()

