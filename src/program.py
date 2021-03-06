#!/usr/bin/python

import wiringpi
import time
import sdnotify

n = sdnotify.SystemdNotifier()
n.notify("READY=1")

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(21, 1)

while True:
    wiringpi.digitalWrite(21, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(21, 0)
    time.sleep(0.5)
    n.notify("WATCHDOG=1")

