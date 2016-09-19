import serial
import time
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
print(ports)
for p in ports:
    x=str(p)
    x=x[0:4]
    print(x)
ser = serial.Serial( x , 9600, timeout=0)
while 1:
    try:
        print (ser.readline())
        time.sleep(1)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)