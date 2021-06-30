import tkinter as tk
import rpy2.robjects as robjects


class Analytics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.backButton = tk.Button(self, text="Back", command=lambda: self.backFunction(controller))
        self.backButton.pack(side="top")

        self.rTest()

    def rTest(self):
        r1 = robjects.r
        path = ("../../")
        print(path+ "BMEAll.R")
        r1.source(path + "BMEAll.R")
        r1.plotBME("C:\\Users\somet\\Desktop\\Summer2021\\summer_work\\ErrorFile_6-21_14-32.csv")

    def backFunction(self, controller):
        from summer_work.Classes.GUI.MainMenu import MainMenu1
        controller.show_frame(MainMenu1)
