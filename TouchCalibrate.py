#! /usr/bin/env python3
#############################################################
# Title: pyTouchCalibrate                                   #
# Description: Creates an offset file for use with          #
#   framebuffer graphical applications.			    #
#                                                           #
# Version:                                                  #
#   * Version 1.0 01/01/2018 RC                             #
#                                                           #
# Author: Richard Cintorino (c) Richard Cintorino 2018      #
#############################################################

import os,sys,inspect,time

sCurPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory

from Debug import pyDebugger
from DrawFBImage import pyDrawFBImage

class TouchCal():

   def __init__(self):
      self.Debugger = pyDebugger(self,True,False)
      self.Debugger.Log("Starting TouchCal, Touchscreen Calibration Application...")

      self.DFBI = pyDrawFBImage()

   def StartCal(self):
      self.Debugger.Log("Starting Calibration Process...")
      self.DFBI.ClearAllSprites()
      self.DFBI.ShowMouse(False)
      self.DFBI.gBackground = self.DFBI.FillSurface(self.DFBI.FBSize,(255,255,255))
      self.DFBI.FBScreen.fill((255,255,255))
      self.DFBI.Update()

      #Draw the First Crosshair
      self.Debugger.Log("Loading Crosshairs...")
      self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),(10,10,0,0))
      self.DFBI.All_Sprites.add(self.CX)
      self.DFBI.Update()
      self.Debugger.Log("Initial Crosshairs Displayed...")

      while True:
         self.Debugger.Log("Wait 1 Second...")
         time.sleep(1)


if __name__ == '__main__':

   TC = TouchCal()
   TC.StartCal()
