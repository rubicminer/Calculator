from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("Calculator")
window.resizable(False, False)

Calculation_Part_Shown_Update = ""
Calculation_Part_Shown_Text = StringVar()
Calculation_Part_Shown = Label(window, textvariable=Calculation_Part_Shown_Text, bd=15, relief=SUNKEN, font=12)
Calculation_Part_Shown_Text.set("")
Calculation_Part_Shown.grid(columnspan=5, sticky=EW)
Calculation_Part_Shown.configure(background="#c2c8cf")
Q, U, I, T = 0, 0, 0, 0


def Button_Click(num):
    global Calculation_Part_Shown_Update
    a = []
    for i in Calculation_Part_Shown_Update:
        a.append(i)
    if (len(a)) == 30:
        return
    if num == ".":
        dots_amount = 0
        for i in a:
            if i == ".":
                dots_amount += 1
            elif i == "+" or i == "-" or i == "*" or i == "*" or i == "/" or i == "(" or i == ")" or i == "^" or \
                    i == "√":
                dots_amount = 0
        if dots_amount >= 1:
            return
    if Calculation_Part_Shown_Update == "":
        if num == "+":
            return
        elif num == "*":
            return
        elif num == "/":
            return
        elif num == ".":
            Calculation_Part_Shown_Update = "0"
        elif num == ")":
            return
        elif num == "^":
            return
    else:
        Parentheses_amount = 0
        for i in Calculation_Part_Shown_Update:
            if i == "(":
                Parentheses_amount = Parentheses_amount + 1
            elif i == ")":
                Parentheses_amount = Parentheses_amount - 1

        b = a[(len(a)) - 1]
        if b == "+":
            if num == "+" or num == "-" or num == "*" or num == "/" or num == ")" or num == "^":
                return
            elif num == ".":
                num = "0."
        elif b == "-":
            if num == "+" or num == "-" or num == "*" or num == "/" or num == ")" or num == "^":
                return
            elif num == ".":
                num = "0."
        elif b == "*":
            if num == "+" or num == "-" or num == "*" or num == "/" or num == ")" or num == "^":
                return
            elif num == ".":
                num = "0."
        elif b == "/":
            if num == "+" or num == "-" or num == "*" or num == "/" or num == ")" or num == "^":
                return
            elif num == ".":
                num = "0."
        elif b == ".":
            if num == "+" or num == "-" or num == "*" or num == "/" or num == "(" or num == ")" or num == "^" or num == ".":
                return
        elif b == "(":
            if num == ")" or num == "/" or num == "*" or num == "^":
                return
            if num == ".":
                num = "0."
            elif num == "(":
                if Parentheses_amount >= 5:
                    return
        elif b == ")":
            if num == "(" or num == "√" or num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or \
                    num == 7 or num == 8 or num == 9 or num == 0:
                num = f"*{num}"
            elif num == ".":
                num = "0."
            elif num == ")":
                if Parentheses_amount <= 0:
                    return
            elif num == "^":
                return
        elif b == "^":
            if num == "+" or num == "-" or num == "*" or num == "/" or num == ")" or num == "^":
                return
            elif num == ".":
                num = "0."
        elif b == "1" or b == "2" or b == "3" or b == "4" or b == "5" or b == "6" or b == "7" or b == "8" or b == "9" \
                or b == "0":
            if num == "(" or num == "√":
                num = f"*{num}"
            elif num == ")":
                if Parentheses_amount <= 0:
                    return
        elif b == "√":
            if num == "√":
                return
    Calculation_Part_Shown_Update = Calculation_Part_Shown_Update + str(num)
    Calculation_Part_Shown_Text.set(Calculation_Part_Shown_Update)


