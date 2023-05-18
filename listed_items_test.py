from tkinter import *
from tkinter import messagebox

#font class
class Style:
    def __init__(self):
        """Dark mode"""
        self.primary = "#292929" #Lighter
        self.secondary = "#121212" #Darker
        self.text_color = "#6ca5b8" #Light Blue

        """Light mode"""

#Secondary class
class Item:
    def __init__(self, frame, value1, value2):
        self.goto_frame = frame
        self.rb_valuealue11 = value1
        self.rb_valuealue22 = value2

        self.widget = Label(self.goto_frame, text=("Name: {} Year group: {}".format(value1, value2)), relief=SOLID, borderwidth=2, width=20, height=1)
        self.widget.configure(bg=style.secondary, fg=style.text_color)

    def get_item(self):
        return self.widget
        

class Gui:
    def __init__(self, parent):
        #Create default font
        default=("Arial", 12, "normal")

        #Make a frame to put the list into and a simple label
        self.list_frame = Frame(parent)
        self.data = []
        label = Label(parent, text="Testing page", font=default, fg=style.text_color, bg=style.secondary)
        label.pack()
        self.list_frame.pack()
        
        #Testing data, actual data would be gathered with entrys.
        self.data.append(Item(self.list_frame, "Noah", "3"))
        self.data.append(Item(self.list_frame, "Nick", "1"))
        self.data.append(Item(self.list_frame, "Jack", "2"))
        self.pack_list()

    """Function to pack the list of items. Only prints in order items were appended in."""
    def pack_list(self):
        for i in self.data:
            widget = i.get_item()
            widget.pack()
        

#Main routine
if __name__ == "__main__":
    #create a style instance
    style = Style()
    root = Tk()
    root.title("Warehouse Software")
    root.configure(background=style.secondary)
    obj = Gui(root)
    root.mainloop()