import tkinter as tk
from GUIpackage.Classes.ErrorFileProb import ErrorFileDict
from GUIpackage.Classes.LetterToCharactersClass import LetterToCharacters
import os
from GUIpackage.sysVar import application_path

class ErrorFileProbabilityClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.fileList = os.listdir(application_path+"\\outData\\ErrorFileDir\\")
        self.fileListRev = []
        for files in self.fileList:
            self.fileListRev.append(os.path.splitext(files)[0])
        self.selection = tk.StringVar(self)
        self.selection.set(self.fileListRev[0])  # default value

        self.optionMenu = tk.OptionMenu(self, self.selection, *self.fileListRev)
        self.optionMenu.pack(side="top")

        self.occursButton = tk.Button(self,text = " Occurs Button",command = lambda:self.occursFunction())
        self.occursButton.pack(side = "top")
    def occursFunction(self):
        self.thisSelection = self.selection.get()
        self.path = application_path+"\\outData\\ErrorFileDir\\" +self.thisSelection+".csv"
        self.errorFile = ErrorFileDict()
        self.errorFile.occursController(self.path)

    def backFunction(self, controller):
        from GUIpackage.MainMenuFrame import MainMenu
        controller.show_frame(MainMenu)


