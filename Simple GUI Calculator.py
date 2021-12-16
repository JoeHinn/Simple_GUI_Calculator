from tkinter import *
from tkinter.constants import CENTER, END
calnumbers = StringVar
tempnum = ""
ui = Tk()
ui.geometry("262x300")
ui.title("Calculator")
entrynumber = Entry(ui,textvariable= calnumbers,background="#0e153a",fg="#e2f3f5",width=43)
entrynumber.place(x=0,y=0,height=40)
entrynumber.pack()
def press(value):
    """global tempnum
    tempnum = tempnum + str(value)
    entrynumber."""
    global tempnum
    tempnum = tempnum +str(value)
    entrynumber.insert(END, value)

def cal():
    """global tempnum
    addval = str(eval(tempnum))
    clear()
    tempnum = ""
    press(addval)"""
    global tempnum
    try:
        
        addval = str(eval(tempnum))
        clear()
        tempnum = ""
        press(addval)
    except:
        addval = "Error try some other expressions"
        tempnum = ""  
        

  
def clear():
    entrynumber.delete(0,END)
#Row 1
b1 = Button(ui,text="7",command=lambda: press("7"),padx=25,pady=20,background="#22d1ee").place(x=0,y=41)
b2 = Button(ui,text="8",command=lambda: press("8"),padx=25,pady=20,background="#22d1ee").place(x=65,y=41)
b3 = Button(ui,text="9",command=lambda: press("9"),padx=25,pady=20,background="#22d1ee").place(x=130,y=41)
b4 = Button(ui,text="+",command=lambda: press("+"),padx=25,pady=20,background="#22d1ee").place(x=195,y=41)   

#Row 2
b5 = Button(ui,text="4",command=lambda: press("4"),padx=25,pady=20,background="#22d1ee").place(x=0,y=105)
b6 = Button(ui,text="5",command=lambda: press("5"),padx=25,pady=20,background="#22d1ee").place(x=65,y=105)
b7 = Button(ui,text="6",command=lambda: press("6"),padx=25,pady=20,background="#22d1ee").place(x=130,y=105)
b8 = Button(ui,text="-",command=lambda: press("-"),padx=27,pady=20,background="#22d1ee").place(x=195,y=105)   

#Row 3
b9 = Button(ui,text="1",command=lambda: press("1"),padx=25,pady=20,background="#22d1ee").place(x=0,y=169)
b10 = Button(ui,text="2",command=lambda: press("2"),padx=25,pady=20,background="#22d1ee").place(x=65,y=169)
b11 = Button(ui,text="3",command=lambda: press("3"),padx=25,pady=20,background="#22d1ee").place(x=130,y=169)
b12 = Button(ui,text="x",command=lambda: press("*"),padx=26,pady=20,background="#22d1ee").place(x=195,y=169) 

#Row 4
b13 = Button(ui,command=clear,text="C",padx=24,pady=20,background="#22d1ee").place(x=0,y=233)
b14 = Button(ui,text="0",command=lambda: press("0"),padx=25,pady=20,background="#22d1ee").place(x=65,y=233)
b15 = Button(ui,text="/",command=lambda: press("/"),padx=25,pady=20,background="#22d1ee").place(x=130,y=233)
b16 = Button(ui,text="=",command=cal,padx=25,pady=20,background="#22d1ee").place(x=195,y=233)

ui.mainloop()