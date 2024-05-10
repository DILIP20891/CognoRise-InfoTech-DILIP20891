import random 
from tkinter import *

root=Tk()
root.configure(bg="#87ceeb")
root.geometry("800x600")
root.resizable(False, False)


def ply_agn():

    global u_s,c_s
    u_s=0
    c_s=0
    l1.configure(text=" ")
    l2.configure(text=" ")
    val1.set(u_s)
    val2.set(c_s)

def men(event):
    characters = ["Rock 🪨","Paper 📃","Scissor ✂️"]
    computer_choice =random.choice(characters)
    print('Computer choice:',computer_choice)
    
    l1.configure(text="🤖Computer choice:"+computer_choice)
    selected_option = lb1.get(lb1.curselection())

    global u_s,c_s # for convert the u_s=0 & c_s=0 the local to globol we can also use c_s & u_s inside the def function

    if selected_option=="Rock 🪨":
        if computer_choice == "Rock 🪨":
            print("Result:- Match Tie!!!")
            l2.configure(text="Result:- Match Tie!!!")
            
        elif computer_choice == "Paper 📃":
            print("Result:- You Lost!!")
            l2.configure(text="Result:- You Lost!!!")
            c_s=c_s+1
            val2.set(c_s)
        else:
            print("Result:- You Win!!!")
            l2.configure(text="Result:- You Win!!!")
            u_s=u_s+1
            val1.set(u_s)
    elif selected_option=="Paper 📃":
        if computer_choice == "Rock 🪨":
            print("Result:- You Win!!")
            l2.configure(text="Result:- You Win!!!")
            u_s=u_s+1
            val1.set(u_s)
        elif computer_choice == "Paper 📃":
            print("Result:- Match Tie!!!")
            l2.configure(text="Result:- Match Tie!!!")
        else:
            print('Result:- You Lost!!!')
            l2.configure(text="Result:- You Lost!!!")
            c_s=c_s+1
            val2.set(c_s)
    
    elif selected_option=="Scissor ✂️":
        if computer_choice == "Rock 🪨":
            print('Result:- You Lost!!!')
            l2.configure(text="Result:- You Lost!!!")
            c_s=c_s+1
            val2.set(c_s)
        elif computer_choice == "Paper 📃":
            print('Result:- You Win!!')
            l2.configure(text="Result:- You Win!!!")
            u_s=u_s+1
            val1.set(u_s)
        else:
            print('Result:- Match Tie!!!')
            l2.configure(text="Result:- Match Tie!!!")

Label(root,text="ROCK,PAPER & SCISSOR GAME ",font="lucida 18 bold").place(x=200,y=20)
Label(root,text="Select for start the game ",font="lucida 18 bold").place(x=250,y=70)
Label(root,text="Your Choice:",font="lucida 15 bold",bg="#87ceeb").place(x=340,y=130)


l1=Label(root,text=" ",font="lucida 15 bold",bg="#87ceeb")
l1.place(x=260,y=260)
l2=Label(root,text=" ",font="lucida 15 bold",bg="#87ceeb")
l2.place(x=300,y=300)

rps=("Rock 🪨","Paper 📃","Scissor ✂️") 
lb1=Listbox(root,height=3,width=20,selectmode=SINGLE,bg="#96c3eb",font="lucida 17 bold")
lb1.place(x=260,y=165)
for option in rps:
    lb1.insert(END,option)
lb1.bind('<<ListboxSelect>>',men)

Label(root,text="Scoreboard",font="lucida 18 bold").place(x=310,y=330)
Label(root,text="Your Score",font="lucida 10 bold").place(x=265,y=370,width=120)
Label(root,text="Computer Score",font="lucida 10 bold").place(x=374,y=370,width=120)

u_s=0
c_s=0
val1=IntVar()
val1.set(u_s)
l3=Label(root,textvariable=val1,font="lucida 13 bold",bg="black",fg="white")
l3.place(x=265,y=395,height=50,width=120)
val2=IntVar()
val2.set(c_s)
l4=Label(root,textvariable=val2,font="lucida 13 bold",bg="black",fg="white")
l4.place(x=374,y=395,height=50,width=120)

b1=Button(root,text="Play Again...",font="lucida 15 bold",bg="#96c3eb",command=ply_agn).place(x=310,y=470,height=50,width=150)

root.mainloop()