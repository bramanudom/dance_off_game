# Tina Xu and Pet Ramanudom 
# Dance Off 
# Final project 

import Tkinter as tk
import os
import animation1 
import danceAnimation
import Image
import ImageTk

# This file creates the DanceGameApp class, which contains the GUI (canvases, widgets,
# buttons for: dance move, head images, start, stop). Running this file invokes the
# danceAnimation.py file to play the dance moves. 
 
class DanceGameApp(tk.Frame,object):
    def __init__(self, root):
        tk.Frame.__init__(self)
        root.title('Dance Off')
        self.grid()
        self.configure(bg='white')
        self.headPictures = ['lyn.gif','rhys.gif','susan.gif','sohie.gif','cat.gif']
        self.createWidgets()
        self.deselectAllRadioButtons()
        
##############        
####CANVAS####       
##############        
        
        # create left and write animation canvases for the two bodies
        
        self.canvasR = animation1.AnimationCanvas(self, width = 150, height = 200,bd=0, highlightthickness=0)
        self.canvasR.config(bg='white')
        self.canvasR.place(x=350,y=130)
        self.canvasR.speed = 60
        self.canvasL = animation1.AnimationCanvas(self, width = 150, height = 200,bd=0, highlightthickness=0)
        self.canvasL.config(bg='white')
        self.canvasL.speed = 60
        self.canvasL.place(x=120,y=130)
        
   
###############        
####WIDGETS####      
###############  
        
    def createWidgets(self):
        #create the title
        
        titlePic = tk.PhotoImage(file='titleImage.gif') # initial image
        self.title = tk.Label(self,image=titlePic,borderwidth=3)
        self.title.titlePic = titlePic
        # position the Label with image on the grid, have it fill the entire space
        self.title.grid(row=0,column=1, columnspan = 3,sticky=tk.N+tk.E+tk.W+tk.S)
  
# start 
        startButton= tk.Button(self, text = 'Start', command = self.startButtonClick) 
        startButton.grid(row =12, column=1, sticky = tk.E) 
    
        stopButton= tk.Button(self, text = 'Stop', command = self.stopButtonClick) 
        stopButton.grid(row =12, column=3, sticky = tk.W) 
    
          
        
###############
###LEFT SIDE###
###############
                    
        # text labels 
        headLabelL = tk.Label(self, text='Pick a Head!', font='TimesRoman 12 bold')
        headLabelL.grid(row=2,column = 0, sticky = tk.W)
        
        danceLabelL = tk.Label(self, text='Pick a Dance Move!', font='TimesRoman 12 bold')
        danceLabelL.grid(row=9,column = 0, sticky = tk.W)
       
        #head buttons Left Side 
        self.headChoiceL = tk.IntVar()
        self.lynButtonL = tk.Radiobutton(self,text = 'Lyn', variable = self.headChoiceL, value = 0 ) 
        self.lynButtonL.grid(row =3, column=0,  sticky = tk.W + tk.E) 
        self.rhysButtonL = tk.Radiobutton(self,text = 'Rhys', variable = self.headChoiceL, value = 1 )
        self.rhysButtonL.grid(row =4, column=0,  sticky = tk.W + tk.E) 
        self.susanButtonL = tk.Radiobutton(self,text = 'Susan', variable = self.headChoiceL, value = 2 )
        self.susanButtonL.grid(row =5, column=0, sticky = tk.W + tk.E) 
        self.sohieButtonL = tk.Radiobutton(self,text = 'Sohie', variable = self.headChoiceL, value = 3 )
        self.sohieButtonL.grid(row =6, column=0, sticky = tk.W + tk.E) 
        self.catButtonL = tk.Radiobutton(self,text = 'Cat', variable = self.headChoiceL, value = 4 )
        self.catButtonL.grid(row =7, column=0, sticky = tk.W + tk.E) 
              
        # dance move buttons Left
        
        self.danceChoiceL = tk.IntVar()
        self.discoButtonL = tk.Radiobutton(self,text = 'Disco', variable = self.danceChoiceL, value = 0 )
        self.discoButtonL.grid(row =10, column=0, sticky = tk.W + tk.E) 
        self.flailButtonL= tk.Radiobutton(self,text = 'Flail', variable = self.danceChoiceL, value = 1 )
        self.flailButtonL.grid(row =11, column=0, sticky = tk.W + tk.E) 
        self.robotButtonL= tk.Radiobutton(self,text = 'Robot', variable = self.danceChoiceL, value = 2 )
        self.robotButtonL.grid(row =12, column=0, sticky = tk.W + tk.E)    
        
         # head image label
          
        self.headPicL = tk.PhotoImage(file='questionMark.gif') # initial image
        self.headLabelL = tk.Label(self,image=self.headPicL,borderwidth=3)
        self.headLabelL.headPicL = self.headPicL
        # position the Label with image on the grid, have it fill the entire space
        self.headLabelL.grid(row=1,column=1, sticky = tk.W +tk.E +tk.S)
        
        
