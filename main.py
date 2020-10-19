from tkinter import *
class Controller:
    def __init__(self):
        self.treeView = TreeViewWindow()
        #self.cpView = CPViewWindow(self.root)

    def run(self):
        #self.root.title("Main Window")
        self.treeView.run()
        #self.root.mainloop()

class TreeViewWindow:
    """ Contains
    Label Enter Length here
    TextInputField
    Button
        Create Flap
        Create River
        Create Subriver
        Go back down

        Undo
        StartOver
    Canvas
    """
    def __init__(self):
        self.root = Tk()
        
        self.bar = TreeViewSideBar(self.root)
        self.bar.frame.pack(side=LEFT)

        self.canvas = Canvas(self.root,width=600,height = 450, bg="black")
        self.canvas.pack(side=LEFT, fill=BOTH)

    def run(self):
        self.root.title("Tree Window")
        self.root.mainloop()

    def drawCanvas(self):
        pass 


class TreeViewSideBar:
    def __init__(self, master):
        self.frame = Frame(master)
        
        Label(self.frame, text = "Test").grid(row=0)
        
        self.size = Entry(self.frame)
        self.size.grid(row=0, column = 1)
        
        self.cFlapButton = Button(self.frame, text="Create Flap")
        self.cFlapButton.grid(row = 1, columnspan=2, sticky=W+E)
        self.cRiverButton = Button(self.frame, text="Create River")
        self.cRiverButton.grid(row = 2, columnspan=2, sticky=W+E)
        self.cSubriverButton = Button(self.frame, text="Create Sub River")
        self.cSubriverButton.grid(row = 3, columnspan=2, sticky=W+E)

        self.walkDownButton = Button(self.frame, text="Go Back Down")
        self.walkDownButton.grid(row = 4, columnspan=2, sticky=W+E)

        Label(self.frame, text="").grid(row=5)

        self.undoButton = Button(self.frame, text="Undo")
        self.undoButton.grid(row=6, columnspan=2, sticky=W+E)

        self.restartButton = Button(self.frame, text="Start Over")
        self.restartButton.grid(row = 4, columnspan=2, sticky=W+E)


class CPViewWindow:
    def __init__(self, master):
        self.frame = Frame(master)
        self.canvas = Canvas(self.frame,width=600,height = 450)
        self.canvas.pack()

if __name__ == "__main__":
    c = Controller()
    c.run()
