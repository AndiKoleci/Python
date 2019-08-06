from tkinter import *
from time import sleep

score = 0

#Confirmation screens

def correctscreen():
    global score
    score = score+1

    correctframe = Frame(root, height=1920, width=1080)
    correctframe.grid(row=0, column=0)

    correcttext = Label(correctframe, text="CORRECT", fg="green")
    correcttext.config(font=("Arial", 60))
    correcttext.grid(padx=600, pady=300)

    root.update()
    sleep(1)
    correctframe.destroy()
    if score == 1:
        Q2()
    elif score==2:
        Q3()
    elif score==3:
        winscreen()

def wrongscreen():
    global score
    score = 0

    def retry():
        wrongframe.destroy()
        Q1()

    wrongframe = Frame(root, height=1920, width=1080)
    wrongframe.grid(row=0, column=0)

    wrongtext = Label(wrongframe, text="WRONG", fg="red")
    wrongtext.config(font = ("Arial", 60))
    wrongtext.grid(row=0, padx=650, pady=300)

    root.update()
    sleep(1)

    tryagain=Button(wrongframe, text="Try again", command=retry)
    tryagain.config(font=("Arial", 20), height=2, width=10)
    tryagain.grid(row=1)

def winscreen():
    win=Frame(root, height=1920, width=1080)
    win.grid(row=0, column=0)
    wintext=Label(win, text="You WON!", fg="yellow")
    wintext.config(font=("Arial", 60))
    wintext.grid(padx=600, pady=300)

    root.update()
    sleep(1)

    exitb = Button(win, text="Exit", command=root.destroy)
    exitb.config(font=("Arial", 20), height=2, width=10)
    exitb.grid(row=2)

#The 3 question screens

def Q1():
    welcome.destroy()
    play.destroy()

    q1frame = Frame(root, height=1920, width=1080)
    qlabel = Label(q1frame, text="First question:")
    question1 = Label(q1frame, text="2+2=?")
    ans1=Label(q1frame, text="A. 2")
    ans2=Label(q1frame, text="B. 3")
    ans3=Label(q1frame, text="C. 4")
    option1 = Button(q1frame, text="A", command=wrongscreen)
    option2 = Button(q1frame, text="B", command=wrongscreen)
    option3 = Button(q1frame, text="C", command=correctscreen)

    qlabel.config(font=("Arial", 44))
    question1.config(font=("Arial", 44))
    ans1.config(font=("Arial", 30))
    ans2.config(font=("Arial", 30))
    ans3.config(font=("Arial", 30))
    option1.config(font = ("Arial", 20), height=2, width=6)
    option2.config(font=("Arial", 20), height=2, width=6)
    option3.config(font=("Arial", 20), height=2, width=6)

    q1frame.grid(row=0, column=0)
    qlabel.grid(columnspan=3, row=1, column=0, padx=(500, 0), pady=(100, 0))
    question1.grid(row=2, padx=(500, 0), pady=(50, 0))
    ans1.grid(row=3, column=0, pady=(50, 0))
    ans2.grid(row=4, column=0)
    ans3.grid(row=5, column=0)
    option1.grid(row=6, column = 0, pady=(50, 0), padx=(100, 0))
    option2.grid(row=6, column = 0, pady=(50, 0), padx=(500, 0))
    option3.grid(row=6, column = 0, pady=(50, 0), padx=(900, 0))

def Q2():
    q2frame = Frame(root, height=1920, width=1080)
    qlabel = Label(q2frame, text="Second question:")
    question1 = Label(q2frame, text="3*3=?")
    ans1 = Label(q2frame, text="A. 3")
    ans2 = Label(q2frame, text="B. 6")
    ans3 = Label(q2frame, text="C. 9")
    option1 = Button(q2frame, text="A", command=wrongscreen)
    option2 = Button(q2frame, text="B", command=wrongscreen)
    option3 = Button(q2frame, text="C", command=correctscreen)

    qlabel.config(font=("Arial", 44))
    question1.config(font=("Arial", 44))
    ans1.config(font=("Arial", 30))
    ans2.config(font=("Arial", 30))
    ans3.config(font=("Arial", 30))
    option1.config(font=("Arial", 20), height=2, width=6)
    option2.config(font=("Arial", 20), height=2, width=6)
    option3.config(font=("Arial", 20), height=2, width=6)

    q2frame.grid(row=0, column=0)
    qlabel.grid(columnspan=3, row=1, column=0, padx=(500, 0), pady=(100, 0))
    question1.grid(row=2, padx=(500, 0), pady=(50, 0))
    ans1.grid(row=3, column=0, pady=(50, 0))
    ans2.grid(row=4, column=0)
    ans3.grid(row=5, column=0)
    option1.grid(row=6, column=0, pady=(50, 0), padx=(100, 0))
    option2.grid(row=6, column=0, pady=(50, 0), padx=(500, 0))
    option3.grid(row=6, column=0, pady=(50, 0), padx=(900, 0))

def Q3():
    q3frame = Frame(root, height=1920, width=1080)
    qlabel = Label(q3frame, text="Third question:")
    question1 = Label(q3frame, text="Who do I love?")
    ans1 = Label(q3frame, text="A. Ande")
    ans2 = Label(q3frame, text="B. Ande")
    ans3 = Label(q3frame, text="C. Ande")
    option1 = Button(q3frame, text="A", command=wrongscreen)
    option2 = Button(q3frame, text="B", command=correctscreen)
    option3 = Button(q3frame, text="C", command=wrongscreen)

    qlabel.config(font=("Arial", 44))
    question1.config(font=("Arial", 44))
    ans1.config(font=("Arial", 30))
    ans2.config(font=("Arial", 30))
    ans3.config(font=("Arial", 30))
    option1.config(font=("Arial", 20), height=2, width=6)
    option2.config(font=("Arial", 20), height=2, width=6)
    option3.config(font=("Arial", 20), height=2, width=6)

    q3frame.grid(row=0, column=0)
    qlabel.grid(columnspan=3, row=1, column=0, padx=(500, 100), pady=(100, 0))
    question1.grid(row=2, padx=(500, 0), pady=(50, 0))
    ans1.grid(row=3, column=0, pady=(50, 0))
    ans2.grid(row=4, column=0)
    ans3.grid(row=5, column=0)
    option1.grid(row=6, column=0, pady=(50, 0), padx=(100, 0))
    option2.grid(row=6, column=0, pady=(50, 0), padx=(500, 0))
    option3.grid(row=6, column=0, pady=(50, 0), padx=(900, 0))

#First screen + root

root = Tk()
root.geometry("1920x1080")
root.title("3 Questions")

welcome = Label(root, text="Welcome to 3 Questions!")
welcome.config(font = ("Arial", 44))
welcome.pack(pady=200)

play = Button(root, text = "PLAY!", command = Q1)
play.config(font = ("Arial", 44))
play.place(x=650, y=450)

root.mainloop()