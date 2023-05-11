from tkinter import *
from tkinter import messagebox

"""Style class"""
class Style:
    def __init__(self):
        #Dark mode
        self.primary = "#474747" #Lighter
        self.secondary = "#333333" #Darker
        self.text_color = "#76a5a6" #Light Blue
        self.accent = "#b8b8b8" #Lightest
        self.background = "#121212" #Dark background
        self.title_color = "#915b31" #Deep orange
        #Light mode

"""Custom item Widget class"""
class Widget:
    def __init__(self, frame, name, count, ref_code, aisle, shelf):

        #Create widget and add style
        self.widget = Label(frame, text="Item:{} Stock:{}".format(name, count))
        self.widget.configure(bg=style.secondary)

"""Main GUI class"""
class Gui:
    def __init__(self, parent):
        #Create Fonts used in GUI creation
        default = ("Arial", 10, "normal")
        title = ("Roboto", 20, "bold")
        button = ("Roboto", 10, "bold")

        #Frame layout
        navbar = Frame(parent, width=(window_width * 0.05), height=window_height, bg=style.secondary,
                       highlightbackground=style.accent, highlightthickness=1, bd=0, relief="solid")
        main = Frame(parent, width=(window_width * 0.95), height=window_height, bg=style.background)
        navbar.grid(row=0, column=0)
        main.grid(row=0, column=1)


        """---Nav bar---"""
        stock = Button(navbar, text="Stock", font=button, height=1, bg=style.accent, fg=style.primary)
        orders = Button(navbar, text="Orders", font=button, height=1, bg=style.accent, fg=style.primary)
        settings = Button(navbar, text="Settings", font=button, height=1, bg=style.accent, fg=style.primary)
        stock.pack(padx=5, pady=(window_height * 0.3)/2)
        orders.pack(padx=5, pady=(window_height * 0.3)/2)
        settings.pack(padx=5, pady=(window_height * 0.3)/2)

        """---Stock Page----"""
        #Create stock page frame
        stock_page = Frame(main, height=window_height, width = (window_width * 0.95), bg=style.primary,
                             highlightbackground="green", highlightthickness=1, bd=0, relief="solid")
        stock_page.pack() #JUST FOR WHILE DEVELOPING THE STOCK PAGE DELETE THIS AFTER!!!!!!!!!

        """Search bar"""
        #Create search bar page frame
        stock_search = Frame(stock_page, bg=style.primary, 
                             highlightbackground="red", highlightthickness=1, bd=0, relief="solid")
        stock_search.pack(fill='x')

        #Title
        search_title = Label(stock_search, text="Search stock", font=title, fg=style.title_color, bg=style.primary, height=(int(window_height * 0.0025)))
        search_title.pack(side='left')

        divide = Frame(stock_search, bg=style.primary, width=(window_width * 0.5))
        divide.pack(side='right')

        #Radiobutton frame
        radiobutton_frame = Frame(divide, bg=style.primary)
        radiobutton_frame.grid(row=0, column=0, padx=5)
        #Search bar frame
        search_bar_frame = Frame(divide, bg=style.primary)
        search_bar_frame.grid(row=0, column=1, padx=5)


        #Radio button for which value to search
        self.v = IntVar()
        self.v.set(1)
        search_name = Radiobutton(radiobutton_frame, variable=self.v, value="name", text="Name", bg=style.primary, fg=style.text_color, font=default)
        search_count = Radiobutton(radiobutton_frame, variable=self.v, value="count", text="Code", bg=style.primary, fg=style.text_color, font=default)
        search_ref_code = Radiobutton(radiobutton_frame, variable=self.v, value="ref_code", text="Refrence Code", bg=style.primary, fg=style.text_color, font=default)
        search_aisle = Radiobutton(radiobutton_frame, variable=self.v, value="aisle", text="Aisle", bg=style.primary, fg=style.text_color, font=default)
        search_shelf = Radiobutton(radiobutton_frame, variable=self.v, value="shelf", text="Shelf", bg=style.primary, fg=style.text_color, font=default)

        #Grid radio buttons
        search_name.grid(row=0, column=0)
        search_count.grid(row=1, column=0)
        search_aisle.grid(row=0, column=1)
        search_shelf.grid(row=1, column=1)
        search_ref_code.grid(row=0, column=2)

        #Search bar frame
        search_bar = Entry(search_bar_frame, width=30)
        search_bar.grid(row=0, column=0)
        #Search button
        search_button = Button(search_bar_frame, text="Search", font=button, bg=style.accent, fg=style.primary)
        search_button.grid(row=0,column=1, padx=5)

        """Create list of items frame"""
        stock_items = Frame(stock_page, height= (window_height * 0.85), width = (window_width * 0.95), bg=style.primary, 
                             highlightbackground="blue", highlightthickness=1, bd=0, relief="solid")
        stock_items.pack()



"""Main routine"""
if __name__ == "__main__":
    style = Style()
    root = Tk()
    root.title("Warehouse Software")
    root.configure(background=style.background)

    #Get window size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    #Define window size
    window_width = int(screen_width * 0.8) #80% of window width
    window_height = int(screen_height * 0.8) #80% of window height
    #Calculate window position to position it in the center of the screen
    window_x = (screen_width - window_width) // 2
    window_y = (screen_height - window_height) // 2
    #Apply window sizing
    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    instance=Gui(root)
    root.mainloop()