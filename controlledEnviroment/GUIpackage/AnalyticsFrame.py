import tkinter as tk
from GUIpackage.R_Frames.TypeOfErrorWCorrect import TypeOfErrorWCorrectClass
from GUIpackage.R_Frames.TypeOfErrorSpecific import typeOfErrorSpecifics
from GUIpackage.R_Frames.TypeOfErrorPercents import TypeOfErrorPercents
from GUIpackage.R_Frames.TypeOfErrorAll import TypeOfErrorAllClass
from GUIpackage.R_Frames.Sessions import SessionsClass
from GUIpackage.R_Frames.PieChartFrame import PieChartClass
from GUIpackage.R_Frames.BMETypeOfErrorSpecific import bmeTypeOfErrorSpecificClass
from GUIpackage.R_Frames.BMETypeOfErrorAll import BMEtypeOfErrorAllClass
from GUIpackage.R_Frames.bmeSpecific import bmeSpecificClass
from GUIpackage.R_Frames.bmeAll import bmeAllClass
import rpy2.robjects as ro


class Analytics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.bmeAllButton = tk.Button(self, text="BME All Graph", command=lambda: self.bmeAllFunction(controller))
        self.bmeSpecificButton = tk.Button(self, text="BME Specific Graph",
                                           command=lambda: self.bmeSpecificFunction(controller))
        self.bmeTypeOfErrorAllButton = tk.Button(self, text="BME Type Of Error All",
                                                 command=lambda: self.bmeTypeOfErrorAllFunction(controller))
        self.bmeTypeOfErrorSpecificButton = tk.Button(self, text="BME Type Of Error Specific",
                                                      command=lambda: self.bmeTypeOfErrorSpecificFunction(controller))
        self.pieChartButton = tk.Button(self, text="Pie Chart Button",
                                        command=lambda: self.pieChartFunction(controller))
        self.sessionButton = tk.Button(self, text="Sessions Button",
                                        command=lambda: self.sessionFunction(controller))
        self.typeOfErrorAllButton = tk.Button(self, text="Type of Error All",
                                              command=lambda: self.TypeOfErrorAllFunction(controller))
        self.typeOfErrorPercentsButton = tk.Button(self, text="Type Of Error Percennt ",
                                                   command=lambda: self.TypeOfErrorPercentFunction(controller))
        self.typeOfErrorSpecificButton = tk.Button(self, text="Type Of Error Specific",
                                                   command=lambda: self.TypeOfErrorSpecificFunction(controller))
        self.typeOfErrorWCorrect = tk.Button(self, text="Type Of Error W Correct",
                                             command=lambda: self.TypeOfErrorWCorrectFunction(controller))

        self.bmeAllButton.pack(side="top")
        self.bmeSpecificButton.pack(side="top")
        self.bmeTypeOfErrorAllButton.pack(side="top")
        self.bmeTypeOfErrorSpecificButton.pack(side="top")
        self.pieChartButton.pack(side="top")
        self.sessionButton.pack(side = "top")
        self.typeOfErrorAllButton.pack(side="top")
        self.typeOfErrorPercentsButton.pack(side="top")
        self.typeOfErrorSpecificButton.pack(side="top")
        self.typeOfErrorWCorrect.pack(side="top")

        self.backButton = tk.Button(self, text="Back", command=lambda: self.backFunction(controller))
        self.backButton.pack(side="top")

    def bmeAllFunction(self, controler):
        controler.show_frame(bmeAllClass)

    def bmeSpecificFunction(self, controller):
        controller.show_frame(bmeSpecificClass)

    def bmeTypeOfErrorAllFunction(self, controller):
        controller.show_frame(BMEtypeOfErrorAllClass)

    def bmeTypeOfErrorSpecificFunction(self, controller):
        controller.show_frame(bmeTypeOfErrorSpecificClass)

    def pieChartFunction(self, controller):
        controller.show_frame(PieChartClass)

    def sessionFunction(self, controller):
        controller.show_frame(SessionsClass)

    def TypeOfErrorAllFunction(self, controller):
        controller.show_frame(TypeOfErrorAllClass)

    def TypeOfErrorPercentFunction(self, controller):
        controller.show_frame(TypeOfErrorPercents)

    def TypeOfErrorSpecificFunction(self, controller):
        controller.show_frame(typeOfErrorSpecifics)

    def TypeOfErrorWCorrectFunction(self, controller):
        controller.show_frame(TypeOfErrorWCorrectClass)

    def backFunction(self, controller):
        from GUIpackage.MainMenuFrame import MainMenu
        controller.show_frame(MainMenu)
