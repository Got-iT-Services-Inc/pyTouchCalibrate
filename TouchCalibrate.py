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

sys.path.append("/opt/PiStat/pyDebugger")
sys.path.append("/opt/PiStat/pyDrawFBImage")
from Debug import pyDebugger
from DrawFBImage import pyDrawFBImage

class TouchCal():

   def __init__(self):
      self.Debugger = pyDebugger(self,True,False)
      self.Debugger.Log("Starting TouchCal, Touchscreen Calibration Application...")
      self.FirstPos = None
      self.FirstPosOffset = None
      self.SecondPos = None
      self.SecondPosOffset = None
      self.ThirdPos = None
      self.ThirdPosOffset = None
      self.FouthPos = None
      self.FourthPosOffset = None
      self.FifthPos = None
      self.FifthPosOffset = None
      self.XOffset = None
      self.YOffset = None
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
      self.DFBI.Update(True)
      self.Debugger.Log("Initial Crosshairs Displayed...")

      while True:
         #Pickup Mouse Events
         #self.Debugger.Log("Checking for mouse events...")
         bEvent = False
         tEvents = self.DFBI.getEvents()
         for Tevent in tEvents:
            if Tevent.type == self.DFBI.MOUSEBUTTONUP:
               self.Debugger.Log("Mouse up event found!...")
               tPos = self.DFBI.getMousePos()
               self.Debugger.Log("Mouse Located at: " + str(tPos))
               if self.FirstPosOffset == None:
                  self.FirstPosOffset = (tPos[0]-23,tPos[1]-22)
                  self.FirstPos = tPos
                  self.Debugger.Log("Mouse Offset is: " + str(self.FirstPosOffset))
                  self.DFBI.ClearAllSprites()
                  #Draw the Second Crosshair
                  self.Debugger.Log("Loading Crosshairs...")
                  self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),(10,self.DFBI.FBSize[1] - 35,0,0))
                  self.DFBI.All_Sprites.add(self.CX)
                  self.DFBI.Update(True)
                  self.Debugger.Log("Second Crosshairs Displayed...")

               elif self.SecondPosOffset == None:
                  self.SecondPosOffset = (tPos[0]-23,tPos[1] - (self.DFBI.FBSize[1]-23))
                  self.SecondPos = tPos
                  self.Debugger.Log("Mouse Offset is: " + str(self.SecondPosOffset))
                  self.DFBI.ClearAllSprites()
                  #Draw the Third Crosshair
                  self.Debugger.Log("Loading Crosshairs...")
                  self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),(self.DFBI.FBSize[0]-35,self.DFBI.FBSize[1]-35,0,0))
                  self.DFBI.All_Sprites.add(self.CX)
                  self.DFBI.Update(True)
                  self.Debugger.Log("Third Crosshairs Displayed...")
               elif self.ThirdPosOffset == None:
                  self.ThirdPosOffset = (tPos[0]-(self.DFBI.FBSize[0]-22),tPos[1]-(self.DFBI.FBSize[1]-22))
                  self.ThirdPos = tPos
                  self.Debugger.Log("Mouse Offset is: " + str(self.ThirdPosOffset))
                  self.DFBI.ClearAllSprites()
                  #Draw the Fourth Crosshair
                  self.Debugger.Log("Loading Crosshairs...")
                  self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),(self.DFBI.FBSize[0]-35,10,0,0))
                  self.DFBI.All_Sprites.add(self.CX)
                  self.DFBI.Update(True)
                  self.Debugger.Log("Fourth Crosshairs Displayed...")
               elif self.FourthPosOffset == None:
                  self.FourthPosOffset = (tPos[0]-(self.DFBI.FBSize[0]-22),tPos[1] -22)
                  self.FourthPos = tPos
                  self.Debugger.Log("Mouse Offset is: " + str(self.FourthPosOffset))
                  self.DFBI.ClearAllSprites()
                  #Draw the Fifth Crosshair
                  self.Debugger.Log("Loading Crosshairs...")
                  self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),((self.DFBI.FBSize[0]/2)-13,(self.DFBI.FBSize[1]/2)-13,0,0))
                  self.DFBI.All_Sprites.add(self.CX)
                  self.DFBI.Update(True)
                  self.Debugger.Log("Fifth Crosshairs Displayed...")

               elif self.FifthPosOffset == None:
                  self.FifthPosOffset = (tPos[0]-(self.DFBI.FBSize[0]/2),tPos[1] -22)
                  self.FifthPos = tPos
                  self.Debugger.Log("Mouse Offset is: " + str(self.FifthPosOffset))
                  self.DFBI.ClearAllSprites()
                  #Draw all four Crosshair
                  self.Debugger.Log("Loading Crosshairs...")
                  self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),(self.DFBI.FBSize[0]-35,10,0,0))
                  self.DFBI.All_Sprites.add(self.CX)
                  self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),(self.DFBI.FBSize[0]-35,self.DFBI.FBSize[1]-35,0,0))
                  self.DFBI.All_Sprites.add(self.CX)
                  self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),(10,self.DFBI.FBSize[1] - 35,0,0))
                  self.DFBI.All_Sprites.add(self.CX)
                  self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),(10,10,0,0))
                  self.DFBI.All_Sprites.add(self.CX)
                  self.CX = self.DFBI.pySprite("./crosshairs.png",(0,0,0),((self.DFBI.FBSize[0]/2)-23,(self.DFBI.FBSize[1]/2)-23,0,0))
                  self.DFBI.All_Sprites.add(self.CX)
                  self.DFBI.Update(True)
                  self.Debugger.Log("All Crosshairs Displayed...")
                  self.Calculate_Offset_Formula()
               else:
                  self.Debugger.Log("Mouse First Offset is:" + str(self.FirstPosOffset))
                  self.Debugger.Log("Mouse Second Offset is:" + str(self.SecondPosOffset))
                  self.Debugger.Log("Mouse Third Ofsett is:" + str(self.ThirdPosOffset))
                  self.Debugger.Log("Mouse Fourth Ofsett is:" + str(self.FourthPosOffset))
                  self.Debugger.Log("Mouse Fifth Ofsett is:" + str(self.FifthPosOffset))

                  self.Debugger.Log("X offset Calculated at: " + str(self.AdjustMousePos(tPos)))
                  break


         if bEvent == False:
            #self.Debugger.Log("Sleeping for 2 Seconds...")
            time.sleep(2)

   def Calculate_Offset_Formula(self):
      if self.FirstPos == None or self.SecondPos == None or self.ThirdPos == None or self.FourthPos == None or self.FifthPos == None:
         return none
      else:
         self.XOffset = self.Calc_Parabola_Three_Points(self.FirstPosOffset[0],self.FifthPosOffset[0],self.FourthPosOffset[0],self.FirstPos[0],self.FifthPos[0],self.FourthPos[0])
         self.YOffset = self.Calc_Parabola_Three_Points(self.FirstPosOffset[1],self.FifthPosOffset[1],self.FourthPosOffset[1],self.FirstPos[1],self.FifthPos[1],self.FourthPos[1])

   def Calc_Parabola_Three_Points(self,yA,yB,yC,xA,xB,xC):
         #Lets calc X-Axis First
         #yA = self.FirstPosOffset[0]
         #yB = self.FifthPosOffset[0]
         #yC = self.FourthPosOffset[0]

         #xA = self.FirstPos[0] #+ self.FirstPosOffset[0]
         #xB = self.FifthPos[0] #+ self.FourthPosOffset[0]
         #xC = self.FourthPos[0] #+ self.FifthPosOffset[0]

         #Debug Info
         self.Debugger.Log("yA: " + str(yA))
         self.Debugger.Log("yB: " + str(yB))
         self.Debugger.Log("yC: " + str(yC))

         self.Debugger.Log("xA: " + str(xA))
         self.Debugger.Log("xB: " + str(xB))
         self.Debugger.Log("xC: " + str(xC))


         aA = None
         aB = None
         aC = None

         bA = None
         bB = None
         bC = None

         cA = None
         cB = None
         cC = None

         #Lets Calc the first set of each formula
         fyA = (yA * -1) + yB
         fxaA = ((xA * xA) * -1) + (xB * xB)
         fxaB = (xA * -1) + xB

         fyB = (yB * -1) + yC
         fxbA = ((xB * xB) * -1) + (xC * xC)
         fxbB = (xB * -1) + xC

         fyC = (yA * -1) + yC
         fxcA = ((xA * xA) * -1) + (xC * xC)
         fxcB = (xA * -1) + xC

         #Debug Info
         self.Debugger.Log("fyA: " + str(fyA))
         self.Debugger.Log("fxaA: " + str(fxaA))
         self.Debugger.Log("fxaB: " + str(fxaB))

         self.Debugger.Log("fyB: " + str(fyB))
         self.Debugger.Log("fxbA: " + str(fxbA))
         self.Debugger.Log("fxbB: " + str(fxbB))

         self.Debugger.Log("fyC: " + str(fyC))
         self.Debugger.Log("fxcA: " + str(fxcA))
         self.Debugger.Log("fxcB: " + str(fxcB))


         #Lets Calc for A
         try:
            aA = ((fyA * (fxbB * -1)) + (fyB * fxaB)) / ((fxaA * (fxbB * -1)) + (fxbA * fxaB))
         except Exception as e:
            aA = 0
            self.Debugger.Log("Error: " + str(e))

         try:
            aB = ((fyB * (fxcB * -1)) + (fyC * fxbB)) / ((fxbA * (fxcB * -1)) + (fxcA * fxbB))
         except Exception as e:
            aB = 0
            self.Debugger.Log("Error: " + str(e))

         try:
            aC = ((fyC * (fxaB * -1)) + (fyA * fxcB)) / ((fxcA * (fxaB * -1)) + (fxaA * fxcB))
         except Exception as e:
            aC = 0
            self.Debugger.Log("Error: " + str(e))

         #Debug Info
         self.Debugger.Log("aA: " + str(aA))
         self.Debugger.Log("aB: " + str(aB))
         self.Debugger.Log("aC: " + str(aC))
         if aA == aB and aB == aC and aA == aC:
            self.Debugger.Log("All 'A' Calculations Match!")

         #Lets Calc for B, now that we have A
         try:
            bA = (fyA - (aA * fxaA)) / fxaB
         except Exception as e:
            bA = 0
            self.Debugger.Log("Error: " + str(e))
         try:
            bB = (fyB - (aB * fxbA)) / fxbB
         except Exception as e:
            bB = 0
            self.Debugger.Log("Error: " str(e))
         try:
            bC = (fyC - (aC * fxcA)) / fxcB
         except Exception as e:
            bC = 0
            self.Debugger.Log("Error: " str(e))

         #Debug Info
         self.Debugger.Log("bA: " + str(bA))
         self.Debugger.Log("bB: " + str(bB))
         self.Debugger.Log("bC: " + str(bC))
         if bA == bB and bB == bC and bA == bC:
            self.Debugger.Log("All 'B' Calculations Match!")

         #Lets Calc for C, now that we have A and B
         cA = yA - ((aA * (xA * xA)) + (bA * xA))
         cB = yB - ((aB * (xB * xB)) + (bB * xB))
         cC = yC - ((aC * (xC * xC)) + (bC * xC))

         #Debug Info
         self.Debugger.Log("bA: " + str(cA))
         self.Debugger.Log("bB: " + str(cB))
         self.Debugger.Log("bC: " + str(cC))
         if cA == cB and cB == cC and cA == cC: 
            self.Debugger.Log("All 'C' Calculations Match!")

         #Check for value in a, then B, then C, and choose the first with a value
         if aA != None:
            self.XOffset = (aA, bA, cA)
         elif bA != None:
            self.XOffset = (bA, bB, bC)
         elif cA != None:
            self.XOffset = (cA, cB, cC)
         else:
            self.XOffset = (0,0,0)

   def AdjustMousePos(self,mPos=None):
      if mPos != None and self.XOffset != None:
         fx = (self.XOffset[0] * (mPos[0] * mPos[0])) + (self.XOffset[1] * mPos[0]) + self.XOffset[2]
         fy = (self.YOffset[0] * (mPos[1] * mPos[1])) + (self.YOffset[1] * mPos[1]) + self.YOffset[2]
         return (mPos[0] - fx, mPos[1] - fy)

if __name__ == '__main__':

   TC = TouchCal()
   TC.StartCal()
