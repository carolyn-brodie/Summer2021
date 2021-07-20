import tkinter as tk
from GUIpackage.MainMenuFrame import MainMenu
from GUIpackage.WordQuizerFrame import WordQuizer
from GUIpackage.PatientSimulatorFrame import PatientSimulator
from GUIpackage.AnalyticsFrame import Analytics
from GUIpackage.ErrorFileProbabilityFrame import ErrorFileProbabilityClass
from GUIpackage.PatientSimulatorCreatorFrame import PatientSimulatorCreator
from GUIpackage.R_Frames.bmeAll import bmeAllClass
from GUIpackage.R_Frames.bmeSpecific import bmeSpecificClass
from GUIpackage.R_Frames.BMETypeOfErrorAll import BMEtypeOfErrorAllClass
from GUIpackage.R_Frames.BMETypeOfErrorSpecific import bmeTypeOfErrorSpecificClass
from GUIpackage.R_Frames.PieChartFrame import PieChartClass
from GUIpackage.R_Frames.Sessions import SessionsClass
from GUIpackage.R_Frames.TypeOfErrorAll import TypeOfErrorAllClass
from GUIpackage.R_Frames.TypeOfErrorPercents import TypeOfErrorPercents
from GUIpackage.R_Frames.TypeOfErrorSpecific import typeOfErrorSpecifics
from GUIpackage.R_Frames.TypeOfErrorWCorrect import TypeOfErrorWCorrectClass



class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Need the container to load frames
        container = tk.Frame(self)

        container.pack(side="top")

        # set up, but don't use the grid atm
        container.grid_rowconfigure(0)
        container.grid_columnconfigure(0)

        """
            List of all frames to be loaded and switched
            !test if destroying a frame inside individual frame class causes issues!
        """
        self.frames = {}

        """
            TK loads every single frame from the start
            Loops through the frame list selecting a frame to put on top
        """
        for FrameSelected in (
                MainMenu, WordQuizer, PatientSimulator, Analytics, PatientSimulatorCreator, ErrorFileProbabilityClass,
                PieChartClass,bmeAllClass,bmeSpecificClass,BMEtypeOfErrorAllClass,bmeTypeOfErrorSpecificClass,
                SessionsClass,TypeOfErrorAllClass,TypeOfErrorPercents,typeOfErrorSpecifics,TypeOfErrorWCorrectClass):
            frame = FrameSelected(container, self)

            self.frames[FrameSelected] = frame

            # I think this is like the pack() for frames, because nothing loads without it
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

        # this is the function that switches the frame
        print(self.frames)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


import sys, os
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))