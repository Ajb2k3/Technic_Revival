import serial
ser = serial.Serial(
    port='/dev/cu.PL2303G-USBtoUART2420',
    baudrate=9600,
    )

ser.write(b'p\0###Do you byte, when I knock?$$$')
print(b'###Do you byte, when I knock?$$$')
print(ser.read(31))
ser.write(b'\x91\x01') #Turns on Motor Port A
