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
    pt1 = p1 + 14081
    pt2 = p2 + 14081
    pt3 = p3 + 14081
    pt4 = p4 + 14081
    pt5 = p5 + 13057
    pt6 = p6 + 13057
    pt7 = p7 + 13057
    pt8 = p8 + 13057
    print(f'STOP: {STOP}')
    print(f'Port1: {pt1}')
    print(f'Port2: {pt2}')
    print(f'Port3: {pt3}')
    print(f'Port4: {pt4}')
    print(f'Port5: {pt5}')
    print(f'Port6: {pt6}')
    print(f'Port7: {pt7}')
    print(f'Port8: {pt8}')