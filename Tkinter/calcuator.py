import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

tk.Button(root, text="1", command=lambda:add_to_calculation(1), width=5).grid(row=2, column=1)
tk.Button(root, text="2", command=lambda:add_to_calculation(2), width=5).grid(row=2, column=2)
tk.Button(root, text="3", command=lambda:add_to_calculation(3), width=5).grid(row=2, column=3)

tk.Button(root, text="4", command=lambda:add_to_calculation(4), width=5).grid(row=3, column=1)
tk.Button(root, text="5", command=lambda:add_to_calculation(5), width=5).grid(row=3, column=2)
tk.Button(root, text="6", command=lambda:add_to_calculation(6), width=5).grid(row=3, column=3)

tk.Button(root, text="7", command=lambda:add_to_calculation(7), width=5).grid(row=4, column=1)
tk.Button(root, text="8", command=lambda:add_to_calculation(8), width=5).grid(row=4, column=2)
tk.Button(root, text="9", command=lambda:add_to_calculation(9), width=5).grid(row=4, column=3)

tk.Button(root, text="0", command=lambda:add_to_calculation(0), width=5).grid(row=5, column=2)

tk.Button(root, text="+", command=lambda:add_to_calculation("+"), width=5).grid(row=2, column=4)
tk.Button(root, text="-", command=lambda:add_to_calculation("-"), width=5).grid(row=3, column=4)
tk.Button(root, text="x", command=lambda:add_to_calculation("*"), width=5).grid(row=4, column=4)
tk.Button(root, text="/", command=lambda:add_to_calculation("/"), width=5).grid(row=5, column=4)

tk.Button(root, text="(", command=lambda:add_to_calculation("("), width=5).grid(row=5, column=1)
tk.Button(root, text=")", command=lambda:add_to_calculation(")"), width=5).grid(row=5, column=3)

tk.Button(root, text="C", command=clear_field, width=11).grid(row=6, column=1, columnspan=2)
tk.Button(root, text="=", command=evaluate_calculation, width=11).grid(row=6, column=3, columnspan=2)

root.mainloop()