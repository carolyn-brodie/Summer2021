import tkinter as tk
import rpy2.robjects as ro
import PIL.Image
class PieChartClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.fileSelected = "percentFile"
        numberSelected = []
        total = 0
        filereader = open("~/../outData/"+self.fileSelected+".csv","r")
        for line in filereader:
            numberSelected.append(total)
            total += 1

        self.selection = tk.IntVar(self)
        self.selection1 = tk.IntVar(self)

        self.selection.set(numberSelected[0])  # default value
        self.selection1.set(numberSelected[0])

        self.optionMenu = tk.OptionMenu(self, self.selection, *numberSelected)
        self.optionMenu.pack(side="top")

        self.optionMenu2 = tk.OptionMenu(self, self.selection1, *numberSelected)
        self.optionMenu2.pack(side="top")


        self.nextButton = tk.Button(self,text = "Create Graph",command = self.createGraphFunction)
        self.nextButton.pack(side = "top")


        self.backButton = tk.Button(self, text="Back", command=lambda: self.backFunction(controller))
        self.backButton.pack(side="top")

    def backFunction(self, controller):
        from GUIpackage.AnalyticsFrame import Analytics
        controller.show_frame(Analytics)

    def createGraphFunction(self):
        r = ro.r
        self.selectionOne = self.selection.get()
        self.selectionTwo = self.selection1.get()


        r.source("~/../RScripts/PieChart.R")

        r.percent_Of_Sessions(self.selectionOne,self.selectionTwo,self.fileSelected)
        img = PIL.Image.open(
            "~/../Graphs/PieChart" + self.fileSelected + ".png")
        img.show()
        img.close()
