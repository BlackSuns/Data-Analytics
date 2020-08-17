import time
import threading
try:
		for i in range(0,3):
			file =open("/sys/class/leds/apq8016-sbc:green:user3/brightness","w")
			file.write("1")
			file.close()
			time.sleep(2)
			file =open("/sys/class/leds/apq8016-sbc:green:user3/brightness","w")
			file.write("0")
			file.close()
			time.sleep(2)
		for i in range(0,3):
			file =open("/sys/class/leds/apq8016-sbc:green:user2/brightness","w")
			file.write("1")
			file.close()
			time.sleep(1)
			file =open("/sys/class/leds/apq8016-sbc:green:user2/brightness" ,"w")
			file.write("0")
			file.close()
			time.sleep(1)
		for i in range(0,3):
			file =open("/sys/class/leds/apq8016-sbc:green:user2/brightness","w")
                        file1 =open("/sys/class/leds/apq8016-sbc:green:user3/brightness","w")
			file.write("1")
			file1.write("1")
			file.close()
			file1.close()
			time.sleep(1)
			file =open("/sys/class/leds/apq8016-sbc:green:user2/brightness","w")
			file1 =open("/sys/class/leds/apq8016-sbc:green:user3/brightness","w")
			file.write("0")
			file1.write("0")
			file.close()
			file1.close()
			time.sleep(1)
except IOError:
	print"Error"

