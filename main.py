import tkinter as tk

# Game board and player
board = [["", "", ""], ["", "", ""], ["", "", ""]]
current_player = ["X"]

def switch_player():
    """Switches the player between X and O."""
    current_player[0] = "O" if current_player[0] == "X" else "X"
    player_label.config(text=f"It's {current_player[0]}'s turn.") 

def make_move(i, j):
    """Handles button click, updates text, and switches players."""
    if board[i][j] == "":
        board[i][j] = current_player[0]
        board_buttons[i][j].config(text=current_player[0])
        switch_player()

def show_active_player():
    """Displays the current player's turn."""
    global player_label
    player_label = tk.Label(root, text=f"It's {current_player[0]}'s turn.", font=("Cambria", 14, "bold"))
    player_label.grid(row=0, column=0, columnspan=3, pady=10)

def make_move_buttons():
    """Creates a 3x3 button grid for the Tic-Tac-Toe board."""
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
root.geometry("350x350")  # Adjusted window size

# Initialize UI
show_active_player()
make_move_buttons()

root.mainloop()
