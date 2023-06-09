"""This program is a basic warehouse inventory tracking software."""
from tkinter import *
from tkinter import messagebox


class Style:
    """Style class holds constants used for colors and fonts in the GUI."""

    def __init__(self):
        """Create Fonts used in GUI creation."""
        self.default_font = ("Arial", 10, "normal")
        self.title_font = ("Roboto", 30, "bold")
        self.button_font = ("Roboto", 10, "bold")
        self.widget_font = ("Roboto", 15, "normal")
        self.primary = "#d2d3db" # Light gray with a hint of blue
        self.secondary = "#9394a5" # Slightly darker gray with a hint of blue
        self.text_color = "black" # Black
        self.accent = "#b8b8b8" # Darkish gray
        self.background = "#fafafa" # White
        self.title_color = "#484b6a" # Dark pastel blue
        self.border_color = "#666666" # Dark gray
        self.accent2 = "#32a852" # Light pastel green


class ItemWidget:
    """Custom item Widget class."""

    def __init__(self, frame, name, count, ref_code, aisle, shelf):
        """This function initialises the class and creates a frame with widgets of the variables inputted."""
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


class Gui:
    """Main GUI class."""

    def __init__(self, parent):
        """This function initialises the main GUI of the program."""
        self.main = Frame(parent)
        self.main.pack()
        self.items_list = []

        # Stock page
        # Create stock page frame
        self.stock_page = Frame(self.main, bg=style.primary)
        self.stock_page.pack()

        # The search tab section of the stock page.
        # Create search bar page frame
        stock_search = Frame(self.stock_page, bg=style.secondary, highlightbackground=style.border_color, highlightthickness=1, bd=0, relief="solid")
        stock_search.pack(fill='x')

        # Reload button
        reload_button = Button(stock_search, text="Reload", font=style.button_font, bg=style.accent, fg=style.text_color, command=self.reload_list)
        reload_button.grid(row=0, column=0, padx=5, pady=2, )
        # Add stock item button
        new_button = Button(stock_search, text="Add new stock", font=style.button_font, bg=style.accent, fg=style.text_color, command=self.new_item)
        new_button.grid(row=0, column=1, padx=5, pady=2, )

        # Radio button for which value to search
        radiobutton_frame = Frame(stock_search, bg=style.secondary)
        radiobutton_frame.grid(row=0, column=3, padx=5, pady=2, )
        self.rb_value = IntVar()
        self.rb_value.set(0)
        search_name = Radiobutton(radiobutton_frame, variable=self.rb_value, value=0, text="Name", bg=style.secondary, fg=style.text_color, font=style.default_font)
        search_count = Radiobutton(radiobutton_frame, variable=self.rb_value, value=1, text="Count", bg=style.secondary, fg=style.text_color, font=style.default_font)
        search_ref_code = Radiobutton(radiobutton_frame, variable=self.rb_value, value=2, text="Refrence Code", bg=style.secondary, fg=style.text_color, font=style.default_font)
        search_aisle = Radiobutton(radiobutton_frame, variable=self.rb_value, value=3, text="Aisle", bg=style.secondary, fg=style.text_color, font=style.default_font)
        search_shelf = Radiobutton(radiobutton_frame, variable=self.rb_value, value=4, text="Shelf", bg=style.secondary, fg=style.text_color, font=style.default_font)

        # Grid radio buttons
        search_name.grid(row=0, column=0)
        search_count.grid(row=1, column=0)
        search_aisle.grid(row=0, column=1)
        search_shelf.grid(row=1, column=1)
        search_ref_code.grid(row=0, column=2)

        # Search bar frame
        search_bar_frame = Frame(stock_search, bg=style.secondary)
        search_bar_frame.grid(row=0, column=4, padx=5, pady=2)
        self.search_bar = Entry(search_bar_frame, width=30)
        self.search_bar.grid(row=0, column=0)
        # Search button
        search_button = Button(search_bar_frame, text="Search", font=style.button_font, bg=style.accent, fg=style.text_color, command=self.search)
        search_button.grid(row=0, column=1, padx=5)

        # List Frame
        # Stock items list frame
        stock_items = Frame(self.stock_page, bg=style.primary)
        stock_items.pack()

        # Item titles label
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

    def new_item(self):
        """Creates a popup window to enter data in and create new items."""
        popup = Toplevel(bg=style.primary)
        popup.title("Add new item")
        popup.geometry("175x150")

        item_name = Label(popup, text="Item Name", font=style.default_font, fg=style.text_color, bg=style.primary)
        self.item_name_entry = Entry(popup, width=10)
        item_name.grid(row=0, column=0)
        self.item_name_entry.grid(row=1, column=0)

        item_count = Label(popup, text="Current count", font=style.default_font, fg=style.text_color, bg=style.primary)
        self.item_count_entry = Entry(popup, width=10)
        item_count.grid(row=0, column=1)
        self.item_count_entry.grid(row=1, column=1)

        item_aisle = Label(popup, text="Aisle", font=style.default_font, fg=style.text_color, bg=style.primary)
        self.item_aisle_entry = Entry(popup, width=10)
        item_aisle.grid(row=2, column=0)
        self.item_aisle_entry.grid(row=3, column=0)

        item_shelf = Label(popup, text="Shelf", font=style.default_font, fg=style.text_color, bg=style.primary)
        self.item_shelf_entry = Entry(popup, width=10)
        item_shelf.grid(row=2, column=1)
        self.item_shelf_entry.grid(row=3, column=1)

        item_ref_code = Label(popup, text="Refrence code", font=style.default_font, fg=style.text_color, bg=style.primary)
        self.item_ref_code_entry = Entry(popup, width=10)
        item_ref_code.grid(row=4, column=0)
        self.item_ref_code_entry.grid(row=4, column=1)

        add = Button(popup, text="Add +", command=self.add_item, font=style.button_font, bg=style.accent, fg=style.text_color)
        add.grid(row=5, column=1)

    def search(self):
        """Sets all items in the list to gray, then searches for items that match the search parameters and sets those items backgrounds to green."""
        if len(self.search_bar.get()) > 20:
            messagebox.showerror("Entry error", "Your search parameter must be less than 20 characters.")
        elif len(self.search_bar.get()) <= 20:
            for item in self.items_list:
                item.item_frame.configure(bg=style.primary)
                item.name_label.configure(bg=style.primary, fg=style.text_color)
                item.ref_code_label.configure(bg=style.primary, fg=style.text_color)
                item.count_label.configure(bg=style.primary, fg=style.text_color)
                item.aisle_label.configure(bg=style.primary, fg=style.text_color)
                item.shelf_label.configure(bg=style.primary, fg=style.text_color)
            for item in self.items_list:
                var_list = [item.name, item.count, item.ref_code, item.aisle, item.shelf]
                if self.search_bar.get() == var_list[self.rb_value.get()]:
                    item.item_frame.configure(bg=style.accent2)
                    item.name_label.configure(bg=style.accent2, fg=style.primary)
                    item.ref_code_label.configure(bg=style.accent2, fg=style.primary)
                    item.count_label.configure(bg=style.accent2, fg=style.primary)
                    item.aisle_label.configure(bg=style.accent2, fg=style.primary)
                    item.shelf_label.configure(bg=style.accent2, fg=style.primary)

    def add_item(self):
        """validates the inputs and then creates an instance of the ItemWidget subclass and appends it to a list, then clears the entrys."""
        if self.validate_str(self.item_name_entry.get(), 20) is False:
            messagebox.showerror("Entry error", "The name of your item cannot contain digits or must be shortened to less than 20 characters.")
        elif self.validate_int(self.item_count_entry.get(), 999999) is False:
            messagebox.showerror("Entry error", "Your item count cannot contain letters and must be less than 1,000,000")
        elif len(self.item_ref_code_entry.get()) > 6:
            messagebox.showerror("Entry error", "Your refrence code must be 6 digits or less.")
        else:
            self.items_list.append(ItemWidget(self.items_frame, self.item_name_entry.get(), self.item_count_entry.get(), self.item_ref_code_entry.get(), self.item_aisle_entry.get(), self.item_shelf_entry.get()))
            self.item_name_entry.delete(first=0, last=100)
            self.item_aisle_entry.delete(first=0, last=100)
            self.item_count_entry.delete(first=0, last=100)
            self.item_shelf_entry.delete(first=0, last=100)
            self.item_ref_code_entry.delete(first=0, last=100)
            self.reload_list()

    def reload_list(self):
        """Reloads the list and the main page."""
        for item in self.items_list:
            item.item_frame.pack()
        # Configure the canvas to fit the content and enable scrolling
        self.items_frame.update_idletasks()  # Update the frame to get accurate width and height
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.main.forget()
        self.main.pack()

    def validate_int(self, enter, limit):
        """Function to validate an integer"""
        try:
            int(enter)
            if int(enter) > limit:
                return False
            elif int(enter) <= limit:
                return True
        except ValueError:
            return False

    def validate_str(self, enter, limit):
        """Function to validate a string"""
        if len(enter) > limit:
            return False
        elif len(enter) <= limit:
            for i in enter:
                try:
                    int(i)
                    return False
                except ValueError:
                    i
            return True


if __name__ == "__main__":
    style = Style()
    root = Tk()
    root.title("Warehouse Software")
    root.configure(background=style.background)
    instance=Gui(root)
    root.mainloop()
