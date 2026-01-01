import tkinter as tk

# Button click function
def click(btn):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + btn)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

row = 1
col = 0

for btn in buttons:
    if btn == "=":
        tk.Button(root, text=btn, width=5, height=2,
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=btn, width=5, height=2,
                  command=lambda b=btn: click(b)).grid(row=row, column=col)
    
    col += 1
    if col == 4:
        col = 0
        row += 1

tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=row, column=0)

root.mainloop()