def Equal_Click():
    global Calculation_Part_Shown_Update
    if Calculation_Part_Shown_Update == "":
        return
    a = []
    change = "no"
    change2 = "no"
    for i in Calculation_Part_Shown_Update:
        a.append(i)
    for number, character in enumerate(a):
        if character == "^":
            a[number] = "**"
            change = "yes"
    for number, character in enumerate(a):
        if change2 == "yes":
            if a[number] == a[len(a) - 1] or a[number + 1] == "+" or a[number + 1] == "-" or a[number + 1] == "*" or a[
                number + 1] == "/" or \
                    a[number + 1] == "**" or a[number + 1] == "√":
                a.insert((number + 1), "**(1 / 2))")
                change2 = "no"
        if character == "√":
            if a[number - 1] == ")":
                a[number] = "("
            else:
                a[number] = "("
            change2 = "yes"
            change = "yes"

    if change == "yes":
        Calculation_Part_Shown_Update = ""
        for i in a:
            Calculation_Part_Shown_Update += i
    if a[len(a) - 1] == "+" or a[len(a) - 1] == "-" or a[len(a) - 1] == "*" or a[len(a) - 1] == "/" or a[len(a) - 1] \
            == "^":
        return
    elif a[len(a) - 1] == ".":
        Calculation_Part_Shown_Update += "0"
        Total = round(eval(Calculation_Part_Shown_Update), 1)
        Total = str(Total)
        Calculation_Part_Shown_Update = Total
        Calculation_Part_Shown_Text.set(Calculation_Part_Shown_Update)
    try:
        Total = round(eval(Calculation_Part_Shown_Update), 5)
        Total = str(Total)
        Calculation_Part_Shown_Update = Total
    except ZeroDivisionError:
        tkinter.messagebox.showerror("Division By Zero", "Sorry, but in math, `/0` is not defined!")
        Calculation_Part_Shown_Update = ""
        Calculation_Part_Shown_Text.set(Calculation_Part_Shown_Update)
    if len(Calculation_Part_Shown_Update) >= 30:
        tkinter.messagebox.showerror("Too much numbers", "Sorry, but answers with more than 30 numbers aren't allowed!")
        Calculation_Part_Shown_Update = ""
        Calculation_Part_Shown_Text.set(Calculation_Part_Shown_Update)
        return
    else:
        Calculation_Part_Shown_Text.set(Calculation_Part_Shown_Update)


def Clear_Click():
    global Calculation_Part_Shown_Update
    Calculation_Part_Shown_Update = ""
    Calculation_Part_Shown_Text.set(Calculation_Part_Shown_Update)


def BackSpace_Click():
    global Calculation_Part_Shown_Update
    if Calculation_Part_Shown_Update == "":
        return
    a = []
    for i in Calculation_Part_Shown_Update:
        a.append(i)
    b = a[(len(a) - 1)]
    a = a[::-1]
    a.remove(b)
    a = a[::-1]
    b = ""
    for i in a:
        b = b + i
    Calculation_Part_Shown_Update = b
    Calculation_Part_Shown_Text.set(Calculation_Part_Shown_Update)


def Number1_Click(event):
    Button_Click("1")


def Number2_Click(event):
    Button_Click("2")


def Number3_Click(event):
    Button_Click("3")


def Number4_Click(event):
    Button_Click("4")


def Number5_Click(event):
    Button_Click("5")


def Number6_Click(event):
    Button_Click("6")


def Number7_Click(event):
    Button_Click("7")


def Number8_Click(event):
    Button_Click("8")


def Number9_Click(event):
    Button_Click("9")


def Number0_Click(event):
    Button_Click("0")


def Float_Click(event):
    Button_Click(".")


def Plus_Click(event):
    Button_Click("+")


def Minus_Click(event):
    Button_Click("-")


def Multiply_Click(event):
    Button_Click("*")


def Division_Click(event):
    Button_Click("/")


def Open_Parenthese_Click(event):
    Button_Click("(")


def Close_Parenthese_Click(event):
    Button_Click(")")


def Power_Click(event):
    Button_Click("^")


def Radical_Click(event):
    Button_Click("√")


def Equal_Click_Keyboard(event):
    Equal_Click()


def BackSpace_Click_Keyboard(event):
    BackSpace_Click()


def Shift_Click(event):
    return


def Clear_Click_Keyboard(event):
    Clear_Click()


def Space_Click(event):
    return


def Quit_Q(event):
    global Q
    Q = 1


def Quit_U(event):
    global Q
    if Q == 1:
        global U
        U = 1
    else:
        return


def Quit_I(event):
    global U
    if U == 1:
        global I
        I = 1
    else:
        return


def Quit_T(event):
    global I
    if I == 1:
        window.destroy()
    else:
        return


Button_1 = Button(window, text="1", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(1), bd=3, font=10)
Button_1.grid(row=2)
Button_1.configure(background="#1e98ba")
Button_2 = Button(window, text="2", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(2), bd=3, font=10)
Button_2.grid(row=2, column=1)
Button_2.configure(background="#1e98ba")
Button_3 = Button(window, text="3", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(3), bd=3, font=10)
Button_3.grid(row=2, column=2)
Button_3.configure(background="#1e98ba")
Button_4 = Button(window, text="4", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(4), bd=3, font=10)
Button_4.grid(row=3)
Button_4.configure(background="#1e98ba")
Button_5 = Button(window, text="5", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(5), bd=3, font=10)
Button_5.grid(row=3, column=1)
Button_5.configure(background="#1e98ba")
Button_6 = Button(window, text="6", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(6), bd=3, font=10)
Button_6.grid(row=3, column=2)
Button_6.configure(background="#1e98ba")
Button_7 = Button(window, text="7", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(7), bd=3, font=10)
Button_7.grid(row=4)
Button_7.configure(background="#1e98ba")
Button_8 = Button(window, text="8", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(8), bd=3, font=10)
Button_8.grid(row=4, column=1)
Button_8.configure(background="#1e98ba")
Button_9 = Button(window, text="9", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(9), bd=3, font=10)
Button_9.grid(row=4, column=2)
Button_9.configure(background="#1e98ba")
Button_0 = Button(window, text="0", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(0), bd=3, font=10)
Button_0.grid(row=5, columnspan=2, sticky=EW)
Button_0.configure(background="#1e98ba")
Float_Button = Button(window, text=".", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click("."), bd=3,
                      font=10)
