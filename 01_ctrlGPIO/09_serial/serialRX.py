import RPi.GPIO as GPIO
import serial
import io

ser = serial.serial_for_url('/dev/ttyUSB0', 115200, timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

rcv = ""

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

try:
  while(1):
    
    rcv = sio.readline()
    
    if(rcv != ""):
      print unicode(rcv)
      
      if( unicode(rcv[0:3]) == "red" ):
        if( rcv[3] == "1" ):
          GPIO.output(23, True )
          print "RED On"
        else:
          GPIO.output(23, False)
          print "RED Off"
         
      elif( unicode(rcv[0:3]) == "grn" ):
        if( rcv[3] == "1" ):
          GPIO.output(24, True )
          print "GREEN On"
        else:
          GPIO.output(24, False)
          print "GREEN Off"
      else:
        pass
      
except KeyboardInterrupt:
  print "\n", "program terminated by user!"
  GPIO.cleanup()
  sio.flush()