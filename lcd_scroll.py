import sys
import lcd
import time
import subprocess
import urllib2
#sys.path.append('/home/pi/Desktop/lcd')

#lcd.GPIO.setwarnings(False)

string1 = sys.argv[-3]
string2 = sys.argv[-2]
line = sys.argv[-1]

string1 = '                '+string1
lcd.lcd_init()

lcd.GPIO.output(15, True)
time.sleep(0.5)
lcd.GPIO.output(15, False)
time.sleep(0.5)
lcd.GPIO.output(15, True)
time.sleep(0.5)
 
lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
lcd.lcd_string(string2, 2)

if line == 1:
	lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
elif line == 2:
	lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)


for i in range(len(string1)-15):
	lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
	str = string1[ i : (i+16)]	
	lcd.lcd_string(str, 2)
	time.sleep(0.3)
	i = i+1

time.sleep(1)
lcd.GPIO.output(15, False)

lcd.GPIO.cleanup()

