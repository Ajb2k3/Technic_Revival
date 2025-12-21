import serial
import time
from struct import *
ser = serial.Serial(
    port='/dev/cu.PL2303G-USBtoUART2420',
    baudrate=9600,
    )

print("hello")
ser.write(b'p\0###Do you byte, when I knock?$$$')
print("Knock, knock")
print(ser.read(31))
print("Lets looks at the input ports")

while True:
    ser.write(b'2')
    dat = ser.read(19)
    print("is anything there?")
#    b_data = ser.read(19)
#    print(b_data)
    print(dat)
    ser.write(b'\x91\x01') #Turns on Motor Port A
    time.sleep(0.5)
    ser.write(b'\x91\x02') #Turns on Motor Port B
    time.sleep(0.5)
    ser.write(b'\x91\x04') #Turns on Motor Port C
    time.sleep(0.5)
    ser.write(b'\x91\x08') #Turns on Motor Port D
    time.sleep(0.5)
    ser.write(b'\x91\x10') #Turns on Motor Port E
    time.sleep(0.5)
    ser.write(b'\x91\x20') #Turns on Motor Port F
    time.sleep(0.5)
    ser.write(b'\x91\x40') #Turns on Motor Port G
    time.sleep(0.5)
    ser.write(b'\x91\x80') #Turns on Motor Port H
    time.sleep(0.5)
    ser.write(b'\x90\x01') #Turns off Motor Port A
    time.sleep(0.5)
    ser.write(b'\x90\x02') #Turns off Motor Port B
    time.sleep(0.5)
    ser.write(b'\x90\x04') #Turns off Motor Port C
    time.sleep(0.5)
    ser.write(b'\x90\x08') #Turns off Motor Port D
    time.sleep(0.5)
    ser.write(b'\x90\x10') #Turns off Motor Port E
    time.sleep(0.5)
    ser.write(b'\x90\x20') #Turns off Motor Port F
    time.sleep(0.5)
    ser.write(b'\x90\x40') #Turns off Motor Port G
    time.sleep(0.5)
    ser.write(b'\x90\x80') #Turns off Motor Port H
    time.sleep(0.5)
