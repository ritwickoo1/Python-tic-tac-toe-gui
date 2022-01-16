from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

ActivePlayer = 1
P1 = []
P2 = []
root = Tk()
style = ttk.Style()
style.theme_use("classic")
root.title("Tic Tac Toe Player 1")
bu1 = ttk.Button(root,text='')
bu1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
bu1.config(command=lambda: ButtonClick(1))
bu2 = ttk.Button(root, text='')
bu2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
bu2.config(command=lambda: ButtonClick(2))
bu3 = ttk.Button(root, text='')
bu3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
bu3.config(command=lambda: ButtonClick(3))
bu4 = ttk.Button(root, text='')
bu4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
bu4.config(command=lambda: ButtonClick(4))
bu5 = ttk.Button(root, text='')
bu5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
bu5.config(command=lambda: ButtonClick(5))
bu6 = ttk.Button(root, text='')
bu6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
bu6.config(command=lambda: ButtonClick(6))
bu7 = ttk.Button(root, text='')
bu7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
bu7.config(command=lambda: ButtonClick(7))
bu8 = ttk.Button(root, text='')
bu8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
bu8.config(command=lambda: ButtonClick(8))
bu9 = ttk.Button(root, text='')
bu9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
bu9.config(command=lambda: ButtonClick(9))

def ButtonClick(id):
    global ActivePlayer
    global P1
    global P2
    global root
    if(ActivePlayer == 1):
        setLayout(id,'X')
        root.title("Tic Tac Toe: Player 2")
        P1.append(id)
        ActivePlayer = 2
        AutoPlay()
    elif(ActivePlayer == 2):
        setLayout(id, 'O')
        root.title("Tic Tac Toe: Player 1")
        P2.append(id)
        ActivePlayer = 1
    checkWinner()

def setLayout(id,PlayerSymbol):
    if id == 1:
        bu1.config(text=PlayerSymbol)
        bu1.state(['disabled'])
    elif(id == 2):
        bu2.config(text=PlayerSymbol)
        bu2.state(['disabled'])
    elif (id == 3):
        bu3.config(text=PlayerSymbol)
        bu3.state(['disabled'])
    elif(id == 4):
            bu4.config(text=PlayerSymbol)
            bu4.state(['disabled'])
    elif(id == 5):
            bu5.config(text=PlayerSymbol)
            bu5.state(['disabled'])
    elif(id == 6):
            bu6.config(text=PlayerSymbol)
            bu6.state(['disabled'])
    elif(id == 7):
            bu7.config(text=PlayerSymbol)
            bu7.state(['disabled'])
    elif(id == 8):
            bu8.config(text=PlayerSymbol)
            bu8.state(['disabled'])
    elif(id == 9):
            bu9.config(text=PlayerSymbol)
            bu9.state(['disabled'])

def checkWinner():
    winner = -1
    if( (1 in P1) and (2 in P1) and (3 in P1)):
        winner = 1
    elif( (4 in P1) and (5 in P1) and (6 in P1)):
        winner = 1
    elif( (7 in P1) and (8 in P1) and (9 in P1)):
        winner = 1
    elif( (1 in P1) and (4 in P1) and (7 in P1)):
        winner = 1
    elif( (2 in P1) and (5 in P1) and (8 in P1)):
        winner = 1
    elif( (3 in P1) and (6 in P1) and (9 in P1)):
        winner = 1
    elif( (1 in P2) and (2 in P2) and (3 in P2)):
        winner = 2
    elif ((4 in P2) and (5 in P2) and (6 in P2)):
        winner = 2
    elif ((7 in P2) and (8 in P2) and (9 in P2)):
        winner = 2
    elif ((1 in P2) and (4 in P2) and (7 in P2)):
        winner = 2
    elif ((2 in P2) and (5 in P2) and (8 in P2)):
        winner = 2
    elif ((3 in P2) and (6 in P2) and (9 in P2)):
        winner = 2
    elif ((1 in P2) and (5 in P2) and (9 in P2)):
        winner = 2
    elif ((1 in P1) and (5 in P1) and (9 in P1)):
        winner = 1
    elif ((3 in P2) and (5 in P2) and (7 in P2)):
        winner = 2
    elif ((3 in P1) and (5 in P1) and (7 in P1)):
        winner = 1
    if winner == 1:
        messagebox.showinfo(title="Congrat.", message="Player 1 is the winner")
    elif winner == 2:
        messagebox.showinfo(title="Congrat.", message="Player 2 is the winner")

def AutoPlay():
    global P1
    global P2
    EmptyCells = []
    for cells in range(9):
        if(not((cells+1 in P1) or (cells+1 in P2))):
            EmptyCells.append(cells+1)
    RandIndex = randint(0, len(EmptyCells)-1)
    ButtonClick(EmptyCells[RandIndex])

root.mainloop()


