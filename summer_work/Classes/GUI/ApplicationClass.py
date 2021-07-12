import tkinter as tk
from summer_work.Classes.GUI.MainMenuFrame import MainMenu
from summer_work.Classes.GUI.WordQuizerFrame import WordQuizer
from summer_work.Classes.GUI.PatientSimulatorFrame import PatientSimulator
from summer_work.Classes.GUI.AnalyticsFrame import Analytics
from summer_work.Classes.GUI.PieChartFrame import PieChart

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
                MainMenu, WordQuizer, PatientSimulator, Analytics,PieChart):
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


def main():
    app = GUI()
    app.title("Application")
    app.geometry("600x600")
    app.mainloop()


main()
