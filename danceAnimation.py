# Tina Xu and Pet Ramanudom 
# Dance Off 
# Final project 

import Tkinter as tk
import animation1
import random

# This file is invoked from the DanceOff file to animate the dance moves.
# Contains three classes: Flail, Disco, Robot. Flail contains one image
# that moves ("shakes") on the canvas, while Disco and Robot cycle through
# three and four static images, respectively.

###############        
#####FLAIL#####       
############### 

class Flail(animation1.AnimatedObject):
    
    def __init__(self,canvas,filename,x,y):
        self.canvas = canvas
        self.photo = tk.PhotoImage(file = filename) # eg filename= 'small_agnes.gif'
        self.id = self.canvas.create_image(x,y, image=self.photo)
        self.photo_width=self.photo.width()
        self.delta = 7
        
    def move(self):
        # Makes the image 'shake' by changing "self.delta" to -1 one the horizontal
        # position "x" reaches half the photo width subtracted from the canvas width.
        # This changes the direction.
        
        if self.delta > 0:
            x1, y1 = self.canvas.coords(self.id)
            if x1 >= self.canvas.winfo_width()-self.photo_width/2: # bounce back from R wall
                self.delta *= -1
            
        elif self.delta < 0:
            x1, y1 = self.canvas.coords(self.id)
            if x1 <= self.photo_width/2: # bounce back from L wall
                self.delta *= -1
           
        self.canvas.move(self.id,self.delta,1) # move left and right
        
        # Without this "y1" restriction, the photo would slide down and disappear from
        # the canvas. By making the value "-1" if y1 is larger than an arbitrarily
        # small number (we chose 10), we disabled the moving down part of the function
        # above.
           
        if y1 > 10:
            self.canvas.move(self.id,self.delta,-1)    
    
###############        
#####DISCO#####       
###############  

class Disco(animation1.AnimatedObject):
    def __init__(self,canvas,fileList,x,y):
      self.canvas = canvas
      self.fileList = fileList
      self.currentIndex = 0 
      self.photo  = tk.PhotoImage(file = self.fileList[self.currentIndex])
      self.id = self.canvas.create_image(x,y, image=self.photo)
    
    # Toggles the currentIndex between 0 and 1, creates the effect of flipping
    # between the two disco images (fileList[1] and fileList[2]).  
    def move(self):  
        if self.currentIndex == 0:   
          self.currentIndex = 1
        else:
          self.currentIndex = 0 
        self.photo  = tk.PhotoImage(file = self.fileList[self.currentIndex])
        self.canvas.itemconfig(self.id, image=self.photo)
        
###############        
#####ROBOT#####       
###############
    
class Robot(animation1.AnimatedObject):
    def __init__(self,canvas,fileList,x,y):
        self.canvas = canvas
        self.fileList = fileList
        self.currentIndex = 0
        self.photo  = tk.PhotoImage(file = self.fileList[self.currentIndex])
        self.id = self.canvas.create_image(x,y, image=self.photo)
    
    # Uses "%" operator to cycle through the indices of fileList, creating the effect
    # of flipping between the four images of the robot dance.    
    def move(self):  
        self.photo  = tk.PhotoImage(file = self.fileList[self.currentIndex%len(self.fileList)])
        self.canvas.itemconfig(self.id, image=self.photo)
        self.currentIndex +=1
        
        
