import tkinter as tk
import WordQuizer
import PatientSimulator
import Analytics

class MainMenu1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Label for the main menu
        self.mainMenuLabel = tk.Label(self, text="Main Menu")
        self.mainMenuLabel.grid(row = 1)

        self.Start = tk.Button(self, text="Word Quizzer", command = lambda: controller.show_frame(
            WordQuizer.WordQuizer))
        self.Start.grid(row = 2)

        # Button to go to the analytic screen
        self.patientSimulator = tk.Button(self, text="Patient Simulator", command=lambda: controller.show_frame(
            PatientSimulator.PatientSimulator))
        self.patientSimulator.grid(row = 3)

        self.analyticButton = tk.Button(self, text = "analytic Button", command = lambda: controller.show_frame(
            Analytics.Analytics))
        self.analyticButton.grid(row = 4)
        # Exit button
        self.Quit = tk.Button(self, text="Exit", command=self.master.quit)
        self.Quit.grid(row = 10)

