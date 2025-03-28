# Import module 
from tkinter import *

# Create object 
root = Tk()
root.title('Tic-Tac-Toe') 
root.geometry("860x613") 

# Add image file 
bg = PhotoImage(file = "board.png")
x_img = PhotoImage(file='x_player.png')
o_img = PhotoImage(file='O_player.png')

# Show image using label 
label1 = Label( root, image=bg)
label1.place(x=0, y=0, relwidth=1, relheight=1)

board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

current_player = 'X'

buttons = [[None, None, None] for _ in range(3)]

def on_click(row, col):
    global current_player

    if board[row][col] is None:
        board[row][col] = current_player

        if current_player == "x":
            buttons[row][col].config(image=x_img)
        else:
            buttons[row][col].config(image=o_img)

        if check_winner():
            print(f'{current_player} WINS!')
            reset_board()
        else:
            current_player = 'O' if current_player == "X" else "X"

def check_winner():
    for row in board:
        if row in board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return True
    if board[0][0] == board[1][1] == board[1][1] == board[2][2] and board[0][0] is not None:
        return True
    if board[0][2] == board[1][1] == board [2][0] and board[0][2] is not None:
        return True
    return False

def reset_board():
    global current_player
    current_player = 'X'
    for r in range(3):
        for c in range(3):
            board[r][c] = None
            buttons[r][c].config(image='')

button_size = 10
x_offset = 130
y_offset = 41
spacing = 0


for r in range(3):
    for c in range(3):
        btn = Button(root, image="", width=button_size, height=button_size, borderwidth=0,
                     command=lambda row=r, col=c: on_click(row, col))
        btn.place(x=x_offset + c * button_size, y=y_offset + r * button_size)
        buttons[r][c] = btn

# Execute tkinter 
root.mainloop()
