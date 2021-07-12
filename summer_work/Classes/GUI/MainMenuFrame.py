import tkinter as tk
from summer_work.Classes.GUI.WordQuizerFrame import WordQuizer
from summer_work.Classes.GUI.PatientSimulatorFrame import PatientSimulator
from summer_work.Classes.GUI.AnalyticsFrame import Analytics

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Label for the main menu
        self.mainMenuLabel = tk.Label(self, text="Main Menu")
        self.mainMenuLabel.grid(row = 1)

        self.Start = tk.Button(self, text="Word Quizzer", command = lambda: controller.show_frame(
            WordQuizer))
        self.Start.grid(row = 2)

        # Button to go to the analytic screen
        self.patientSimulator = tk.Button(self, text="Patient Simulator", command=lambda: controller.show_frame(
            PatientSimulator))
        self.patientSimulator.grid(row = 3)

        self.analyticButton = tk.Button(self, text = "Analytic Button", command = lambda: controller.show_frame(
            Analytics))
        self.analyticButton.grid(row = 4)
        # Exit button
        self.Quit = tk.Button(self, text="Exit", command=self.master.quit)
        self.Quit.grid(row = 10)

