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
        self.primary = "#d2d3db"
        self.secondary = "#9394a5"
        self.text_color = "black" 
        self.accent = "#b8b8b8"
        self.background = "#fafafa"
        self.title_color = "#484b6a"
        self.border_color = "#484b6a"
        #Light mode


"""Custom item Widget class"""
class ItemWidget:
    def __init__(self, frame, name, count, ref_code, aisle, shelf):
        self.frame = frame
        self.name = name
        self.count = int(count)
        self.ref_code = ref_code
        self.aisle = aisle
        self.shelf = shelf

        self.item_frame = Frame(self.frame, bg=style.primary)
        self.name_label = Label(self.item_frame, text=self.name, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        self.count_label = Label(self.item_frame, text=self.count, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        ref_code_label = Label(self.item_frame, text=self.ref_code, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        aisle_label = Label(self.item_frame, text=self.aisle, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        shelf_label = Label(self.item_frame, text=self.shelf, font=style.default_font, fg=style.text_color, bg=style.primary, width=20)
        self.name_label.grid(row=0, column=0, padx=5, pady=2)
        self.count_label.grid(row=0, column=1, padx=5, pady=2)
        ref_code_label.grid(row=0, column=2, padx=5, pady=2)
        aisle_label.grid(row=0, column=3, padx=5, pady=2)
        shelf_label.grid(row=0, column=4, padx=5, pady=2)

"""Main GUI class"""
class Gui:
    def __init__(self, parent):
        navbar = Frame(parent, bg=style.secondary)
        main = Frame(parent)
        navbar.pack(fill='x', side='top')
        main.pack()

        self.items_list = []

        """------Nav bar------"""
        #Create and grid Buttons
        stock = Button(navbar, text="Stock", font=style.button_font, height=1, bg=style.accent, fg=style.text_color, command=self.goto_stock)
        orders = Button(navbar, text="Orders", font=style.button_font, height=1, bg=style.accent, fg=style.text_color, command=self.goto_orders)
        shipments = Button(navbar, text="Shipments", font=style.button_font, height=1, bg=style.accent, fg=style.text_color, command=self.goto_shipments)
        settings = Button(navbar, text="Settings", font=style.button_font, height=1, bg=style.accent, fg=style.text_color, command=self.goto_settings)
        stock.grid(padx=5, pady=2, row=0, column=0)
        orders.grid(padx=5, pady=2, row=0, column=1)
        shipments.grid(padx=6, pady=2, row=0, column=2)
        settings.grid(padx=5, pady=2, row=0, column=3)

        """------Stock Page-------"""
        #Create stock page frame
        self.stock_page = Frame(main, bg=style.primary)

        """Search tab"""
        #Create search bar page frame
        stock_search = Frame(self.stock_page, bg=style.primary, 
                             highlightbackground=style.border_color, highlightthickness=1, bd=0, relief="solid")
        stock_search.pack(fill='x')

        #reload button
        reload_button = Button(stock_search, text="Reload", font=style.button_font, bg=style.accent, fg=style.text_color, command=self.reload_list)
        reload_button.grid(row=0, column=0, padx=5, pady=2,)
        #Add stock item button
        new_button = Button(stock_search, text="Add new stock", font=style.button_font, bg=style.accent, fg=style.text_color, command=self.new_item)
        new_button.grid(row=0, column=1, padx=5, pady=2,)

        #Radio button for which value to search
        radiobutton_frame = Frame(stock_search, bg=style.primary)
        radiobutton_frame.grid(row=0, column=2, padx=5, pady=2,)
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
        search_bar_frame = Frame(stock_search, bg=style.primary)
        search_bar_frame.grid(row=0, column=3, padx=5, pady=2)
        search_bar = Entry(search_bar_frame, width=30)
        search_bar.grid(row=0, column=0)
        #Search button
        search_button = Button(search_bar_frame, text="Search", font=style.button_font, bg=style.accent, fg=style.text_color)
        search_button.grid(row=0,column=1, padx=5)

        """List frame"""
        #Stock items list frame
        stock_items = Frame(self.stock_page, bg=style.primary)
        stock_items.pack()

        #Item titles label
        item_title = Frame(stock_items)
        item_title.pack(fill='x')

        name_label = Label(item_title, text="Name", font=style.default_font, fg=style.text_color, width=20)
        count_label = Label(item_title, text="Count", font=style.default_font, fg=style.text_color, width=20)
        ref_code_label = Label(item_title, text="Refrence code", font=style.default_font, fg=style.text_color, width=20)
        aisle_label = Label(item_title, text="Aisle", font=style.default_font, fg=style.text_color, width=20)
        shelf_label = Label(item_title, text="Shelf", font=style.default_font, fg=style.text_color, width=20)
        name_label.grid(row=0, column=0, padx=5, pady=2)
        count_label.grid(row=0, column=1, padx=5, pady=2)
        ref_code_label.grid(row=0, column=2, padx=5, pady=2)
        aisle_label.grid(row=0, column=3, padx=5, pady=2)
        shelf_label.grid(row=0, column=4, padx=5, pady=2)

        #Create scrollable canvas
        self.scrollpage = Canvas(stock_items, height=200, bg=style.background)
        scrollbar = Scrollbar(stock_items, orient="vertical", command=self.scrollpage.yview)
        self.scrollpage.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        self.scrollpage.pack(fill="x", expand=True)

        #Create a frame within the canvas to put the items into
        self.items_frame = Frame(self.scrollpage)
        self.scrollpage.create_window((0, 0), window=self.items_frame, anchor="nw")

        # Configure the canvas to fit the content and enable scrolling
        stock_items.update_idletasks()  # Update the frame to get accurate width and height
        self.scrollpage.config(scrollregion=self.scrollpage.bbox("all"))


        """------Orders page------"""
        #Create page frame
        self.orders_page = Frame(main)


        """------Shipments page------"""
        #Create page frame and Title
        self.shipments_page = Frame(main, bg=style.background)
        self.shipments_page.pack()
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
        shipment_add_b.grid(row=2, columnspan=2, padx=5, pady=2)


        """------Settings page------"""
        #Create page frame
        self.settings_page = Frame(main)



    def goto_stock(self):
        self.orders_page.forget()
        self.shipments_page.forget()
        self.settings_page.forget()
        self.stock_page.pack()

    def goto_orders(self):
        self.stock_page.forget()
        self.settings_page.forget()
        self.shipments_page.forget()
        self.orders_page.pack()

    def goto_settings(self):
        self.stock_page.forget()
        self.orders_page.forget()
        self.shipments_page.forget()
        self.settings_page.pack()

    def goto_shipments(self):
        self.stock_page.forget()
        self.orders_page.forget()
        self.settings_page.forget()
        self.shipments_page.pack()

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

    def add_item(self):
        self.items_list.append(ItemWidget(self.items_frame, self.item_name_entry.get(), self.item_count_entry.get(), self.item_ref_code_entry.get(), self.item_aisle_entry.get(), self.item_shelf_entry.get()))

    def reload_list(self):
        for item in self.items_list:
            item.item_frame.forget()
        for item in self.items_list:
            item.item_frame.pack()

    def add_shipment(self):
        valid = False
        for search in self.items_list:
            if search.name == self.shipment_title_e.get():
                cont = search.count
                cont = int(cont)
                cont += int(self.shipment_amount_e.get())
                search.count = cont
                search.count_label.configure(text=cont)
                valid = True
        if valid == False:
            messagebox.showerror("Error", "There is no item called ({})".format(self.shipment_title_e.get()))
        


"""Main routine"""
if __name__ == "__main__":
    style = Style()
    root = Tk()
    root.title("Warehouse Software")
    root.configure(background=style.background)
    instance=Gui(root)
    root.mainloop()