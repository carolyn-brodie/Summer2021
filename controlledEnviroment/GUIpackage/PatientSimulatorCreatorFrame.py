import tkinter as tk
from GUIpackage.Classes.patientSimulatorClass import PatientSimulatorClass

class PatientSimulatorCreator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.entry1 = .20
        self.entry2 = .20
        self.entry3 = .20
        self.entry4 = .20
        self.entry5 = .20

        self.controller = controller

        self.createPatientButton = tk.Button(self,text = "Create Patient",command = self.createPatientFunction)
        self.createPatientButton.pack(side = "top")
        self.entryBox1 = tk.Entry(self)
        self.entryBox1.pack(side='top')

        self.entryBox2 = tk.Entry(self)
        self.entryBox2.pack(side='top')

        self.entryBox3 = tk.Entry(self)
        self.entryBox3.pack(side='top')

        self.entryBox4 = tk.Entry(self)
        self.entryBox4.pack(side='top')

        self.entryBox5 = tk.Entry(self)
        self.entryBox5.pack(side='top')

        self.soundBoxButton = tk.Button(self, text="Enter", command=lambda: self.EnterNumbers())
        self.soundBoxButton.pack(side="top")

        self.backButton = tk.Button(self,text = "Back",command = lambda:self.backFunction(controller))
        self.backButton.pack(side = "bottom")
    def EnterNumbers(self):

        self.entry1 = float(self.entryBox1.get())
        self.entry2 = float(self.entryBox2.get())
        self.entry3 = float(self.entryBox3.get())
        self.entry4 = float(self.entryBox4.get())
        self.entry5 = float(self.entryBox5.get())

    def createPatientFunction(self,):
        psc = PatientSimulatorClass()
        psc.constructor(self.entry1,self.entry2,self.entry3,self.entry4,self.entry5)
    def backFunction(self,controller):
        from GUIpackage.MainMenuFrame import MainMenu
        controller.show_frame(MainMenu)