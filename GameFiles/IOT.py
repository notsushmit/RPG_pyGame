import matplotlib.pyplot as plt
import numpy as np


class factory:
    def __init__(self):
        pass
    
    


class motor:
    def __init__(self):
        self.modes = {"ON": 1, "OFF":0}
        self.freq = 0
        self.digital_output = 0
        self.analog_output = 0
        self.OVLD = 0
        self.RPM = 0
        self.start=False

        

        
    def turnOn(self):
        self.digital_output = self.modes["ON"]
        
    
    def turnOff(self):
        self.digital_output = self.modes["OFF"]
    
    def setFreq(self, value):
        if value>50:
            self.analog_output = 50
        elif value<0:
            self.analog_output = 0
        else:
            self.analog_output = value
    
    def setOVLD(self):
        self.OVLD= 1
    
    def resetOVLD(self):
        self.OVLD=0
        
    def run(self):
        
            if self.start :
                self.digital_output=True
                
            else:
                self.digital_output=False
    
 
        


import time
import threading

 
        
class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.presetTime = 3
        self.count=0
       

    def run(self):
        
        while self.count <self.presetTime and not self.event.is_set():
            print(self.count)
            self.count += 1
            self.event.wait(1)
        self.count=0
        self.stop()

    def stop(self):
        self.event.set()
        self.count=0
    
    def set_presetTime(self,value):
        self.presetTime = value
        
        

m = motor()
tmr = TimerClass()
#tmr.start()
state ="turnOnTimer"
while(1):
    


        
    if state=="turnOnTimer":
       
        if  tmr.is_alive()==False:
                tmr = TimerClass()
                tmr.start()
                state="waitForTimer"
                m.start=False
    
    elif state=="waitForTimer":
        if tmr.is_alive()==False:
            state="turnOnMotor"
    
    elif  state== "turnOnMotor":
        m.start=True
        m.run()
        tmr = TimerClass()
        tmr.start()        
        state="turnOnTimer"
         
    print(state, m.start, tmr.count)
 

#tmr.stop()        

      
#t = TON() 
#t.start=True
#t.startTimer()
#m=motor() 
#state="timer"
#i=2
#while(1):
#    while(1):
        
      
#        if t.getOutput():
#            print(t.thread.is_alive()) 
#            t.start=True
#            t.startTimer()
#            break

             
         
#print(t.thread.is_alive())   
 #make the timer in a thread. not every run is  a new thread
        
     
        
