#Simple GUIvcalculator using tkinter
import tkinter  
from tkinter import *  
from tkinter import messagebox  

var = ""  
A = 0  
operator = ""  

def button_1_is_Clicked():  
    global var  
    var = var + "1"  
    the_data.set(var)  
def button_2_is_Clicked():  
    global var  
    var = var + "2"  
    the_data.set(var)  
def button_3_is_Clicked():  
    global var  
    var = var + "3"  
    the_data.set(var)  
def button_4_is_Clicked():  
    global var  
    var = var + "4"  
    the_data.set(var)  
def button_5_is_Clicked():  
    global var  
    var = var + "5"  
    the_data.set(var)  
def button_6_is_Clicked():  
    global var  
    var = var + "6"  
    the_data.set(var)
def button_7_is_Clicked():  
    global var  
    var = var + "7"  
    the_data.set(var) 
def button_8_is_Clicked():  
    global var  
    var = var + "8"  
    the_data.set(var)  
def button_9_is_Clicked():  
    global var  
    var = var + "9"  
    the_data.set(var)  
def button_0_is_Clicked():  
    global var  
    var = var + "0"  
    the_data.set(var)  

def button_Add_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "+"  
    var = var + "+"  
    the_data.set(var)  

def button_Sub_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "-"  
    var = var + "-"  
    the_data.set(var)  

def button_Mul_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "*"  
    var = var + "*"  
    the_data.set(var) 

def button_Div_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "/"  
    var = var + "/"  
    the_data.set(var)  

def button_Equal_is_Clicked():  
    global A  
    global var  
    global operator  
    A = float(var)  
    operator = "="  
    var = var + "="  
    the_data.set(var)  

def button_C_is_Clicked():  
    global A  
    global var  
    global operator  
    var = ""  
    A = 0  
    operator = ""  
    the_data.set(var)  


def res():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Division by 0 Not Allowed.")  
            A == ""  
            var = ""  
            the_data.set(var)  
        else:  
            x = float(A/a)  
            the_data.set(x)  
            var = str(x)  

guiWindow = tkinter.Tk() 
guiWindow.geometry("320x500+400+400") 
guiWindow.resizable(0, 0)  
guiWindow.title("Calculator")  

the_data = StringVar()  
guiLabel = Label(  
    guiWindow,  
    text = "Label",  
    anchor = SE,  
    font = ("Cambria Math", 20),  
    textvariable = the_data,  
    background = "#ffffff",  
    fg = "#000000"  
)  
guiLabel.pack(expand = True, fill = "both") 
frameOne = Frame(guiWindow, bg = "#000000")  
frameOne.pack(expand = True, fill = "both")
frameTwo = Frame(guiWindow, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
frameThree = Frame(guiWindow, bg = "#000000")  
frameThree.pack(expand = True, fill = "both") 
frameFour = Frame(guiWindow, bg = "#000000")  
frameFour.pack(expand = True, fill = "both")  

buttonONE = Button(  
    frameOne,  
    text = "1",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_1_is_Clicked  
)  
buttonONE.pack(side = LEFT, expand = True, fill = "both")  
buttonTWO = Button(  
    frameOne,  
    text = "2",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_2_is_Clicked  
) 
buttonTWO.pack(side = LEFT, expand = True, fill = "both") 
buttonTHREE = Button(  
    frameOne,  
    text = "3",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_3_is_Clicked  
)
buttonTHREE.pack(side = LEFT, expand = True, fill = "both") 
buttonC = Button(  
    frameOne,  
    text = "C",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_C_is_Clicked  
)  
buttonC.pack(side = LEFT, expand = True, fill = "both")  
buttonFOUR = Button(  
    frameTwo,  
    text = "4",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_4_is_Clicked  
)
buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
buttonFIVE = Button(  
    frameTwo,  
    text = "5",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_5_is_Clicked  
)  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  
  
  
buttonSIX = Button(  
    frameTwo,  
    text = "6",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_6_is_Clicked  
)  
 
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  

buttonADD = Button(  
    frameTwo,  
    text = "+",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Add_is_Clicked  
)  
 
buttonADD.pack(side = LEFT, expand = True, fill = "both")  

buttonSEVEN = Button(  
    frameThree,  
    text = "7",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_7_is_Clicked  
)  

buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")  
  

buttonEIGHT = Button(  
    frameThree,  
    text = "8",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_8_is_Clicked  
)  

buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
  
  
buttonNINE = Button(  
    frameThree,  
    text = "9",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_9_is_Clicked  
)  
 
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
  

buttonSUB = Button(  
    frameThree,  
    text = "-",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Sub_is_Clicked  
)  
 
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  
  

buttonZERO = Button(  
    frameFour,  
    text = "0",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_0_is_Clicked  
)  
 
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
  

buttonMUL = Button(  
    frameFour,  
    text = "*",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Mul_is_Clicked  
)  

buttonMUL.pack(side = LEFT, expand = True, fill = "both")  
  
  
buttonDIV = Button(  
    frameFour,  
    text = "/",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_Div_is_Clicked  
)  
 
buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  

buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = res  
)  

buttonEQUAL.pack(side = LEFT, expand = True, fill = "both")  
  

guiWindow.mainloop()  
 


