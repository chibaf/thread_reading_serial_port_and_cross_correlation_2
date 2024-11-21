import serial, sys

ser=serial.Serial(sys.argv[1],sys.argv[2])
print("connected to: " + ser.portstr)
while True:
  line = ser.readline()
  print(line)
ser.close()
