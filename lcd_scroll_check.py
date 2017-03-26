import sys
import lcd
import time
import urllib2

lcd.GPIO.setwarnings(False)

#subprocess.Popen('sudo explorenfc-wifi-connect ', shell = True , stdout = subprocess.PIPE,stderr = subprocess.STDOUT)
#print "Subprocess Opened"

def check_connection():
	try :
		urllib2.urlopen("http://192.168.100.1", timeout=5)
	except urllib2.URLError as err:
		return False

string = sys.argv[-2]
line = sys.argv[-1]

string = '                '+string
lcd.lcd_init()

lcd.GPIO.output(15, True)
time.sleep(0.5)
lcd.GPIO.output(15, False)
time.sleep(0.5)
lcd.GPIO.output(15, True)
time.sleep(0.5)
 

lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
lcd.lcd_string("NFC PENDRIVE ", 2)

if line == 1:
	lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
elif line == 2:
	lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)

while True:
	for i in range(len(string)-15):
		lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
		str = string[ i : (i+16)]
		lcd.lcd_string(str, 2)
		time.sleep(0.3)
		i = i+1
		if not check_connection():
			pass
		else:
			break

print "Connected......"

time.sleep(3)
lcd.GPIO.output(15, False)

lcd.GPIO.cleanup()

