from tkinter import *
from tkinter import messagebox

"""Style class"""
class Style:
    def __init__(self):
        #Create Fonts used in GUI creation
        self.default_font = ("Arial", 10, "normal")
        self.title_font = ("Roboto", 30, "bold")
        self.button_font = ("Roboto", 10, "bold")
        self.widget_font = ("Roboto", 30, "normal")

        #Dark mode
        self.primary = "#474747" #Lighter
        self.secondary = "#333333" #Darker
        self.text_color = "#76a5a6" #Light Blue
        self.accent = "#b8b8b8" #Lightest
        self.background = "#121212" #Dark background
        self.title_color = "#915b31" #Deep orange
        self.border_color = "#bababa" #Light Gray
        #Light mode


"""Custom item Widget class"""
class ItemWidget:
    def __init__(self, frame, name, count, ref_code, aisle, shelf):
        self.frame = frame
        self.name = name
        self.count = count
        self.ref_code = ref_code
        self.aisle = aisle
        self.shelf = shelf


"""Main GUI class"""
class Gui:
    def __init__(self, parent):
        self.stock_list = []
        #Frame layout
        navbar = Frame(parent, width=(window_width * 0.05), height=window_height, bg=style.secondary,
                       highlightbackground=style.accent, highlightthickness=1, bd=0, relief="solid")
        main = Frame(parent, width=(window_width * 0.95), height=window_height, bg=style.background)
        navbar.grid(row=0, column=0)
        main.grid(row=0, column=1)


        """------Nav bar------"""
        stock = Button(navbar, text="Stock", font=style.button_font, height=1, bg=style.accent, fg=style.primary, command=self.goto_stock)
        orders = Button(navbar, text="Orders", font=style.button_font, height=1, bg=style.accent, fg=style.primary, command=self.goto_orders)
        settings = Button(navbar, text="Settings", font=style.button_font, height=1, bg=style.accent, fg=style.primary, command=self.goto_settings)
        stock.pack(padx=5, pady=(window_height * 0.3)/2)
        orders.pack(padx=5, pady=(window_height * 0.3)/2)
        settings.pack(padx=5, pady=(window_height * 0.3)/2)

        """------Stock Page-------"""
        #Create stock page frame
        self.stock_page = Frame(main, height=window_height, bg=style.primary)

        """Search bar"""
        #Create search bar page frame
        stock_search = Frame(self.stock_page, bg=style.primary, 
                             highlightbackground=style.border_color, highlightthickness=1, bd=0, relief="solid")
        stock_search.pack(fill='x')

        #Title
        search_title = Label(stock_search, text="Stock", font=style.title_font, fg=style.title_color, bg=style.primary, height=(int(window_height * 0.003)))
        search_title.pack(side='left')

        divide = Frame(stock_search, bg=style.primary)
        divide.pack(side='right')

        #Reload Button
        reload_button = Button(divide, text="Reloud", font=style.default_font, command=self.reload)
        reload_button.grid(row=0, column=0)
        #Add new button
        new_item_button = Button(divide, text="+", font=style.title_font, command=self.new_item)
        new_item_button.grid(row=0,column=1)
        #Radiobutton frame
        radiobutton_frame = Frame(divide, bg=style.primary)
        radiobutton_frame.grid(row=0, column=2, padx=5)
        #Search bar frame
        search_bar_frame = Frame(divide, bg=style.primary)
        search_bar_frame.grid(row=0, column=3, padx=5)


        #Radio button for which value to search
        self.v = IntVar()
        self.v.set(1)
        search_name = Radiobutton(radiobutton_frame, variable=self.v, value="name", text="Name", bg=style.primary, fg=style.text_color, font=style.default_font)
        search_count = Radiobutton(radiobutton_frame, variable=self.v, value="count", text="Code", bg=style.primary, fg=style.text_color, font=style.default_font)
        search_ref_code = Radiobutton(radiobutton_frame, variable=self.v, value="ref_code", text="Refrence Code", bg=style.primary, fg=style.text_color, font=style.default_font)
        search_aisle = Radiobutton(radiobutton_frame, variable=self.v, value="aisle", text="Aisle", bg=style.primary, fg=style.text_color, font=style.default_font)
        search_shelf = Radiobutton(radiobutton_frame, variable=self.v, value="shelf", text="Shelf", bg=style.primary, fg=style.text_color, font=style.default_font)

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
        search_button = Button(search_bar_frame, text="Search", font=style.button_font, bg=style.accent, fg=style.primary)
        search_button.grid(row=0,column=1, padx=5)

        """Create list of items frame"""
        stock_items = Frame(self.stock_page, bg=style.primary)
        stock_items.pack()

        #Data names
        top_frame = Frame(stock_items, bg=style.primary, 
                             highlightbackground=style.border_color, highlightthickness=1, bd=0, relief="solid")
        top_frame.pack()
        item_title_padx = 92
        item_name = Label(top_frame, text="Name", padx=item_title_padx, font=style.default_font, fg=style.text_color, bg=style.primary)
        item_count = Label(top_frame, text="Count", padx=item_title_padx, font=style.default_font, fg=style.text_color, bg=style.primary)
        item_ref_code = Label(top_frame, text="Refrence code", padx=item_title_padx, font=style.default_font, fg=style.text_color, bg=style.primary)
        item_aisle = Label(top_frame, text="Aisle", padx=item_title_padx, font=style.default_font, fg=style.text_color, bg=style.primary)
        item_shelf = Label(top_frame, text="Shelf", padx=item_title_padx, font=style.default_font, fg=style.text_color, bg=style.primary)
        item_name.grid(row=0, column=0)
        item_count.grid(row=0, column=1)
        item_ref_code.grid(row=0, column=2)
        item_aisle.grid(row=0, column=3)
        item_shelf.grid(row=0, column=4)

        #Create scrollable frame
        self.scrollpage = Canvas(stock_items, height=(window_height * 0.883), width=(window_width * 0.95), bg=style.background)
        scrollbar = Scrollbar(stock_items, orient="vertical", command=self.scrollpage.yview)
        self.scrollpage.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        self.scrollpage.pack(fill="both", expand=True)

        # Configure the canvas to fit the content and enable scrolling
        stock_items.update_idletasks()  # Update the frame to get accurate width and height
        self.scrollpage.config(scrollregion=self.scrollpage.bbox("all"))

        """------Orders Page------"""
        self.orders_page = Frame(main, height=window_height, width = (window_width * 0.95), bg=style.primary)
        

        """------Settings Page------"""
        self.settings_page = Frame(main, height=window_height, width = (window_width * 0.95), bg=style.primary)

    def goto_stock(self):
        self.orders_page.forget()
        self.settings_page.forget()
        self.stock_page.pack(fill='both')

    def goto_orders(self):
        self.stock_page.forget()
        self.settings_page.forget()
        self.orders_page.pack()

    def goto_settings(self):
        self.stock_page.forget()
        self.orders_page.forget()
        self.settings_page.pack()

    def new_item(self):
        popup = Toplevel()
        popup.title("Add new item")
        popup.geometry(f"175x175+{window_x}+{window_y}")

        item_name = Label(popup, text="Item Name")
        self.item_name_entry = Entry(popup, width=10)
        item_name.grid(row=0, column=0)
        self.item_name_entry.grid(row=1, column=0)

        item_count = Label(popup, text="Current count")
        self.item_count_entry = Entry(popup, width=10)
        item_count.grid(row=0, column=1)
        self.item_count_entry.grid(row=1, column=1)

        item_aisle = Label(popup, text="Aisle")
        self.item_aisle_entry = Entry(popup, width=10)
        item_aisle.grid(row=2, column=0)
        self.item_aisle_entry.grid(row=3, column=0)

        item_shelf = Label(popup, text="Shelf")
        self.item_shelf_entry = Entry(popup, width=10)
        item_shelf.grid(row=2, column=1)
        self.item_shelf_entry.grid(row=3, column=1)

        item_ref_code = Label(popup, text="Refrence code")
        self.item_ref_code_entry = Entry(popup, width=10)
        item_ref_code.grid(row=4, column=0)
        self.item_ref_code_entry.grid(row=4, column=1)

        add = Button(popup, text="Add +", command=self.add_too_list)
        add.grid(row=5, column=1)

    def add_too_list(self):
        self.stock_list.append(ItemWidget(self.scrollpage, self.item_name_entry.get(), self.item_count_entry.get(), self.item_ref_code_entry.get(), self.item_aisle_entry.get(), self.item_shelf_entry.get()))

    def reload(self):
        rowcount=0
        for item in self.stock_list:
            self.widget = Frame(self.scrollpage)
            self.name_label = Label(self.widget, text=item.name, font=style.widget_font, bg=style.secondary, fg=style.text_color, width=int((window_width * 0.002)))
            self.count_label = Label(self.widget, text=item.count, font=style.widget_font, bg=style.secondary, fg=style.text_color, width=int((window_width * 0.002)))
            self.ref_code_label = Label(self.widget, text=item.ref_code, font=style.widget_font, bg=style.secondary, fg=style.text_color, width=int((window_width * 0.002)))
            self.aisle_label = Label(self.widget, text=item.aisle, font=style.widget_font, bg=style.secondary, fg=style.text_color, width=int((window_width * 0.002)))
            self.shelf_label = Label(self.widget, text=item.shelf, font=style.widget_font, bg=style.secondary, fg=style.text_color, width=int((window_width * 0.002)))
            
            self.name_label.grid(row=rowcount, column=0)
            self.count_label.grid(row=rowcount, column=1)
            self.ref_code_label.grid(row=rowcount, column=2)
            self.aisle_label.grid(row=rowcount, column=3)
            self.shelf_label.grid(row=rowcount, column=4)
            rowcount+=1

            self.widget.pack(fill='x')

            

            

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
    print(window_width*0.2)

    instance=Gui(root)
    root.mainloop()