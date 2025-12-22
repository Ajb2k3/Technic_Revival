import serial
import time
from struct import *
import functools
ser = serial.Serial(
    port='/dev/cu.PL2303G-USBtoUART2420',
    baudrate=9600,
    )

ser.write(b'p\0###Do you byte, when I knock?$$$') #initiates communication with the Control center.
print(ser.read(31))

print(ser.read(19))
