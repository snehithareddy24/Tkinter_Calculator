import tkinter as tk
'''Import tkinter module as tk is an alias for easy access'''
#button click handler
def press(v):
    entry.insert(tk.END,v)
    '''called when a number or operator button is clicked 
    Inserts the pressed value  at the end of Entry widget'''
#clear Function
def clear():
    entry.delete(0,tk.END)
    '''clears the calculator screen
    Deletes all characters from indexing 0 to end'''
def back():
    text=entry.get()
    if text:
        entry.delete(len(text)-1)
#calculation function
def calc():
    try:
        result=eval(entry.get())
        '''entry.get() retrives the expression e.g.(2+6)
        eval() evalutes the string as a Python expression'''
        entry.delete(0,tk.END)#clears the old expression
        entry.insert(0,result)#Displays exception instead of crashing
        
    except:
        entry.delete(0,tk.END)#clears the old expression
        entry.insert(0,"Invalid Expression")#Displays exception instead of crashing
        '''Handles invalid expression (e.g. 5++)'''
       
#main window creation
root=tk.Tk()#creates the main window
root.title("Calculator")#sets window title
root.configure(bg="#ffffff")#color the title
root.resizable(False,False)#disables resizing of window
#entry widget (Display Screen)
entry=tk.Entry(
    root,
    font=("Times new roman",20),
    bg="#ffe5d0",
    fg="#0f0f0f",
    bd=0,#border
    justify="right"
)
'''Text input field
acts as calculator display
Right-aligned for better calaculator look'''
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12)
buttons=[
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
   ]
'''represent calculator buttons
stored in list to reduce repetative code
'''
#dynamic Button Creation
r=1
c=0
'''rows and column counter for grid layout'''
for b in buttons:
    cmd = calc if b=="=" else lambda x=b:press(x)
    '''if button is "=" ,call calc()
else,call press() with button value
Lambda x=b prevents late binding'''
    tk.Button(
        root,
        text=b,
        command=cmd,#these three lines create a button widget
        font=("Calibri",14),
        width=5,
        height=2,
        bg="#e29e67" if b in "+-*/" else "#6bcd76",
        fg="#0f0f0f",
        bd=0,
        ).grid(row=r,column=c,padx=6,pady=6)
    c+=1
    if c==4:
        r+=1
        c=0
    '''moves to next row after 4 buttons'''
#clear Button
tk.Button(
    root,
    text="Clear",
    command=clear,
    font=("Calibri",14),
    width=5,
    height=2,
    bg="#ffe5d0",
    fg="#0f0f0f",
    bd=0

).grid(row=r,column=0,columnspan=4,pady=4)
'''clears the calculator display screen spans across all columns'''
tk.Button(
    root,
    text="back",
    command=back,
    font=("Calibri",14),
    width=5,
    height=2,
    bg="#ffe5d0",
    fg="#0f0f0f",
    bd=0

).grid(row=r,column=2,columnspan=4,pady=4)
root.mainloop()
'''keeps the window running
Listens for user interactions'''