#################
###RIGHT SIDE####
#################

        # text labels 
        headLabelR = tk.Label(self, text='Pick a Head!', font='TimesRoman 12 bold')
        headLabelR.grid(row=2,column = 4, sticky= tk.E)
        
        danceLabelR = tk.Label(self, text='Pick a Dance Move!', font='TimesRoman 12 bold')
        danceLabelR.grid(row=9,column = 4, sticky = tk.E)
        
        
        #head buttons Right  
        
        self.headChoiceR = tk.IntVar()
        self.lynButtonR = tk.Radiobutton(self,text = 'Lyn', variable = self.headChoiceR, value = 0 ) 
        self.lynButtonR.grid(row =3, column=4, sticky = tk.W + tk.E) 
        self.rhysButtonR = tk.Radiobutton(self,text = 'Rhys', variable = self.headChoiceR, value = 1 )
        self.rhysButtonR.grid(row =4, column=4, sticky = tk.W + tk.E) 
        self.susanButtonR = tk.Radiobutton(self,text = 'Susan', variable = self.headChoiceR, value = 2 )
        self.susanButtonR.grid(row =5, column=4, sticky = tk.W + tk.E) 
        self.sohieButtonR = tk.Radiobutton(self,text = 'Sohie', variable = self.headChoiceR, value = 3 )
        self.sohieButtonR.grid(row =6, column=4, sticky = tk.W + tk.E) 
        self.catButtonR = tk.Radiobutton(self,text = 'Cat', variable = self.headChoiceR, value = 4 )
        self.catButtonR.grid(row =7, column=4, sticky = tk.W + tk.E) 
              
        # dance move buttons Right
        self.danceChoiceR = tk.IntVar()
        self.discoButtonR = tk.Radiobutton(self,text = 'Disco', variable = self.danceChoiceR, value = 0 )
        self.discoButtonR.grid(row =10, column=4,sticky = tk.E + tk.W) 
        self.flailButtonR= tk.Radiobutton(self,text = 'Flail', variable = self.danceChoiceR, value = 1 )
        self.flailButtonR.grid(row =11, column=4, sticky = tk.W + tk.E) 
        self.robotButtonR= tk.Radiobutton(self,text = 'Robot', variable = self.danceChoiceR, value = 2 )
        self.robotButtonR.grid(row =12, column=4, sticky = tk.W + tk.E)  
        
        # head iamge label 
        self.headPicR = tk.PhotoImage(file='questionMark.gif') # initial image
        self.headLabelR = tk.Label(self,image=self.headPicR,borderwidth=3)
        self.headLabelR.headPicR = self.headPicR
       
        # position the Label with image on the grid, have it fill the entire space
        self.headLabelR.grid(row=1,column=3,sticky = tk.W +tk.E +tk.S) 
        
    def deselectAllRadioButtons(self):
        #deselect buttons 
        self.discoButtonR.deselect()
        self.flailButtonR.deselect()
        self.robotButtonR.deselect()
        
        self.discoButtonL.deselect()
        self.flailButtonL.deselect()
        self.robotButtonL.deselect()
        
        self.lynButtonR.deselect()
        self.rhysButtonR.deselect()
        self.sohieButtonR.deselect()
        self.susanButtonR.deselect()
        self.catButtonR.deselect()
        
        self.lynButtonL.deselect()
        self.rhysButtonL.deselect()
        self.sohieButtonL.deselect()
        self.susanButtonL.deselect()
        self.catButtonL.deselect()
        
        
        
####################
####START BUTTON####
####################       
        
    def startButtonClick(self):
        
        # takes rightHeadVar and danceChoice from earlier 
        # radio buttons and uses them to invoke correct files/images.  
       
        rightHeadVar = int(self.headChoiceR.get())
        
        leftHeadVar = int(self.headChoiceL.get())
        
        self.pictureR = str(self.headPictures[rightHeadVar])
    
        self.pictureL = str(self.headPictures[leftHeadVar])

        self.NewpicR = tk.PhotoImage(file= self.pictureR)
        self.NewpicL = tk.PhotoImage(file= self.pictureL)
        self.headLabelL.configure(image = self.NewpicL)
        self.headLabelR.configure(image = self.NewpicR)
            
        currentDanceChoiceR = self.danceChoiceR.get()
        print currentDanceChoiceR
        currentDanceChoiceL = self.danceChoiceL.get()
        print currentDanceChoiceL
    
        # picking a dance move, check to see what the user selects and adds the 
        #corresponding dance move to the correct aniamtion canvas  
            
        if currentDanceChoiceR == 1:      
            self.canvasR.addItem(danceAnimation.Flail(self.canvasR,'flailR.gif',80,80)) # image    
        
        if currentDanceChoiceR == 0:
            self.canvasR.addItem(danceAnimation.Disco(self.canvasR, ['disco1R.gif','disco2R.gif'],80,80))
            
        if currentDanceChoiceR == 2:
            self.canvasR.addItem(danceAnimation.Robot(self.canvasR, ['robot1R.gif','robot2R.gif','robot3R.gif','robot4R.gif'],80,80))
      
        if currentDanceChoiceL == 1:           
            self.canvasL.addItem(danceAnimation.Flail(self.canvasL,'flailL.gif',80,80)) # image   
            
        if currentDanceChoiceL == 0:
            self.canvasL.addItem(danceAnimation.Disco(self.canvasL, ['disco1L.gif','disco2L.gif'],80,80))
        if currentDanceChoiceL == 2:
            self.canvasL.addItem(danceAnimation.Robot(self.canvasL, ['robot1L.gif','robot2L.gif','robot3L.gif','robot4L.gif'],80,80))
         
        self.canvasR.start()  
        self.canvasL.start() 
        
        
        
###################
####STOP BUTTON####
###################          
           
        

    def stopButtonClick(self):
        self.headLabelL.configure(image = self.headPicL)
        self.headLabelR.configure(image = self.headPicR)
            
        for item in self.canvasR.items:
            self.canvasR.removeItem(item)
        for item in self.canvasL.items:
            self.canvasL.removeItem(item)
        self.canvasR.stop()
        self.canvasL.stop()
    
        self.deselectAllRadioButtons()
        
        
        
        
        
        
            
            
            
        
    



        
root = tk.Tk()
app = DanceGameApp(root)
# For Macs only: Bring root window to the front
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
root.mainloop()