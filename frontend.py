import tkinter as tk

def on_button_click():
    # Code to handle button click event
    pass

# Create the main window
window = tk.Tk()
window.title("AI Desktop Assistant")

# Create GUI components
label = tk.Label(window, text="Welcome to the AI Desktop Assistant")
button = tk.Button(window, text="Click Me", command=on_button_click)

# Position GUI components using grid layout
label.grid(row=0, column=0, padx=10, pady=10)
button.grid(row=1, column=0, padx=10, pady=10)

# Start the main event loop
window.mainloop()