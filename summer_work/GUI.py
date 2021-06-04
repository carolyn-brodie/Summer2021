# Imports:
import tkinter as tk
import speech_recognition as sr
import random

# Globals:

# Window Globals
WINDOW_NAME = "Un-named"
# x,y value of the window height and width
WINDOW_X = 400
WINDOW_Y = 400

# Should allow for change of the window height and width 
WINDOW_STARTING_SIZE = str(WINDOW_X) + "x" + str(WINDOW_Y)

# Word Globals
wordSelected = ""
wordInputed = ""

# Tally System
right = 0
wrong = 0

selection = 0

def main():
    app = GUI()
    app.title(WINDOW_NAME)
    app.geometry(WINDOW_STARTING_SIZE)

    app.mainloop()


# Main Gui
class GUI(tk.Tk):
    """
        *args takes any number of positional arguments.
        **kwargs takes any number of keyword arguments.
        Important for loading the different frames as they might have many different arguments.
    """
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
        for FrameSelected in (MainMenu, WordTypeSelection,WordShower, ResultsPage, AnalyticResults):
            frame = FrameSelected(container, self)

            self.frames[FrameSelected] = frame

            # I think this is like the pack() for frames, because nothing loads without it
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    # this is the function that switches the frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Classes for the Frames
# Main Menu
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Label for the main menu
        self.mainMenuLabel = tk.Label(self, text="Main Menu")
        self.mainMenuLabel.grid(row = 1)

        self.Start = tk.Button(self, text="Start",command = lambda: controller.show_frame(WordTypeSelection))
        self.Start.grid(row = 2)

        # Button to go to the analytic screen
        self.analyticButton = tk.Button(self, text="Analytic button",command=lambda: controller.show_frame(AnalyticResults))
        self.analyticButton.grid(row = 3)

        # Exit button
        self.Quit = tk.Button(self, text="Exit", command=self.master.quit)
        self.Quit.grid(row = 10)


class WordTypeSelection(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        self.wordTypeLabel = tk.Label(self,text="Word Types To Select")
        self.wordTypeLabel.grid(row = 1)

        self.rWordSelection = tk.Button(self, text="R words",command = lambda: self.chooser(parent,controller,1))
        self.rWordSelection.grid(row = 2)

        self.sWordSelection = tk.Button(self, text="S words",command = lambda: self.chooser(parent,controller,2))
        self.sWordSelection.grid(row = 3)

        self.lWordSelection = tk.Button(self, text="L words",command = lambda: self.chooser(parent,controller,3))
        self.lWordSelection.grid(row = 4)

        self.blendsWordSelection = tk.Button(self, text="blend words",command = lambda: self.chooser(parent,controller,4))
        self.blendsWordSelection.grid(row = 5)

        self.backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame(MainMenu))
        self.backButton.grid(row = 10,column = 0,sticky = "e")

        self.quitbutton = tk.Button(self, text="exit", command=self.master.quit)
        self.quitbutton.grid(row = 10,column = 0,sticky = "w")

    def chooser(self,parent,controller,integer):
        controller.show_frame(WordShower)
        global selection
        self.integer = integer

        if self.integer == 1:
            selection = 1
        elif self.integer == 2:
            selection = 2
        elif self.integer == 3:
            selection = 3

class WordShower(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        lbl = tk.Label(self,text = "text")
class ResultsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



class AnalyticResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)






main()
