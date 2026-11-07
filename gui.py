import tkinter as tk
import calculator



root = tk.Tk()

root.title("Smart Calculator")
root.geometry("400x500")
root.configure(bg="#1e1e2e")

#label
label= tk.Label(root, text= "SMART CALCULATOR", font=("Arial", 20, "bold"), bg="#1e1e2e", fg="white")
label.pack(pady=20)

#display
display= tk.Entry(root, font=("Arial", 24), bg="#313244", fg="white", justify="right",width=20,relief="flat",borderwidth=10)

display.pack()
display.insert(0,"0")
first_number=0
operation=""



#frame
button_frame=tk.Frame(root)
button_frame.pack()
number_style = {
    "font": ("Arial", 18),
    "bg": "#45475a",
    "fg": "black",
    "activebackground": "#585b70",
    "activeforeground": "white",
    "width": 5,
    "height": 2,
    "relief": "flat"
}
operation_style = {
    "font": ("Arial", 18, "bold"),
    "bg": "#89b4fa",
    "fg": "#1e1e2e",
    "activebackground": "#74c7ec",
    "width": 5,
    "height": 2,
    "relief": "flat"
}

equals_style = {
    "font": ("Arial", 18, "bold"),
    "bg": "#a6e3a1",
    "fg": "#1e1e2e",
    "activebackground": "#94e2d5",
    "width": 5,
    "height": 2,
    "relief": "flat"
}
clear_style = {
    "font": ("Arial", 18, "bold"),
    "bg": "#f38ba8",
    "fg": "#1e1e2e",
    "activebackground": "#eba0ac",
    "width": 5,
    "height": 2,
    "relief": "flat"
}

def button_insertion(value):
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
        display.insert(tk.END, value)
    else:
        display.insert(tk.END, value)
#button 7
button7=tk.Button(button_frame, text="7",command=lambda: button_insertion("7"), **number_style)
button7.grid(row=0, column=0)

#button8
button8 = tk.Button(
    button_frame,
    text="8",
    command=lambda: button_insertion("8"),**number_style
)
button8.grid(row=0, column=1)

#button9
button9 = tk.Button(
    button_frame,
    text="9",
    command=lambda: button_insertion("9"),**number_style
)
button9.grid(row=0, column=2)

# 4
button4 = tk.Button(button_frame, text="4",
                    command=lambda: button_insertion("4"),**number_style)
button4.grid(row=1, column=0)

# 5
button5 = tk.Button(button_frame, text="5",
                    command=lambda: button_insertion("5"),**number_style)
button5.grid(row=1, column=1)

# 6
button6 = tk.Button(button_frame, text="6",
                    command=lambda: button_insertion("6"),**number_style)
button6.grid(row=1, column=2)

# 1
button1 = tk.Button(button_frame, text="1",
                    command=lambda: button_insertion("1"),**number_style)
button1.grid(row=2, column=0)

# 2
button2 = tk.Button(button_frame, text="2",
                    command=lambda: button_insertion("2"),**number_style)
button2.grid(row=2, column=1)

# 3
button3 = tk.Button(button_frame, text="3",
                    command=lambda: button_insertion("3"),**number_style)
button3.grid(row=2, column=2)

# 0
button0 = tk.Button(button_frame, text="0",
                    command=lambda: button_insertion("0"),**number_style)
button0.grid(row=3, column=1)

# Division
def choose_division():
    global first_number, operation
    first_number = float(display.get())
    operation = "÷"
    display.delete(0, tk.END)
divide_button = tk.Button(button_frame, text="÷", command=lambda: choose_division(), **operation_style)
divide_button.grid(row=0, column=3)

# Multiplication
def choose_multiplication():
    global first_number, operation
    first_number = float(display.get())
    operation = "×"
    display.delete(0, tk.END)
multiply_button = tk.Button(button_frame, text="×", command=lambda: choose_multiplication(), **operation_style)
multiply_button.grid(row=1, column=3)

# Subtraction
def choose_subtraction():
    global first_number, operation
    first_number = float(display.get())
    operation = "-"
    display.delete(0, tk.END)
minus_button = tk.Button(button_frame, text="-", command=lambda: choose_subtraction(), **operation_style)
minus_button.grid(row=2, column=3)

# Addition
def choose_addition():
    global first_number, operation
    first_number = float(display.get())
    operation = "+"
    display.delete(0, tk.END)
plus_button = tk.Button(button_frame, text="+", command=lambda: choose_addition(), **operation_style)
plus_button.grid(row=3, column=3)


#clear button
def clear_display():
    global operation, first_number
    display.delete(0, tk.END)
    display.insert(0, "0")
    first_number=0
    operation=""
clear_button= tk.Button(button_frame, text="C", command=clear_display,**clear_style)
clear_button.grid(row=3, column=0)



#equal button

def calculate():
    if operation=="":
        display.delete(0,tk.END)
        display.insert(0,"Select an operation")
        return
    try:
        second_number = float(display.get())
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Invalid input")
        return

    if operation == "+":
        result = calculator.add(first_number, second_number)

    elif operation == "-":
        result = calculator.subtract(first_number, second_number)

    elif operation == "×":
        result = calculator.multiply(first_number, second_number)

    elif operation == "÷":
        if second_number==0:
            display.delete(0,tk.END)
            display.insert(0,"Error")
            return
        else:
            result = calculator.divide(first_number, second_number)

    display.delete(0, tk.END)
    display.insert(0, str(result))

equal_button = tk.Button(button_frame,text="=",command=calculate,**equals_style)
equal_button.grid(row=4, column=2)


root.mainloop()
