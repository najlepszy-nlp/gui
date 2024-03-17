import tkinter as tk
import sys
from tkinter import ttk
import tkintermapview

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Complex Layout")

    # Set the window size to 800x600
    root.geometry("800x600")

    # Set a white background color explicitly
    root.configure(bg="white")
    
    # Create two frames
    left_frame = tk.Frame(root, bg="white", width=200, height=600)  # Green background
    right_frame = tk.Frame(root, bg="white", height=600)  # Blue background

    # Set the weights to make the right frame take the rest of the width
    root.grid_columnconfigure(1, weight=1)

    # Place the frames using the grid layout manager
    left_frame.grid(row=0, column=0, sticky="nsew")
    right_frame.grid(row=0, column=1, sticky="nsew")

    # Create a list of frames in the left frame (scrollable)
    list_frame = ttk.Frame(left_frame)
    list_frame.grid(row=0, column=0, sticky="nsew")

    # Configure the row to expand vertically
    left_frame.grid_rowconfigure(0, weight=1)

    # Create a scrollbar for the list
    scrollbar = ttk.Scrollbar(list_frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    # Create a canvas to hold the list of frames
    canvas = tk.Canvas(list_frame, yscrollcommand=scrollbar.set, bg="white")
    canvas.pack(side="left", fill="both", expand=True)

    # Configure the scrollbar to work with the canvas
    scrollbar.config(command=canvas.yview)

    # Create a frame inside the canvas to hold the widgets
    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    # Add some example divs to the list
    for i in range(20):
        div = tk.Frame(inner_frame, bg="lightgray", pady=10, padx=5, borderwidth=2, relief="solid")
        div.grid(row=i, column=0, sticky="ew")

    # Input section at the bottom of the left frame
    input_frame = tk.Frame(left_frame, padx=10, pady=5, bg="white")
    input_frame.grid(row=1, column=0, sticky="ew")

    # Create the text input with placeholder
    entry_placeholder = "Type in the event name"
    entry_var = tk.StringVar()
    entry = tk.Entry(input_frame, textvariable=entry_var, bg="white", relief="solid", borderwidth=1, width=20, fg="black")
    entry.insert(0, entry_placeholder)
    entry.bind("<FocusIn>", lambda event: entry.delete(0, "end") if entry_var.get() == entry_placeholder else None)
    entry.bind("<FocusOut>", lambda event: entry_var.set(entry_placeholder) if not entry_var.get() else None)
    entry.grid(row=0, column=0, padx=(0, 5), sticky="ew")

    # Create the Search button
    search_button = tk.Button(input_frame, text="Search", command=lambda: search_event(entry_var.get()))
    search_button.grid(row=0, column=1, padx=(5, 0), sticky="ew")
    map_widget = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0)
    map_widget.grid(row=0, column=1, sticky="ew")
    # Run the Tkinter event loop
    root.mainloop()

def search_event(event_name):
    # Add your search logic here
    print("Searching for:", event_name)

if __name__ == "__main__":
    main()
