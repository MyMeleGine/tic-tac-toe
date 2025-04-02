import tkinter as tk

# Game board and player
board = [["", "", ""], ["", "", ""], ["", "", ""]]
current_player = ["X"]

def check_winner():
    """Checks if a player has won and displays a message."""
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],  # Row 1
        [(1, 0), (1, 1), (1, 2)],  # Row 2
        [(2, 0), (2, 1), (2, 2)],  # Row 3
        [(0, 0), (1, 0), (2, 0)],  # Column 1
        [(0, 1), (1, 1), (2, 1)],  # Column 2
        [(0, 2), (1, 2), (2, 2)],  # Column 3
        [(0, 0), (1, 1), (2, 2)],  # Diagonal \
        [(0, 2), (1, 1), (2, 0)]   # Diagonal /
    ]

    for combo in winning_combinations:
        if board[combo[0][0]][combo[0][1]] == current_player[0] and \
           board[combo[1][0]][combo[1][1]] == current_player[0] and \
           board[combo[2][0]][combo[2][1]] == current_player[0]:
            display_winner(f"Player {current_player[0]} Wins!")
            return True

    # Check for a draw
    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        display_winner("It's a Draw!")
        return True

    return False

def display_winner(message):
    color= 'red' if message == "It's a Draw!" else 'green'
    player_label.config(text=message, fg=color)
    for row in board_buttons:
        for button in row:
            button.config(state="disabled")

def switch_player():
    """Switches the player between X and O."""
    current_player[0] = "O" if current_player[0] == "X" else "X"
    player_label.config(text=f"It's {current_player[0]}'s turn.") 

def make_move(i, j):
    if board[i][j] == "":
        board[i][j] = current_player[0]
        board_buttons[i][j].config(text=current_player[0])
        if check_winner():
            return
        switch_player()

def show_active_player():
    global player_label
    player_label = tk.Label(root, text=f"It's {current_player[0]}'s turn.", font=("Cambria", 14, "bold"))
    player_label.grid(row=0, column=0, columnspan=3, pady=10)

def make_move_buttons():
    global board_buttons
    board_buttons = []

    button_size = 3 

    for i in range(3):
        row_buttons = []
        for j in range(3):
            move_button = tk.Button(root, text='', font=("Cambria", 16), width=6, height=3,  # Adjusted button size
                                    command=lambda r=i, c=j: make_move(r, c))
            move_button.grid(row=i+1, column=j, padx=0, pady=0, sticky="nsew")  # No padding to stick them together
            row_buttons.append(move_button)
        board_buttons.append(row_buttons)

    for i in range(3):
        root.grid_columnconfigure(i, weight=1, uniform="equal")
        root.grid_rowconfigure(i+1, weight=1, uniform="equal")

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x350")

# Initialize UI
show_active_player()
make_move_buttons()

root.mainloop()
