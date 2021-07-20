import tkinter as tk
from GUIpackage.WordQuizerFrame import WordQuizer
from GUIpackage.PatientSimulatorFrame import PatientSimulator
from GUIpackage.AnalyticsFrame import Analytics
from GUIpackage.PatientSimulatorCreatorFrame import PatientSimulatorCreator
from GUIpackage.ErrorFileProbabilityFrame import ErrorFileProbabilityClass


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Label for the main menu
        self.mainMenuLabel = tk.Label(self, text="Main Menu")
        self.mainMenuLabel.grid(row=1)

        self.Start = tk.Button(self, text="Well Spoken", command=lambda: controller.show_frame(
            WordQuizer))
        self.Start.grid(row=2)

        # Button to go to the analytic screen
        self.patientSimulatorButton = tk.Button(self, text="Patient Simulator", command=lambda: controller.show_frame(
            PatientSimulator))
        self.patientSimulatorButton.grid(row=3)

        self.patientSimulatorCreatorButton = tk.Button(self, text="Patient Simulator Creator",
                                                       command=lambda: controller.show_frame(
                                                           PatientSimulatorCreator))
        self.patientSimulatorCreatorButton.grid(row=4)

        self.analyticButton = tk.Button(self, text="Analytic Button", command=lambda: controller.show_frame(
            Analytics))
        self.analyticButton.grid(row=5)

        self.errorFileButton = tk.Button(self, text="Error File Probability",
                                         command=lambda: controller.show_frame(ErrorFileProbabilityClass))
        self.errorFileButton.grid(row=6)
        # Exit button
        self.Quit = tk.Button(self, text="Exit", command=self.master.quit)
        self.Quit.grid(row=10)
