import tkinter as tk
import os
import rpy2.robjects as ro
import PIL.Image


class bmeTypeOfErrorSpecificClass(tk.Frame):
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
    def soundSelectionFunction(self):
        self.soundSelection = self.soundBox.get()
    def backFunction(self, controller):
        from GUIpackage.AnalyticsFrame import Analytics
        controller.show_frame(Analytics)

    def createGraphFunction(self):
        selection = self.selection.get()
        r = ro.r

        r.source("~/../RScripts/BMETypeOfErrorSpecific.R")

        r.plotWhereError(self.soundSelection,selection)
        img = PIL.Image.open(
            "~/../Graphs/BMETypeOfErrorSpecific" + selection + ".png")
        img.show()
        img.close()