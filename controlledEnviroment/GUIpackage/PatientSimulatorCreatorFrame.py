import tkinter as tk
from Classes.patientSimulatorClass import PatientSimulatorClass

class PatientSimulatorCreator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.createPatientButton = tk.Button(self,text = "Create Patient",command = self.createPatientFunction)
        self.createPatientButton.pack(side = "top")

        self.backButton = tk.Button(self,text = "Back",command = lambda:self.backFunction(controller))
        self.backButton.pack(side = "bottom")
    def createPatientFunction(self,):
        psc = PatientSimulatorClass()
        psc.constructor(.5,.3,.5,.2,.1)
    def backFunction(self,controller):
        from GUIpackage.MainMenuFrame import MainMenu
        controller.show_frame(MainMenu)