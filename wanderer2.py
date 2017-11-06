from create2 import *
from time import sleep

bot1 = Connect("192.168.1.106", 2030)        ## Connect to bot1
print("Connected")                            ## Notify user of successful connection

bot2 = Connect("192.168.1.108", 2030)        ## Connect to second bot2
print("Connected")                           ## Notify user of successful connection

while True:
    while ReadBumpSensors(bot1) == 0:            ## No collisions detected
        Drive(bot1, 500, 32768)        ## Drive forward at full speed

    if ReadBumpSensors(bot1) == 1:           ## Right bump sensor is pressed
        print('Right-side collision detected')
#        ReadAngleTurned(bot1)                  ## Clear counter

        Drive(bot1, -400, 32768)
        sleep(.25)
        ## Wait until bot1 turns left 90 degrees
        Drive(bot1, 200, 1)
#        while ReadAngleTurned(bot1) <= 90:
#            pass
        sleep(.75)
            
    elif ReadBumpSensors(bot1) == 2:           ## Left bump sensor is pressed
        print('Left-side collision detected')
#        ReadAngleTurned(bot1)                  ## Clear counter
        
        Drive(bot1, -400, 32768)
        sleep(.25)
        ## Wait until bot1 turns right 90 degrees
        Drive(bot1, 200, -1)
#        while ReadAngleTurned(bot1) <= 90:
#            pass
        sleep(.75)

    elif ReadBumpSensors(bot1) == 3:           ## Both bump sensors are pressed (head on collision)
        print('Head on collision detected')
#        ReadAngleTurned(bot1)                  ## Clear counter
        
        Drive(bot1, -400, 32768)
        
        sleep(.25)
        ## Wait until bot1 has turned 135 degrees
        Drive(bot1, 200, -1)
#        while ReadAngleTurned(bot1) <= 135:
#            pass
        sleep(.75)
    
    while ReadBumpSensors(bot2) == 0:            ## No collisions detected
        Drive(bot2, 500, 32768)        ## Drive forward at full speed

    if ReadBumpSensors(bot2) == 1:           ## Right bump sensor is pressed
        print('Right-side collision detected')
#        ReadAngleTurned(bot2)                  ## Clear counter

        Drive(bot2, -400, 32768)
        sleep(.25)
        ## Wait until bot2 turns left 90 degrees
        Drive(bot2, 200, 1)
#        while ReadAngleTurned(bot2) <= 90:
#            pass
        sleep(.75)
            
    elif ReadBumpSensors(bot2) == 2:           ## Left bump sensor is pressed
        print('Left-side collision detected')
#        ReadAngleTurned(bot2)                  ## Clear counter
        
        Drive(bot2, -400, 32768)
        sleep(.25)
        ## Wait until bot2 turns right 90 degrees
        Drive(bot2, 200, -1)
#        while ReadAngleTurned(bot2) <= 90:
#            pass
        sleep(.75)

    elif ReadBumpSensors(bot2) == 3:           ## Both bump sensors are pressed (head on collision)
        print('Head on collision detected')
#        ReadAngleTurned(bot2)                  ## Clear counter
        
        Drive(bot2, -400, 32768)
        
        sleep(.25)
        ## Wait until bot2 has turned 135 degrees
        Drive(bot2, 200, -1)
#        while ReadAngleTurned(bot2) <= 135:
#            pass
        sleep(.75)