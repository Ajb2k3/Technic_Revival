import serial
import time
ser = serial.Serial(
    port='/dev/cu.PL2303G-USBtoUART2420',
    # Set additional parameters if strictly required.
)

ser.write(b'p\0###Do you byte, when I knock?$$$')
print(b'p\0###Do you byte, when I knock?$$$')
print(ser.read(31))
time.sleep(1)

input_bytes = bytearray(ser.read(19))
keepalive = (b'\x02')

## Input ports definition
st = (input_bytes[0:2])
p4 = (input_bytes[2:4])
p8 = (input_bytes[4:6])
p3 = (input_bytes[6:8])
p7 = (input_bytes[8:10])
p2 = (input_bytes[10:12])
p6 = (input_bytes[12:14])
p1 = (input_bytes[14:16])
p5 = (input_bytes[16:18])
cks = (input_bytes[18])

##Prints Unlabeled byte values from input array
print(input_bytes)
print(st)
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(cks)

##Labeled byte values from input array
print(f'STOP: {st}')
print(f'Port1: {p1}')
print(f'Port2: {p2}')
print(f'Port3: {p3}')
print(f'Port4: {p4}')
print(f'Port5: {p5}')
print(f'Port6: {p6}')
print(f'Port7: {p7}')
print(f'Port8: {p8}')
print(f'Checksum: {cks}')

##Creates an int from split up byte array
port4 = int.from_bytes(p4, "big")
print(port4)
print(f'Port4: {port4}')

#stop = int.from_bytes(st, "big")
#print(stop)
#print(f'Stop Button: {stop}')

while True:
    ser.write(keepalive)
    input_bytes = bytearray(ser.read(19)) #For some reason this line must be included in the main loop.
    st = (input_bytes[0:2])
    stop = int.from_bytes(st, "big")
    print(stop)
    print(f'Stop Button: {stop}')
    if stop > 0:
        print('Stop button pressed.')
