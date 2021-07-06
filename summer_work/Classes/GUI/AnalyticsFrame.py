import tkinter as tk
import rpy2.robjects as robjects


class Analytics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.bmeAllButton = tk.Button(self,text = "BME All Graph")
        self.bmeAllButton.pack(side = "top")

        self.bmeTypeOfErrorButton = tk.Button(self,text = "BME Type Of Error")
        self.bmeTypeOfErrorButton.pack(side = "top")

        self.bmeTypeOfErrorAllButton = tk.Button(self,text = "BME Type Of Error All Graph")
        self.bmeTypeOfErrorAllButton.pack(side = "top")

        self.sessionsButton = tk.Button(self,text = "Session Graph")
        self.sessionsButton.pack(side = "top")

        self.pieChartButton = tk.Button(self,text = "Pie Chart",command = lambda : self.pieChartFunction(controller))
        self.pieChartButton.pack(side = "top")

        self.typeOfErrorAllButton = tk.Button(self,text = "Type of Error Graph")
        self.typeOfErrorAllButton.pack(side = "top")

        self.typeOfErrorPercent = tk.Button(self,text = "Type of Error Graph")
        self.typeOfErrorPercent.pack(side = "top")

        self.backButton = tk.Button(self, text="Back", command=lambda: self.backFunction(controller))
        self.backButton.pack(side="top")


    def pieChartFunction(self,controller):
        from summer_work.Classes.GUI.PieChartFrame import PieChart
        controller.show_frame(PieChart)

    def backFunction(self, controller):
        from summer_work.Classes.GUI.MainMenuFrame import MainMenu
        controller.show_frame(MainMenu)
