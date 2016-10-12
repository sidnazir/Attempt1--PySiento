"""This code
 1)Initialize a serial communication (COM port)
 2)Receive the data from it
 3) write it to a dict
 4)Parse it to Json"""
import serial
import time
import serial.tools.list_ports
import json
#Detecting the connected port
ports = list(serial.tools.list_ports.comports())
print(ports)
for p in ports:
    x=str(p)
    x=x[0:4]
    print(x)
#Initialize the connection
ser = serial.Serial( x , 9600, timeout=0)
#Reading The data
while 1:
    try:
        val=ser.readline()
        list1 = list() #making a BPR list
        list2 = list() #making a Skin conductance
        val = str.split() #spliting the recieved line of data to BPR and Skin conductance
        list1.append(val[0]) #adding data to BPR list
        list2.append(val[1]) #adding data to skin conductance list
        data_dict = {"BPR": list1, "Skin conductance": list2} #making a dict
        data_Json = json.dumps(data_dict) #parse into json
    except ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)
