from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Tic-Tac-Toe')


MainFrame=Frame(root,bd=10,width=180, height=75,relief=RIDGE)
MainFrame.grid(row=1,column=4)


InnerFrame=Frame(MainFrame,bd=10,width=180,height=75, padx=10,pady=2,relief=RIDGE)
InnerFrame.pack(side=RIGHT)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerXTitle=Label(InnerFrame,font=('Helvetica',15),text='Player X: ',padx=2,pady=2)
PlayerXTitle.grid(row=0,column=0)

txtPlayerX=Entry(InnerFrame,font=('Helvetica',15),bd=2,fg='black',textvariable=PlayerX,width=14,state=DISABLED,justify=LEFT)
txtPlayerX.grid(row=0,column=1)

PlayerOTitle=Label(InnerFrame,font=('Helvetica',15),text='Player O: ',padx=2,pady=2)
PlayerOTitle.grid(row=1,column=0)

txtPlayerO=Entry(InnerFrame,font=('Helvetica',15),bd=2,fg='black',textvariable=PlayerO,width=14,state=DISABLED,justify=LEFT)
txtPlayerO.grid(row=1,column=1)

#X starts so true
clicked = True
count = 0
# disable all the buttons
def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)
# Check to see if someone won
def checkifwon():
	global winner,score
	winner = False
	if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
		b1.config(bg="red")
		b2.config(bg="red")
		b3.config(bg="red")
		winner = True
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		n=float(PlayerX.get())
		scoreX=(n+1)
		PlayerX.set(scoreX)
		disable_all_buttons()
	elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
		b4.config(bg="red")
		b5.config(bg="red")
		b6.config(bg="red")
		winner = True
		n=float(PlayerX.get())
		scoreX=(n+1)
		PlayerX.set(scoreX)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()
	elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
		b7.config(bg="red")
		b8.config(bg="red")
		b9.config(bg="red")
		winner = True
		n=float(PlayerX.get())
		scoreX=(n+1)
		PlayerX.set(scoreX)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()
	elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
		b1.config(bg="red")
		b4.config(bg="red")
		b7.config(bg="red")
		winner = True
		n=float(PlayerX.get())
		scoreX=(n+1)
		PlayerX.set(scoreX)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()
	elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
		b2.config(bg="red")
		b5.config(bg="red")
		b8.config(bg="red")
		winner = True
		n=int(PlayerX.get())
		scoreX=(n+1)
		PlayerX.set(scoreX)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()
	elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
		b3.config(bg="red")
		b6.config(bg="red")
		b9.config(bg="red")
		winner = True
		n=float(PlayerX.get())
		scoreX=(n+1)
		PlayerX.set(scoreX)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()
	elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
		b1.config(bg="red")
		b5.config(bg="red")
		b9.config(bg="red")
		winner = True
		n=float(PlayerX.get())
		scoreX=(n+1)
		PlayerX.set(scoreX)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()
	elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
		b3.config(bg="red")
		b5.config(bg="red")
		b7.config(bg="red")
		winner = True
		n=float(PlayerX.get())
		scoreX=(n+1)
		PlayerX.set(scoreX)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
		disable_all_buttons()
	#### CHECK FOR O's Win
	elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
		b1.config(bg="red")
		b2.config(bg="red")
		b3.config(bg="red")
		winner = True
		n=float(PlayerO.get())
		scoreO=(n+1)
		PlayerO.set(scoreO)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()
	elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
		b4.config(bg="red")
		b5.config(bg="red")
		b6.config(bg="red")
		winner = True
		n=float(PlayerO.get())
		scoreO=(n+1)
		PlayerO.set(scoreO)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()
	elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
		b7.config(bg="red")
		b8.config(bg="red")
		b9.config(bg="red")
		winner = True
		n=float(PlayerO.get())
		scoreO=(n+1)
		PlayerO.set(scoreO)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()
	elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
		b1.config(bg="red")
		b4.config(bg="red")
		b7.config(bg="red")
		winner = True
		n=float(PlayerO.get())
		scoreO=(n+1)
		PlayerO.set(scoreO)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()
	elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
		b2.config(bg="red")
		b5.config(bg="red")
		b8.config(bg="red")
		winner = True
		n=float(PlayerO.get())
		scoreO=(n+1)
		PlayerO.set(scoreO)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()
	elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
		b3.config(bg="red")
		b6.config(bg="red")
		b9.config(bg="red")
		winner = True
		n=float(PlayerO.get())
		scoreO=(n+1)
		PlayerO.set(scoreO)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()
	elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
		b1.config(bg="red")
		b5.config(bg="red")
		b9.config(bg="red")
		winner = True
		n=float(PlayerO.get())
		scoreO=(n+1)
		PlayerO.set(scoreO)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()
	elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
		b3.config(bg="red")
		b5.config(bg="red")
		b7.config(bg="red")
		winner = True
		n=float(PlayerO.get())
		scoreO=(n+1)
		PlayerO.set(scoreO)
		messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
		disable_all_buttons()

	# Check if tie
	if count == 9 and winner == False:
		messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
		disable_all_buttons()

# Button clicked function
def b_click(b):
	global clicked, count
	if b["text"] == " " and clicked == True:
		b["text"] = "X"
		clicked = False
		count += 1
		checkifwon()
	elif b["text"] == " " and clicked == False:
		b["text"] = "O"
		clicked = True
		count += 1
		checkifwon()
	else:
		messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )



# Start the game over!
def reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global clicked, count,scoreX,scoreO
	clicked = True
	count = 0
	
	# Build our buttons
	b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
	b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
	b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
	b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
	b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
	b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
	b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
	b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
	b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
	# Grid our buttons to the screen
	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)
	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)
	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)
#NewGame
def NewGame():
        reset()
        PlayerX.set(0)
        PlayerO.set(0)


# Create menue
my_menu = Menu(root,bd=3)
root.config(menu=my_menu)
# Create Options Menu
options_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Rest Game", command=reset)
options_menu.add_command(label="New Game", command=NewGame)
reset()
NewGame()
root.mainloop()
