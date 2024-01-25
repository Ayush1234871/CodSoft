import tkinter as tk

def on_click(button_text):
    current_text = entry.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif button_text == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and configure the entry widget
entry = tk.Entry(root, width=16, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button_text in buttons:
    tk.Button(root, text=button_text, width=4, height=2, command=lambda text=button_text: on_click(text)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
root.mainloop()
