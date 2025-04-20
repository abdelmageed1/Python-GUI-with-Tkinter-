# import Modules
from tkinter import *

# Create main window

root = Tk()



root.title("Simple Calculator app")
root.minsize(250,450)


entry = Entry(root ,width=35  )
entry.grid(row = 1, column=0 ,columnspan=3 ,padx=40 , pady= 20)


num1 = 0
num2 = 0
operator = ''

def btn_num(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,f'{current}{number}')


def btn_add( ):

     global num1 , operator
     num1 = getNumFromEntry()
     operator = '+'
    # entry.insert(0,f'{num} ')

def btn_sub():
    global num1, operator
    num1 = getNumFromEntry()
    operator = '-'
def btn_mul():
    global num1, operator
    num1 = getNumFromEntry()
    operator = '*'

def getNumFromEntry():
    num = int(entry.get())
    entry.delete(0, last=END)
    return num


def btn_equel():
    global  num2 ,operator
    num2 = getNumFromEntry()
    if operator =="+":
        entry.insert(0,f'{num1+num2}')
    elif operator =='-'    :
        entry.insert(0, f'{num1 - num2}')
    elif operator =='*'    :
        entry.insert(0, f'{num1 * num2}')

def btn_clear():
    entry.delete(0,END)
btn1 = Button(root , text="1", padx=40 , pady= 20 ,command= lambda : btn_num(1))
btn1.grid(row = 2, column=0)

btn2 = Button(root , text="2", padx=40 , pady= 20,command= lambda : btn_num(2))
btn2.grid(row = 2, column=1,  )

btn3 = Button(root , text="3", padx=40 , pady= 20,command= lambda : btn_num(3))
btn3.grid(row = 2, column=2)

btn4 = Button(root , text="4", padx=40 , pady= 20,command= lambda : btn_num(4))
btn4.grid(row = 3, column=0)

btn5 = Button(root , text="5", padx=40 , pady= 20,command= lambda : btn_num(5))
btn5.grid(row = 3, column=1)

btn6 = Button(root , text="6", padx=40 , pady= 20,command= lambda : btn_num(6))
btn6.grid(row = 3, column=2)


btn7 = Button(root , text="7", padx=40 , pady= 20,command= lambda : btn_num(7))
btn7.grid(row = 4, column=0)

btn8 = Button(root , text="8", padx=40 , pady= 20,command= lambda : btn_num(8))
btn8.grid(row = 4, column=1)

btn9 = Button(root , text="9", padx=40 , pady= 20,command= lambda : btn_num(9))
btn9.grid(row = 4, column=2)


btn_plus = Button(root , text="+", padx=40 , pady= 20 , command=btn_add)
btn_plus.grid(row = 5, column=0)

btn_minus = Button(root , text="-", padx=40 , pady= 20,command=btn_sub)
btn_minus.grid(row = 5, column=1)

btn_mul = Button(root , text="*", padx=40 , pady= 20 ,command=btn_mul)
btn_mul.grid(row = 5, column=2)


btn_equel = Button(root , text="="     ,padx=88 , pady= 20 ,command=btn_equel )
btn_equel.grid(row = 6, column=0 ,columnspan=2   )
# #
btn_clear = Button(root , text="Clear"    ,padx=30 , pady= 18 ,command=btn_clear )
btn_clear.grid(row = 6, column=2  )







root.mainloop()
