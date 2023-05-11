import tkinter as tk

root = tk.Tk()

# Create a Canvas widget with a vertical Scrollbar
canvas = tk.Canvas(root, height=200)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Create a frame inside the canvas to hold the content
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add content to the frame
for i in range(50):
    tk.Label(frame, text=f"Label {i}").pack()

# Configure the canvas to fit the content and enable scrolling
frame.update_idletasks()  # Update the frame to get accurate width and height
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
