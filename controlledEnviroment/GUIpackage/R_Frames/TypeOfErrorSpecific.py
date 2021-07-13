import tkinter as tk
import os
import rpy2.robjects as ro
import PIL

class typeOfErrorSpecifics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.fileList = os.listdir("~/../outData/ErrorFileDir/")
        self.fileListRev = []
        for files in self.fileList:
            self.fileListRev.append(os.path.splitext(files)[0])
        self.selection = tk.StringVar(self)
        self.selection.set(self.fileListRev[0])  # default value

        self.optionMenu = tk.OptionMenu(self, self.selection, *self.fileListRev)
        self.optionMenu.pack(side="top")

        self.labelSoundBox = tk.Label(self,text = "Sound Box Selection")
        self.labelSoundBox.pack(side = "top")

        self.soundBox = tk.Entry(self)
        self.soundBox.pack(side='top')

        self.soundSelection = "a"

        self.soundBoxButton = tk.Button(self,text = "Enter",command = lambda: self.soundSelectionFunction())
        self.soundBoxButton.pack(side = "top")

        self.nextButton = tk.Button(self, text="Create Graph", command=self.createGraphFunction)
        self.nextButton.pack(side="top")

        self.backButton = tk.Button(self, text="Back", command=lambda: self.backFunction(controller))
        self.backButton.pack(side="top")

    def backFunction(self, controller):
        from GUIpackage.AnalyticsFrame import Analytics
        controller.show_frame(Analytics)

    def soundSelectionFunction(self):
        self.soundSelection = self.soundBox.get()

    def createGraphFunction(self):
        selection = self.selection.get()
        r = ro.r
        print("../RScripts/TypeOfErrorSpecific.R")
        r.source("~/../RScripts/TypeOfErrorSpecific.R")
        print("../Graphs/TypeOfErrorSpecific" + selection + ".png")
        r.plotLetter(self.soundSelection,selection)
        img = PIL.Image.open(
            "~/../Graphs/TypeOfErrorSpecific" + selection+self.soundSelection + ".png")
        img.show()
        img.close()