from tkinter import *
root=Tk()
root.configure(bg="#696969")
root.geometry("500x600")

# Defining a function to addition two numbers
def ad():

    # Setting the operation label to " + "
    z.set("           +")
    num1=x.get()
    num2=y.get()
    # Calculating the sum
    ans=num1+num2
    # Displaying the result in the result label
    l1.configure(text=ans)


# Defining a function to subraction two numbers
def sb():

    # Setting the operation label to " - "
    z.set("           –")
    num1=x.get()
    num2=y.get()
    # Calculating the difference
    ans=num1-num2
    # Displaying the result in the result label
    l1.configure(text=ans)


# Defining a function to multiply two numbers
def ml():

    # Setting the operation label to " x "
    z.set("           x")
    num1=x.get()
    num2=y.get()

    # Calculating the product
    ans=num1*num2
    # Displaying the result in the result label
    l1.configure(text=ans)


# Defining a function to divide two numbers
def dv():

    # Setting the operation label to " ÷ "
    z.set("           ÷")
    num1=x.get()
    num2=y.get()
    # Calculating the quotient
    ans=num1/num2
    # Displaying the result in the result label
    l1.configure(text=ans)


# Defining a function to modulus two numbers
def md():

    # Setting the operation label to " % "
    z.set("           %")
    num1=x.get()
    num2=y.get()
    # Calculating the modulus
    ans=num1//num2
    # Displaying the result in the result label
    l1.configure(text=ans)


# Defining a function to all clear
def acl():

    # Setting the values of the first and second numbers and the operation label to " 0 "
    x.set("0")
    x.set("0")
    y.set("0")
    z.set("0")
    # Clearing the result label
    l1.configure(text=" ")

# Creating labels for the first number, second number, and operation
Label(root,text="Enter First Number:",bg="white",font="lucida 10 bold").place(x=100,y=100,width=150,height=30)
Label(root,text="Enter Second Number:",bg="white",font="lucida 10 bold").place(x=100,y=150,width=150,height=30)
Label(root,text="Enter operation:",bg="white",font="lucida 10 bold").place(x=100,y=200,width=150,height=30)

# Creating variables to store the values of the first and second numbers and the operation
x=IntVar()
y=IntVar()
z=StringVar()
e1=Entry(root,textvariable=x,font="lucida 15 bold").place(x=280,y=100,width=150,height=30)
e2=Entry(root,textvariable=y,font="lucida 15 bold").place(x=280,y=150,width=150,height=30)
e3=Entry(root,textvariable=z,font="lucida 15 bold").place(x=280,y=200,width=150,height=30)

# Creating a label to display the result
l1=Label(root,text=" ",bg="white",font="lucida 15 bold")
l1.place(x=150,y=250,width=200,height=30)


# Creating buttons for addition, subtraction, multiplication, division, modulus, and clear all
a1=Button(root,text="+",font="lucida 30 bold",command=ad).place(x=100,y=300,width=80,height=80)
s1=Button(root,text="–",font="lucida 30 bold",command=sb).place(x=200,y=300,width=80,height=80)
m1=Button(root,text="x",font="lucida 30 bold",command=ml).place(x=100,y=400,width=80,height=80)
d1=Button(root,text="÷",font="lucida 30 bold",command=dv).place(x=200,y=400,width=80,height=80)
m2=Button(root,text="%",font="lucida 30 bold",command=md).place(x=300,y=300,width=80,height=80)
ac=Button(root,text="AC",font="lucida 30 bold",command=acl).place(x=300,y=400,width=80,height=80)


root.mainloop()