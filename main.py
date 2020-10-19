from tkinter import *
class Controller:
    def __init__(self):
        self.master = Tk()
        self.mk = Toplevel(self.master)
        self.treeView = TreeViewWindow(self.master)
        self.cpView = CPViewWindow(self.mk)

        self.treeView.bar.closeButton.bind("<Button-1>",self.closeProgramm)
    def run(self):
        self.treeView.run()
        self.cpView.run()
        self.master.mainloop()

    def closeProgramm(self, event):
        self.master.destroy()
        print("CLOSE")

class TreeViewWindow:
    """ Contains
    TreeViewSideBar
    Canvas

    All the model to view interaction
    """
    def __init__(self, master):
        self.master = master
        self.master.title("TreeWindow")
        self.master.geometry("400x400")
        self.root = Frame(master)
        
        self.bar = TreeViewSideBar(self.root)
        self.bar.frame.pack(side=LEFT)

        self.canvas = Canvas(self.root,width=600,height = 450, bg="black")
        self.canvas.pack(side=LEFT, fill=BOTH)

    def run(self):
        self.root.pack()

    def drawCanvas(self):
        pass 


class TreeViewSideBar:
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
    """
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
        
        self.closeButton = Button(self.frame, text = "Exit")
        self.closeButton.grid(row = 8, columnspan=2, sticky=W+E)


class CPViewWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("CPWindow")
        self.master.geometry("400x400")
        self.root = Frame(master)
        
        self.bar = CPViewSideBar(self.root)
        self.bar.frame.pack(side=LEFT)

        self.canvas = Canvas(self.root,width=600,height = 450, bg="RED")
        self.canvas.pack(side=LEFT, fill=BOTH)

    def run(self):
        self.root.pack()

    def drawCanvas(self):
        pass 

class CPViewSideBar:
    """ Contains
    input
    calculate button

    increase grid size
    lower grid size
    next Solution
    previous solution

    save as cp file
    """
    def __init__(self, master):
        self.frame = Frame(master)

        self.inputField = Entry(self.frame)

        
        self.calculateButton = Button(self.frame, text="Calculate")
        self.calculateButton.grid(row = 1, columnspan=2, sticky=W+E)
        self.incGridButton = Button(self.frame, text="Increase Grid Size")
        self.incGridButton.grid(row = 2, columnspan=2, sticky=W+E)
        self.decGridButton = Button(self.frame, text="Decrease Grid Size")
        self.decGridButton.grid(row = 3, columnspan=2, sticky=W+E)
        
        self.nextSolButton = Button(self.frame, text="Next Solution")
        self.nextSolButton.grid(row = 4, columnspan=2, sticky=W+E)
        self.prevSolButton = Button(self.frame, text="Previous Solution")
        self.prevSolButton.grid(row = 5, columnspan=2, sticky=W+E)

        Label(self.frame, text="").grid(row= 6)

        self.saveCPButton = Button(self.frame, text="Save .cp")
        self.saveCPButton.grid(row = 7, columnspan=2, sticky=W+E)


if __name__ == "__main__":
    c = Controller()
    c.run()
