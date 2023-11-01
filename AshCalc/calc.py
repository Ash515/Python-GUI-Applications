from tkinter import * #Importing Tkinter module

exp=""

def press(num):  # Function for Number pressing 
    global exp
    exp=exp+str(num)
    equation.set(exp)

def equalpress():      # Function for pressing Equal sign 
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp=""
    except:
        equation.set('error')      
        exp = " " 
def clear():     # Function for pressing clearing 
    global exp
    exp=""
    equation.set("")


#Creating Windows GUI

root=Tk()
root.geometry("400x400")
root.title("Calculator")
root.configure(bg="green")
heading=Label(root,text="AshCalc",font=('verdana',15,'bold'),bg="yellow",fg="indigo")
heading.place(x=150, y=10)
equation= StringVar()
txt = Entry(root,state='readonly',font=('times new roman',25, "bold"),textvariable=equation)
txt.grid(row=6, column=3, pady=50, padx=30, sticky="w")
txt_frame=Frame(txt,bd=10,bg="crimson")
txt_frame.place(x=2,y=2,width=450)

#Fixing Buttons
seven=Button(text="7",width=10,height=2,command = lambda : press(7))
seven.place(x=30,y=110)
eight=Button(text="8",width=10,height=2,command = lambda : press(8))
eight.place(x=120,y=110)
nine=Button(text="9",width=10,height=2,command = lambda : press(9))
nine.place(x=210,y=110)
CE=Button(text="CE",width=10,height=2,command=clear)
CE.place(x=295,y=110)
four=Button(text="4",width=10,height=2,command = lambda : press(4))
four.place(x=30,y=160)
five=Button(text="5",width=10,height=2,command = lambda : press(5))
five.place(x=120,y=160)
six=Button(text="6",width=10,height=2,command = lambda : press(6))
six.place(x=210,y=160)
zero=Button(text="0",width=10,height=2,command = lambda : press(0))
zero.place(x=295,y=160)
Add=Button(text="+",width=10,height=2,command = lambda : press('+'))
Add.place(x=295,y=210)
one=Button(text="1",width=10,height=2,command = lambda : press(1))
one.place(x=30,y=210)
two=Button(text="2",width=10,height=2,command = lambda : press(2))
two.place(x=120,y=210)
three=Button(text="3",width=10,height=2,command = lambda : press(3))
three.place(x=210,y=210)
div=Button(text="/",width=10,height=3,command = lambda : press('/'))
div.place(x=30,y=260)
multiply=Button(text="*",width=10,height=3,command = lambda : press('*'))
multiply.place(x=120,y=260)
sub=Button(text="-",width=10,height=3,command = lambda : press('-'))
sub.place(x=210,y=260)
equal=Button(text="=",width=10,height=3,command = equalpress)
equal.place(x=295,y=260)

root.mainloop()