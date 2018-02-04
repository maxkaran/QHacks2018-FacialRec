import sys
import time
import mraa

TURNONMABITCH = mraa.Gpio(23)

TURNONMABITCH.dir(mraa.DIR_OUT)
TURNONMABITCH.write(1)

time.sleep(5)

TURNONMABITCH.write(0)

print "\nDone"