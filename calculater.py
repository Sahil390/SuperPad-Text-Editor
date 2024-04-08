import tkinter as tk


def calculator():
    def button_click(number):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + str(number))

    def button_clear():
        entry.delete(0, tk.END)

    def button_equal(event=None):  # Add event parameter
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    # Create the main window
    window = tk.Tk()
    window.title("Calculator")

    # Create an entry widget to display the numbers and results
    entry = tk.Entry(window, width=20, borderwidth=5, font=("Arial", 20))
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Bind the Enter key to the button_equal() function
    window.bind('<Return>', button_equal)

    # Start the main loop
    window.mainloop()


