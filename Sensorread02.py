import serial
import time
from struct import *
import functools
ser = serial.Serial(
    port='/dev/cu.PL2303G-USBtoUART2420',
    baudrate=9600,
    )


ser.write(b'p\0###Do you byte, when I knock?$$$') #initiates communication with the Control center.
print(ser.read(31))  # Check  to see if the Interface has responded. Stop LED should go off.

while True:
    ser.write(b'2')
    dat = ser.read(19)
    print(dat)
    STOP, p4, p8, p3, p7, p2, p6, p1, p5 = unpack('<hhhhhhhhh', dat[:-1])
    print(STOP, p1, p2, p3, p4, p5, p6, p7, p8)