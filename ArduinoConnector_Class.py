import serial
import time
import serial.tools.list_ports
import json


class Connection(object):
    def __init__(self):
        self.ports = list(serial.tools.list_ports.comports())
        print(self.ports)
        for p in self.ports:
            x = str(p)
            x = x[0:4]
            print("Connecting on %r" % x)
        # Initialize the connection
        self.ser = serial.Serial(x, 9600, timeout=0)

    def get_data(self):
        while 1:
            try:
                val = self.ser.readline()
                list1 = list()  # making a BPR list
                list2 = list()  # making a Skin conductance
                val = str.split()  # spliting the recieved line of data to BPR and Skin conductance
                list1.append(val[0])  # adding data to BPR list
                list2.append(val[1])  # adding data to skin conductance list
                data_dict = {"BPR": list1, "Skin conductance": list2}  # making a dict
                data_Json = json.dumps(data_dict)  # parse into json
            except self.ser.SerialTimeoutException:
                print('Data could not be read')
                time.sleep(1)