Float_Button.grid(row=5, column=2)
Float_Button.configure(background="#1e98ba")
Equal_Button = Button(window, text="=", width=5, height=2, padx=3, pady=3, command=Equal_Click, bd=3, font=10)
Equal_Button.grid(row=4, column=4, rowspan=2, sticky=NS)
Equal_Button.configure(background="#20a9b3")
Plus_Button = Button(window, text="+", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click("+"), bd=3,
                     font=10)
Plus_Button.grid(row=2, column=3)
Plus_Button.configure(background="#20a9b3")
Minus_Button = Button(window, text="-", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click("-"), bd=3,
                      font=10)
Minus_Button.grid(row=3, column=3)
Minus_Button.configure(background="#20a9b3")
Multiply_Button = Button(window, text="*", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click("*"), bd=3,
                         font=10)
Multiply_Button.grid(row=4, column=3)
Multiply_Button.configure(background="#20a9b3")
Division_Button = Button(window, text="/", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click("/"), bd=3,
                         font=10)
Division_Button.grid(row=5, column=3)
Division_Button.configure(background="#20a9b3")
Parenthese_Open_Button = Button(window, text="(", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click("("),
                                bd=3, font=10)
Parenthese_Open_Button.grid(row=1, column=3)
Parenthese_Open_Button.configure(background="#20a9b3")
Parenthese_Close_Button = Button(window, text=")", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click(")"),
                                 bd=3, font=10)
Parenthese_Close_Button.grid(row=1, column=4)
Parenthese_Close_Button.configure(background="#20a9b3")
Power_Button = Button(window, text="^", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click("^"), bd=3,
                      font=10)
Power_Button.grid(row=3, column=4)
Power_Button.configure(background="#20a9b3")
Radical_Button = Button(window, text="√", width=5, height=2, padx=3, pady=3, command=lambda: Button_Click("√"), bd=3,
                        font=10)
Radical_Button.grid(row=2, column=4)
Radical_Button.configure(background="#20a9b3")
Clear_Button = Button(window, text="C", width=5, height=2, padx=3, pady=3, command=Clear_Click, bd=3, font=10)
Clear_Button.grid(row=1, column=2, sticky=NS)
Clear_Button.configure(background="#1164bd")
BackSpace_Button = Button(window, text="<==", width=5, height=2, padx=3, pady=3, command=BackSpace_Click, bd=3, font=10)
BackSpace_Button.grid(row=1, columnspan=2, sticky=EW)
BackSpace_Button.configure(background="#1164bd")

window.bind("<KeyPress-1>", Number1_Click)
window.bind("<KeyPress-2>", Number2_Click)
window.bind("<KeyPress-3>", Number3_Click)
window.bind("<KeyPress-4>", Number4_Click)
window.bind("<KeyPress-5>", Number5_Click)
window.bind("<KeyPress-6>", Number6_Click)
window.bind("<KeyPress-7>", Number7_Click)
window.bind("<KeyPress-8>", Number8_Click)
window.bind("<KeyPress-9>", Number9_Click)
window.bind("<KeyPress-0>", Number0_Click)
window.bind("<KeyPress-.>", Float_Click)
window.bind("<KeyPress-+>", Plus_Click)
window.bind("<KeyPress-->", Minus_Click)
window.bind("<KeyPress-*>", Multiply_Click)
window.bind("<KeyPress-/>", Division_Click)
window.bind("<Return>", Equal_Click_Keyboard)
window.bind("<BackSpace>", BackSpace_Click_Keyboard)
window.bind("<Shift_L>", Shift_Click)
window.bind("<Escape>", Clear_Click_Keyboard)
window.bind("<space>", Space_Click)
window.bind("<KeyPress-Q>", Quit_Q)
window.bind("<KeyPress-u>", Quit_U)
window.bind("<KeyPress-i>", Quit_I)
window.bind("<KeyPress-t>", Quit_T)
window.bind("<KeyPress-=>", Equal_Click_Keyboard)
window.bind("<KeyPress-(>", Open_Parenthese_Click)
window.bind("<KeyPress-)>", Close_Parenthese_Click)
window.bind("<KeyPress-^>", Power_Click)
window.bind("<KeyPress-&>", Radical_Click)

window.mainloop()
