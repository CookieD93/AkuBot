#import urllib2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

#doc = urllib2.urlopen('http://www.yr.no/place/Denmark/Zealand/Roskilde/forecast_hour_by_hour.xml')

#from xml.dom import minidom

#xmldoc = minidom.parse(doc)

#itemlist = xmldoc.getElementsByTagName('temperature')

#print(itemlist[0].attributes['value'].value)
#nextHourForeTemp = itemlist[0].attributes['value'].value
manTemp = -1

while True:
    p0=GPIO.PWM(14,50)
    p1=GPIO.PWM(15,50)
    p2=GPIO.PWM(18,50)
    p3=GPIO.PWM(23,50)
    if manTemp > 25:
        manTemp = -5
    if manTemp <= -5:
        p0.start(50)
    if manTemp == -4:
        p0.start(50)
        p0.ChangeDutyCycle(60)
    if manTemp == -3:
        p0.start(50)
        p0.ChangeDutyCycle(70)
    if manTemp == -2:
        p0.start(50)
        p0.ChangeDutyCycle(80)
    if manTemp == -1:
        p0.start(50)
        p0.ChangeDutyCycle(90)
    if manTemp == 0:
        p0.start(50)
        p0.ChangeDutyCycle(100)
    if manTemp == 1:
        p1.start(50)
        p1.ChangeDutyCycle(60)
    if manTemp == 2:
        p1.start(50)
        p1.ChangeDutyCycle(70)
    if manTemp == 3:
        p1.start(50)
        p1.ChangeDutyCycle(80)
    if manTemp == 4:
        p1.start(50)
        p1.ChangeDutyCycle(90)
    if manTemp == 5:
        p1.start(50)
        p1.ChangeDutyCycle(100)
    if manTemp == 6:
        p2.start(50)
        p2.ChangeDutyCycle(50)
    if manTemp == 7:
        p2.start(50)
        p2.ChangeDutyCycle(60)
    if manTemp == 8:
        p2.start(50)
        p2.ChangeDutyCycle(65)
    if manTemp == 9:
        p2.start(50)
        p2.ChangeDutyCycle(70)
    if manTemp == 10:
        p2.start(50)
        p2.ChangeDutyCycle(75)
    if manTemp == 11:
        p2.start(50)
        p2.ChangeDutyCycle(80)
    if manTemp == 12:
        p2.start(50)
        p2.ChangeDutyCycle(85)
    if manTemp == 13:
        p2.start(50)
        p2.ChangeDutyCycle(90)
    if manTemp == 14:
        p2.start(50)
        p2.ChangeDutyCycle(100)
    if manTemp == 15:
        p3.start(50)
        p3.ChangeDutyCycle(60)
    if manTemp == 16:
        p3.start(50)
        p3.ChangeDutyCycle(70)
    if manTemp == 17:
        p3.start(50)
        p3.ChangeDutyCycle(80)
    if manTemp == 18:
        p3.start(50)
        p3.ChangeDutyCycle(90)
    if manTemp == 19:
        p3.start(50)
        p3.ChangeDutyCycle(100)
    if manTemp == 20:
        p3.start(50)
        p3.ChangeDutyCycle(50)
    if manTemp == 21:
        p3.start(50)
        p3.ChangeDutyCycle(60)
    if manTemp == 22:
        p3.start(50)
        p3.ChangeDutyCycle(70)
    if manTemp == 23:
        p3.start(50)
        p3.ChangeDutyCycle(80)
    if manTemp == 24:
        p3.start(50)
        p3.ChangeDutyCycle(90)
    if manTemp >= 25:
        p3.start(50)
        p3.ChangeDutyCycle(100)




#        p = GPIO.PWM(14, 50)
 #       p.start(50)
  #      #time.sleep(1)
   #     #time.sleep(1)
    #    p.ChangeDutyCycle(100)
#        #GPIO.output(14, GPIO.HIGH)
#        GPIO.output(15, GPIO.LOW)
#        GPIO.output(18, GPIO.LOW)
#        GPIO.output(23, GPIO.LOW)

 #   if manTemp > 0:
  #      p.stop()  
        #GPIO.output(14, GPIO.LOW)
  #      GPIO.output(15, GPIO.HIGH)
  #      GPIO.output(18, GPIO.LOW)
  #      GPIO.output(23, GPIO.LOW)

   # if manTemp > 5:
    #    GPIO.output(14, GPIO.LOW)
    #    GPIO.output(15, GPIO.LOW)
    #    GPIO.output(18, GPIO.HIGH)
    #    GPIO.output(23, GPIO.LOW)

#    if manTemp > 15:
#        GPIO.output(14, GPIO.LOW)
#        GPIO.output(15, GPIO.LOW)
#        GPIO.output(18, GPIO.LOW)
#        GPIO.output(23, GPIO.HIGH)

    print(manTemp)
    manTemp = manTemp+1
    time.sleep(1)

GPIO.cleanup()



#for s in itemlist:
    #print(s.attributes['value'].value)
    #break

