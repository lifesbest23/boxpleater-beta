from tkinter import *
class Controller:
    def __init__(self):
        self.root = Tk()
        self.treeView = TreeViewWindow(self.root)
        self.cpView = CPViewWindow(self.root)

    def run(self):
        self.root.title("Main Window")
        self.root.mainloop()

class TreeViewWindow:
    def __init__(self, master):
        self.frame = Frame(master)
        self.text = Text(frame, "Test")

        self.canvas = Canvas(self.frame,width=600,height = 450)
        self.canvas.pack()

class CPViewWindow:
    def __init__(self, master):
        self.frame = Frame(master)
        self.canvas = Canvas(self.frame,width=600,height = 450)
        self.canvas.pack()

if __name__ == "__main__":
    c = Controller()
    c.run()
