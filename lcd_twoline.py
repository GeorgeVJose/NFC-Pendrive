import sys
import lcd
import time
#sys.path.append('/home/pi/Desktop/lcd')

lcd.GPIO.setwarnings(False)

string1 = sys.argv[-2]
string2 = sys.argv[-1]

lcd.lcd_init()

lcd.GPIO.output(15, True)
time.sleep(0.2)
lcd.GPIO.output(15, False)
time.sleep(0.2)
lcd.GPIO.output(15, True)
time.sleep(0.3)

lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string(string1, 2)

lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
lcd.lcd_string(string2, 2)

time.sleep(0.5)
lcd.GPIO.output(15, False)

#lcd.GPIO.cleanup()

