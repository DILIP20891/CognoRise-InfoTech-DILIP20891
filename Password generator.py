import random
import string
from tkinter import *

root=Tk()
root.configure(bg="#87ceeb")
root.geometry("700x500")

def weak_password():

    # Get the length of the desired password from the user input
    lenn=length.get()
    print(lenn)
    # Define the set of characters to use in the password ( lowercase letters )
    characters = string.ascii_lowercase
    password = ''.join(random.choice(characters) for i in range(lenn))
    # Display the generated password in the Tkinter window
    l1.configure(text=password)


def strong_password():

    # Get the length of the desired password from the user input
    lenn=length.get()
    print(lenn)
    # Define the set of characters to use in the password ( letters , numbers and  special symbols )
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''. join(random. choice(characters) for i in range(lenn))

    # Display the generated password in the Tkinter window 
    l1.configure(text=password)

Label(root,text="PASSWORD GENERATOR",font="lucida 18 bold").place(x=200,y=20)
Label(root,text="Enter the length",font="lucida 15 bold",bg="#87ceeb").place(x=250,y=80)


length=IntVar()
# Add an Entry widget to the Tkinter window to allow the user to input the length
Entry(root,textvariable=length,font="lucida 10 bold").place(x=270,y=120,height=30,width=120)

# Add a Button widget to the Tkinter window to allow the user to generate a password
Button(root,text="Generate Weak Password",command=weak_password,fg="black",bg="#94C6E5",font="lucida 10 bold").place(x=150,y=160,height=40,width=185)
Button(root,text="Generate Strong Password",command=strong_password,fg="black",bg="#94C6E5",font="lucida 10 bold").place(x=350,y=160,height=40,width=185)

# Create a Label widget to display the generated password
l1=Label(root,text=" ",font="lucida 13 bold",bg="white")
l1.place(x=250,y=220,height=40,width=160)


root.mainloop()