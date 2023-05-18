from tkinter import *
from tkinter import messagebox

"""Style class"""
class Style:
    def __init__(self):
        #Create Fonts used in GUI creation
        self.default_font = ("Arial", 10, "normal")
        self.title_font = ("Roboto", 30, "bold")
        self.button_font = ("Roboto", 10, "bold")
        self.widget_font = ("Roboto", 15, "normal")

        self.primary = "#d2d3db"
        self.secondary = "#9394a5"
        self.text_color = "black" 
        self.accent = "#b8b8b8"
        self.background = "#fafafa"
        self.title_color = "#484b6a"
        self.border_color = "#484b6a"
        self.accent2 = "#32a852"




"""Custom item Widget class"""
class ItemWidget:
    def __init__(self, frame, name, count, ref_code, aisle, shelf):
        self.frame = frame
        self.name = name
        self.count = count
        self.ref_code = ref_code
        self.aisle = aisle
        self.shelf = shelf

        self.item_frame = Frame(self.frame, bg=style.primary)
        self.name_label = Label(self.item_frame, text=self.name, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        self.count_label = Label(self.item_frame, text=self.count, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        self.ref_code_label = Label(self.item_frame, text=self.ref_code, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        self.aisle_label = Label(self.item_frame, text=self.aisle, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        self.shelf_label = Label(self.item_frame, text=self.shelf, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        self.name_label.grid(row=0, column=0, padx=5, pady=2)
        self.count_label.grid(row=0, column=1, padx=5, pady=2)
        self.ref_code_label.grid(row=0, column=2, padx=5, pady=2)
        self.aisle_label.grid(row=0, column=3, padx=5, pady=2)
        self.shelf_label.grid(row=0, column=4, padx=5, pady=2)

"""Main GUI class"""
class Gui:
    def __init__(self, parent):
        self.main = Frame(parent)
        self.main.pack()

        self.items_list = []

        """------Nav bar------
        #Create and grid Buttons
        stock = Button(self.navbar, text="Stock", font=style.button_font, height=1, bg=style.accent, fg=style.text_color, command=self.goto_stock)
        #orders = Button(navbar, text="Orders", font=style.button_font, height=1, bg=style.accent, fg=style.text_color, command=self.goto_orders)
        shipments = Button(self.navbar, text="Shipments", font=style.button_font, height=1, bg=style.accent, fg=style.text_color, command=self.goto_shipments)
        #settings = Button(navbar, text="Settings", font=style.button_font, height=1, bg=style.accent, fg=style.text_color, command=self.goto_settings)
        stock.grid(padx=5, pady=2, row=0, column=0)
        #orders.grid(padx=5, pady=2, row=0, column=1)
        shipments.grid(padx=6, pady=2, row=0, column=2)
        #settings.grid(padx=5, pady=2, row=0, column=3)"""

        """------Stock Page-------"""
        #Create stock page frame
        self.stock_page = Frame(self.main, bg=style.primary)
        self.stock_page.pack()

        """Search tab"""
        #Create search bar page frame
        stock_search = Frame(self.stock_page, bg=style.secondary, 
                             highlightbackground=style.border_color, highlightthickness=1, bd=0, relief="solid")
        stock_search.pack(fill='x')

        #reload button
        reload_button = Button(stock_search, text="Reload", font=style.button_font, bg=style.accent, fg=style.text_color, command=self.reload_list)
        reload_button.grid(row=0, column=0, padx=5, pady=2,)
        #Add stock item button
        new_button = Button(stock_search, text="Add new stock", font=style.button_font, bg=style.accent, fg=style.text_color, command=self.new_item)
        new_button.grid(row=0, column=1, padx=5, pady=2,)
        #Add shipment button
        shipments = Button(stock_search, text="Add Shipment", font=style.button_font, bg=style.accent, fg=style.text_color, command=self.new_shipment)
        shipments.grid(row=0, column=2, padx=5, pady=2)

        #Radio button for which value to search
        radiobutton_frame = Frame(stock_search, bg=style.secondary)
        radiobutton_frame.grid(row=0, column=3, padx=5, pady=2,)
        self.v = IntVar()
        self.v.set(0)
        search_name = Radiobutton(radiobutton_frame, variable=self.v, value=0, text="Name", bg=style.secondary, fg=style.text_color, font=style.default_font)
        search_count = Radiobutton(radiobutton_frame, variable=self.v, value=1, text="Count", bg=style.secondary, fg=style.text_color, font=style.default_font)
        search_ref_code = Radiobutton(radiobutton_frame, variable=self.v, value=2, text="Refrence Code", bg=style.secondary, fg=style.text_color, font=style.default_font)
        search_aisle = Radiobutton(radiobutton_frame, variable=self.v, value=3, text="Aisle", bg=style.secondary, fg=style.text_color, font=style.default_font)
        search_shelf = Radiobutton(radiobutton_frame, variable=self.v, value=4, text="Shelf", bg=style.secondary, fg=style.text_color, font=style.default_font)

        #Grid radio buttons
        search_name.grid(row=0, column=0)
        search_count.grid(row=1, column=0)
        search_aisle.grid(row=0, column=1)
        search_shelf.grid(row=1, column=1)
        search_ref_code.grid(row=0, column=2)

        #Search bar frame
        search_bar_frame = Frame(stock_search, bg=style.secondary)
        search_bar_frame.grid(row=0, column=4, padx=5, pady=2)
        self.search_bar = Entry(search_bar_frame, width=30)
        self.search_bar.grid(row=0, column=0)
        #Search button
        search_button = Button(search_bar_frame, text="Search", font=style.button_font, bg=style.accent, fg=style.text_color, command=self.search)
        search_button.grid(row=0,column=1, padx=5)

        """List frame"""
        #Stock items list frame
        stock_items = Frame(self.stock_page, bg=style.primary)
        stock_items.pack()

        #Item titles label
        item_title = Frame(stock_items, bg=style.primary)
        item_title.pack(fill='x')

        name_label = Label(item_title, text="Name", font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        count_label = Label(item_title, text="Count", font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        ref_code_label = Label(item_title, text="Refrence code", font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        aisle_label = Label(item_title, text="Aisle", font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        shelf_label = Label(item_title, text="Shelf", font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        name_label.grid(row=0, column=0, padx=5, pady=2)
        count_label.grid(row=0, column=1, padx=5, pady=2)
        ref_code_label.grid(row=0, column=2, padx=5, pady=2)
        aisle_label.grid(row=0, column=3, padx=5, pady=2)
        shelf_label.grid(row=0, column=4, padx=5, pady=2)

        # Create a Canvas widget with a vertical Scrollbar
        self.canvas = Canvas(stock_items, height=200, bg=style.background)
        scrollbar = Scrollbar(stock_items, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a frame inside the canvas to hold the content
        self.items_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.items_frame, anchor="nw")

        # Configure the canvas to fit the content and enable scrolling
        self.items_frame.update_idletasks()  # Update the frame to get accurate width and height
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        """
        #------Orders page------#
        #Create page frame
        self.orders_page = Frame(main)
        orders_tab = Frame(self.orders_page, bg=style.primary, 
                             highlightbackground=style.border_color, highlightthickness=1, bd=0, relief="solid")
        orders_tab.pack(fill='x')
        orders_title = Label(orders_tab, text="Incoming Orders: ", fg=style.title_color, font=style.title_font, bg=style.primary)
        orders_title.grid(row=0, column=0)
        
        #Create scrollable frame
        orders_list = Frame(self.orders_page)
        orders_list.pack()
        self.orders_scrollpage = Canvas(orders_list, height=200, bg=style.background)
        scrollbar_orders = Scrollbar(orders_list, orient="vertical", command=self.orders_scrollpage.yview)
        self.orders_scrollpage.configure(yscrollcommand=scrollbar.set)
        scrollbar_orders.pack(side='right', fill='y')
        self.orders_scrollpage.pack(fill='x', expand=True)
        
        #Create a frame within the canvas to put the items into
        self.orders_item_frame = Frame(self.orders_scrollpage)
        self.orders_scrollpage.create_window((0, 0), window=self.orders_item_frame, anchor="nw")

        # Configure the canvas to fit the content and enable scrolling
        orders_list.update_idletasks()  # Update the frame to get accurate width and height
        self.orders_scrollpage.config(scrollregion=self.orders_scrollpage.bbox("all"))

        #Test label
        widget = Frame(self.orders_item_frame, bg=style.primary)
        widget.pack()
        info = Frame(widget, bg=style.primary)
        info.grid(row=0, column=0, padx=2, pady=2)
        pn_name = Label(info, text="Postal number: 1746", font=style.default_font, bg=style.primary, fg=style.text_color)
        od_name = Label(info, text="Date ordered: 16/2/19", font=style.default_font, bg=style.primary, fg=style.text_color)
        pn_name.grid(row=0, column=0, padx=2, pady=2)
        od_name.grid(row=1, column=0, padx=2, pady=2)
        it_name = Label(widget, text="Item: thing", font=style.widget_font, fg=style.text_color, bg=style.primary)
        cnt_name = Label(widget, text="Amount: 5", font=style.widget_font, fg=style.text_color, bg=style.primary)
        status_name = Label(widget, text="Status: shipped")
        status_name.grid(row=0, column=3)
        cnt_name.grid(row=0, column=1)
        it_name.grid(row=0, column=2)
        """



        """------Shipments page------"""
        #Create page frame and Title
        self.shipments_page = Frame(self.main, bg=style.background)
        enter_page = Frame(self.shipments_page, bg=style.background)
        add_shipment_l = Label(self.shipments_page, text="Add new Shipment", font=style.title_font, fg=style.title_color, bg=style.background)
        add_shipment_l.pack(padx=5, pady=2)
        enter_page.pack()

        #Entrys and labels
        shipment_title_l = Label(enter_page, text="In stock item name", font=style.default_font, fg=style.text_color, bg=style.background)
        self.shipment_title_e = Entry(enter_page)
        shipment_title_l.grid(row=0, column=0, padx=5, pady=2)
        self.shipment_title_e.grid(row=1, column=0, padx=5, pady=2)
        shipment_amount_l = Label(enter_page, text="Enter amount", font=style.default_font, fg=style.text_color, bg=style.background)
        self.shipment_amount_e = Entry(enter_page)
        shipment_amount_l.grid(row=0, column=1, padx=5, pady=2)
        self.shipment_amount_e.grid(row=1, column=1, padx=5, pady=2)

        #Add shipment button
        shipment_add_b = Button(enter_page, text="Add", font=style.button_font, fg=style.text_color, bg=style.primary, command=self.add_shipment)
        shipment_add_b.grid(row=2, column=1, padx=5, pady=2)
        #Back button
        go_back = Button(enter_page, text="Back", font=style.button_font, fg=style.text_color, bg=style.primary, command=self.load_stock)
        go_back.grid(row=2, column=0, padx=5, pady=2)
        

    def new_item(self):
        popup = Toplevel()
        popup.title("Add new item")
        popup.geometry("175x175")

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

        add = Button(popup, text="Add +", command=self.add_item)
        add.grid(row=5, column=1)

    def new_shipment(self):
        self.stock_page.forget()
        self.shipments_page.pack()

    def load_stock(self):
        self.shipments_page.forget()
        self.stock_page.pack()

    def search(self):
        for item in self.items_list:
            item.item_frame.configure(bg=style.primary)
        for item in self.items_list:
            var_list = [item.name, item.count, item.ref_code, item.aisle, item.shelf]
            print(var_list[self.v.get()])
            if self.search_bar.get() == var_list[self.v.get()]:
                self.unload_list
                item.item_frame.configure(bg=style.accent2)

    def add_item(self):
        if self.validate_str(self.item_name_entry.get()) == False: 
            messagebox.showerror("Entry error", "The name of your item cannot contain digits.")
        elif self.validate_int(self.item_count_entry.get()) == False:
            messagebox.showerror("Entry error", "Your item count cannot contain letters.")
        else:
            self.items_list.append(ItemWidget(self.items_frame, self.item_name_entry.get(), self.item_count_entry.get(), self.item_ref_code_entry.get(), self.item_aisle_entry.get(), self.item_shelf_entry.get()))
            self.item_name_entry.delete(first=0, last=100)
            self.item_aisle_entry.delete(first=0, last=100)
            self.item_count_entry.delete(first=0, last=100)
            self.item_shelf_entry.delete(first=0, last=100)
            self.item_ref_code_entry.delete(first=0, last=100)
            self.reload_list()

    def unload_list(self):
        print("unload function")
        for item in self.items_list:
            item.item_frame.forget()

    def reload_list(self):
        for item in self.items_list:
            item.item_frame.pack()
        # Configure the canvas to fit the content and enable scrolling
        self.items_frame.update_idletasks()  # Update the frame to get accurate width and height
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.main.forget()
        self.main.pack()

    def add_shipment(self):
        valid = False
        for search in self.items_list:
            if search.name == self.shipment_title_e.get():
                cont = search.count
                cont = int(cont)
                cont += int(self.shipment_amount_e.get())
                search.count = cont
                search.count_label.configure(text=cont)
                self.shipment_title_e.delete(first=0, last=100)
                self.shipment_amount_e.delete(first=0, last=100)
                valid = True
        if valid == False:
            messagebox.showerror("Error", "There is no item called ({})".format(self.shipment_title_e.get()))

    def validate_int(self, enter):
            try:
                int(enter)
            except ValueError:
                return False
            
    def validate_str(self, enter):
        for i in enter:
            try:
                int(i)
                return(False)
            except:
                print(i)
        return(True)



"""Main routine"""
if __name__ == "__main__":
    style = Style()
    root = Tk()
    root.title("Warehouse Software")
    root.configure(background=style.background)
    instance=Gui(root)
    root.mainloop()