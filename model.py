#Collaboration with Cindy Nguyen
#Carlan Nguyen
from tkinter import *
from tkinter import font as tkFont
import math

expression = ""

def press(num):
    
    global expression, equation

    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    
    try:
        global expression
        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:
        equation.set(" error ")
        expression = ""

def clear():

    global expression, equation
    
    expression = ""
    equation.set("")

def square():

    global expression
    
    square_value = math.pow(int(expression), 2)
    equation.set(square_value)
    expression = ""

def squareroot():

    global expression
    sqrt_value = math.sqrt(int(expression))
    equation.set(sqrt_value)
    expression = ""

def fontIncrease():
    global font_size
    text_size = font_size.cget('size') + 2
    font_size.configure(size = text_size)

def fontDecrease():
    global font_size
    text_size = font_size.cget('size') - 2
    font_size.configure(size = text_size)
    

def main():
    global font_size, expression, equation
    gui = Tk()
    gui.configure(background="light gray")
    gui.title("Simple Calculator")
    gui.geometry("500x300")
    
    font_size = tkFont.Font(size=10)
    
    equation = StringVar()

    #Create the text entry box for showing the result
    expression_field = Entry(gui, border=5, font=35, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=100, ipady=15, sticky=NSEW)

    equation.set('0')
   
    #Create the buttons
    button1 = Button(gui, text='1', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(1), height=2, width=10)
    button1.grid(row=2, column=0, sticky=NSEW)
    
    button2 = Button(gui, text='2', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(2), height=2, width=10)
    button2.grid(row=2, column=1, sticky=NSEW)
    
            
    button3 = Button(gui, text='3', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(3), height=2, width=10)
    button3.grid(row=2, column=2, sticky=NSEW)
    

    button4 = Button(gui, text='4', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(4), height=2, width=10)
    button4.grid(row=3, column=0, sticky=NSEW)
    
    button5 = Button(gui, text='5', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(5), height=2, width=10)
    button5.grid(row=3, column=1, sticky=NSEW)

    button6 = Button(gui, text='6', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(6), height=2, width=10)
    button6.grid(row=3, column=2, sticky=NSEW)
    
    button7 = Button(gui, text='7', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(7), height=2, width=10)
    button7.grid(row=4, column=0, sticky=NSEW)

    button8 = Button(gui, text='8', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(8), height=2, width=10)
    button8.grid(row=4, column=1, sticky=NSEW)

    button9 = Button(gui, text='9', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(9), height=2, width=10)
    button9.grid(row=4, column=2, sticky=NSEW)

    button0 = Button(gui, text='0', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press(0), height=2, width=10)
    button0.grid(row=5, column=0, sticky=NSEW)

    plus = Button(gui, text=' + ', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press("+"), height=2, width=10)
    plus.grid(row=2, column=3, sticky=NSEW)

    minus = Button(gui, text=' - ', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press("-"), height=2, width=10)
    minus.grid(row=3, column=3, sticky=NSEW)

    multiply = Button(gui, text=' * ', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press("*"), height=2, width=10)
    multiply.grid(row=4, column=3, sticky=NSEW, )

    divide = Button(gui, text=' / ', font=font_size, fg='black', bg='#756bb1',
                     command=lambda: press("/"), height=2, width=10)
    divide.grid(row=5, column=3, sticky=NSEW)

    equal = Button(gui, text=' = ', font=font_size, fg='black', bg='#756bb1',
                     command=equalpress, height=2, width=10)
    equal.grid(row=5, column=2, sticky=NSEW)

    BtnClear = Button(gui, text='Clear ', font=font_size, fg='black', bg='#756bb1',
                     command=clear, height=2, width=10)
    BtnClear.grid(row=5, column=1, sticky=NSEW)

    BtnSquare = Button(gui, text='x^2', font=font_size, fg='black', bg='#756bb1',
                     command=square, height=2, width=10)
    BtnSquare.grid(row=6, column=0, sticky=NSEW)

    BtnSquare_root = Button(gui, text='sqrt', font=font_size, fg='black', bg='#756bb1',
                     command=squareroot, height=2, width=10)
    BtnSquare_root.grid(row=6, column=1, sticky=NSEW)

    BtnFont_increase = Button(gui, text='increase font', font=font_size, fg='black', bg='#756bb1',
                     command=fontIncrease, height=2, width=10)
    BtnFont_increase.grid(row=6, column=2, sticky=NSEW)

    BtnFont_decrease = Button(gui, text='decrease font', font=font_size, fg='black', bg='#756bb1',
                     command=fontDecrease, height=2, width=10)
    BtnFont_decrease.grid(row=6, column=3, sticky=NSEW)
    
    

    gui.rowconfigure(1, weight=1)
    gui.rowconfigure(2, weight=1)
    gui.rowconfigure(3, weight=1)
    gui.rowconfigure(4, weight=1)
    gui.rowconfigure(5, weight=1)
    gui.rowconfigure(6, weight=1)
    gui.columnconfigure(0, weight=1)
    gui.columnconfigure(1, weight=1)
    gui.columnconfigure(2, weight=1)
    gui.columnconfigure(3, weight=1)
    
        
    #start the GUI
    gui.mainloop()


if __name__ == "__main__":
    main()
    
