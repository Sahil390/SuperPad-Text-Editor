import tkinter as tk

def button_equal(event=None):  
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

def close_window(event=None):
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.resizable(width=False, height=False)
window.wm_iconbitmap("icons//calculator.ico")

# Create an entry widget to display the numbers and results
entry = tk.Entry(window, width=20, borderwidth=5, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.focus_set()

# Bind the Enter key to the button_equal() function
window.bind('<Return>', button_equal)

# Bind the Esc key to the close_window() function
window.bind('<Escape>', close_window)

# Start the main loop
window.mainloop()
