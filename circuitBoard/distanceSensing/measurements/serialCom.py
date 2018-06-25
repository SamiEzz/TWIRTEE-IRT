
# -*- coding: utf-8 -*-
"""
_______________________________________________________________________________
|##                                                                         ##|
|##                                                                         ##|
|##                                                                         ##|
|##         Simulation du calcul de la position par Trilateration           ##|
|##                                                                         ##|
|##                                                                         ##|
|##         Tuteur     : JENN Eric                                          ##|
|##         Auteur     : EZZEROUALI Sami                                    ##|
|##                                                                         ##|
|#############################################################################|
"""


import serial

#=======================Class def======================================
class TAG(object):
    def __init__(self):
        self.sline=-1
        #self.lastState=-1
        self.devices=[]
        self.theBigMatrix=[]

        self.anchorsNumber=0
        self.tagPort='/dev/ttyUSB0'
        self.tagBaud=19200
    def loop(self):
        while True:
            if (ser.inWaiting()>0):
                self.sline = ser.readline()
                print(self.sline)
            

    def newDevice(self,id):
        print("new device : "+id)
    def lostDevice(self):
        print("l")
    def newRange(self):
        print("d")
    #-------------------Setters------------------------

    

#=====================================================================
ser = serial.Serial(port="/dev/ttyUSB0", baudrate=19200, timeout=1,writeTimeout=1)
tag = TAG()
tag.loop()


"""
options = { 0:tag.lostDevice,
            1:tag.newDevice,
            2:tag.newRange,
}

with Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1,writeTimeout=1) as serialTag:
    serialTag.open()
    if serialTag.isOpen():
        while true:
            ligne=serialTag.readline()
            options[ligne[0]]()
            """
#=====================================================================








