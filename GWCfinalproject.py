# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 21:24:49 2021

@author: indig
"""
#Doppler effect simulator

import winsound

def DopplerInfo():
  print("Press space, then enter, to go to the next part of the explanation.")
  keepgoing = input("The doppler effect is an increase (or decrease) in the frequency of sound, light, or other waves as the source and observer move toward (or away from) each other.")
  if keepgoing == " ":
    keepgoing2 = input("The effect causes the sudden change in pitch noticeable in a passing siren, as well as the redshift seen by astronomers.")
    if keepgoing2 == " ":
      keepgoing3 = input("The observed frequency can be calculated if someone knows the actual frequency of the sound or light waves, observer velocity, source velocity, and speed of sound (which is 343m/s at room temperature) or speed of light (which is 3x10^8m/s).")
      if keepgoing3 == " ":
        keepgoing4 = input("The equation for this is: observed frequency = ((speed of sound + observer velocity) divided by (speed of sound + source velocity.)), times the actual frequency.")
        if keepgoing4 == " ":
          print("You have now read the explanation. Now let's try simulating it!")
          MainFunction()

def RunSimulatorSound():
  actualFrequency = int(input("Type a number for the actual frequency of the signal, in Hz, between 20 and 20000."))
  observerVelocity = int(input("Type a number for the observer's velocity, in m/s."))
  sourceVelocity = int(input("Type a number for the source's velocity, in m/s."))
  perceivedFrequency = actualFrequency*((observerVelocity+334)/(sourceVelocity+334))
  print('The frequency that the observer perceives is',str(perceivedFrequency),".")
  print('Here is the sound of the actual frequency, then the sound of the perceived frequency.')
  winsound.Beep(actualFrequency,3000)
  winsound.Beep(int(perceivedFrequency),3000)
  userchoice = input('Would you like to try the other simulator now? Type Y if so.')
  if userchoice == 'Y':
      RunSimulatorLight()

#This function is not my code!! It is javascript code I found on an online simulator, rewrote in python, and modified slightly to integrate into the rest of my program. It was found on https://academo.org/demos/wavelength-to-colour-relationship/
def nmToRGB(wavelength):
        Gamma = 0.80
        IntensityMax = 255
        if((wavelength >= 380) and (wavelength<440)):
            red = -(wavelength - 440) / (440 - 380)
            green = 0.0
            blue = 1.0
        elif((wavelength >= 440) and (wavelength<490)):
            red = 0.0
            green = (wavelength - 440) / (490 - 440)
            blue = 1.0
        elif((wavelength >= 490) and (wavelength<510)):
            red = 0.0
            green = 1.0
            blue = -(wavelength - 510) / (510 - 490)
        elif((wavelength >= 510) and (wavelength<580)):
            red = (wavelength - 510) / (580 - 510)
            green = 1.0
            blue = 0.0
        elif((wavelength >= 580) and (wavelength<645)):
            red = 1.0
            green = -(wavelength - 645) / (645 - 580)
            blue = 0.0
        elif((wavelength >= 645) and (wavelength<781)):
            red = 1.0
            green = 0.0
            blue = 0.0
        else:
            red = 0.0
            green = 0.0
            blue = 0.0
        #Let the intensity fall off near the vision limits
        if((wavelength >= 380) and (wavelength<420)):
            factor = 0.3 + 0.7*(wavelength - 380) / (420 - 380)
        elif((wavelength >= 420) and (wavelength<701)):
            factor = 1.0
        elif((wavelength >= 701) and (wavelength<781)):
            factor = 0.3 + 0.7*(780 - wavelength) / (780 - 700);
        else:
            factor = 0.0
        if (red != 0):
            red = (IntensityMax * ((red * factor)**Gamma))
        if (green != 0):
            green = (IntensityMax * ((green * factor)**Gamma))
        if (blue != 0):
            blue = (IntensityMax * ((blue * factor)**Gamma))
        return([int(red),int(green),int(blue)])

RESET = '\033[0m'
def get_color_escape(r, g, b):
    return '\033[{};2;{};{};{}m'.format(38, r, g, b)

def RunSimulatorLight():
  actualFrequency = int(input("Type a number for the actual frequency of the signal, in Hz, between 4x10^14 and 8*10^14."))
  observerVelocity = int(input("Type a number for the observer's velocity, in m/s."))
  sourceVelocity = int(input("Type a number for the source's velocity, in m/s."))
  perceivedFrequency = actualFrequency*((observerVelocity+299792458)/(sourceVelocity+299792458))
  print('The frequency that the observer perceives is',str(perceivedFrequency),".")
  oldwavelength = (299792458/actualFrequency)*1000000000
  newwavelength = (299792458/perceivedFrequency)*1000000000
  print("Its original color was",get_color_escape(nmToRGB(oldwavelength)[0],nmToRGB(oldwavelength)[1],nmToRGB(oldwavelength)[2]),'this.')
  print(RESET)
  print('Its new color is',get_color_escape(nmToRGB(newwavelength)[0],nmToRGB(newwavelength)[1],nmToRGB(newwavelength)[2]),'this!') 
  print(RESET)
  userchoice = input('Would you like to try the other simulator now? Type Y if so.')
  if userchoice == 'Y':
      RunSimulatorSound()

def RunSimulator():
  userchoice = input('Would you like to run the simulator for sound waves or light waves? Type S for sound, L for light.')
  if userchoice == "S":
    RunSimulatorSound()
  if userchoice == "L":
    RunSimulatorLight()

def MainFunction():
  userchoice = input('Would you like to enter the simulator or learn more about it?\nType Y to enter, N for learning more.')
  if userchoice == "Y":
    RunSimulator()
  if userchoice == "N":
    DopplerInfo()

MainFunction()
