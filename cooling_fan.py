import os
import RPi.GPIO as IO          # calling header file which helps us use GPIOs of PI
import time                             # calling time to provide delays in program

#Variable Declaration
BCM_output_pin=18
ontemp=60   #in deg C         
offtemp=55  #in deg C
max_fan_speed=80	# maximum speed in percent 0-100

#DO NOT EDIT BELOW THIS -------------------------------------------
IO.setwarnings(False)            #do not show any warnings
IO.setmode (IO.BCM)           #we are programming the GPIO by BCM pin numbers. (PIN35 as GPIO19)
IO.setup(BCM_output_pin, IO.OUT)         # initialize GPIO13 as an output.

p = IO.PWM(BCM_output_pin, 100)        #GPIO13 as PWM output, with 100Hz frequency
p.start(0)                            #generate PWM signal with 0% duty cycle

# Return CPU temperature as a character string
def getTemp():
   res = os.popen('vcgencmd measure_temp').readline()
   return(res.replace("temp=","").replace("'C\n",""))

x=0
curtemp=0
fanOn=False
trackingtemp=0

try:
#   print("Fan control start...")
   while 1:

      temp=int(float(getTemp()))
      if temp>=ontemp:
         if curtemp!=temp:
            if not fanOn:
#               print("Temp: %d. Fan start." % (temp))
               trackingtemp=0
            curtemp=temp
         x=max_fan_speed
         fanOn=True
         p.ChangeDutyCycle(x)

      elif temp<=offtemp:
         if curtemp!=temp:
            if fanOn:
#               print("Temp: %d. Fan stop." % (temp))
               trackingtemp=0
            curtemp=temp
         x=0
         fanOn=False
         p.ChangeDutyCycle(x)

      else:
         if curtemp!=temp:
            curtemp=temp
            if curtemp!=trackingtemp:
               if fanOn:
                  pass
#                  print("Temp: %d. Fan running" % (temp))
               else:
                  pass
#                  print("Temp: %d. Fan idle" % (temp))
               trackingtemp=curtemp
      time.sleep(0.5)

except KeyboardInterrupt:
   pass
except:
   pass
finally:
#   print("\nFan control stop")
   IO.cleanup()
