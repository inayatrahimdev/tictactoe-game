import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Initialize game variables
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False

        # Create game UI
        self.create_board_ui()

    def create_board_ui(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Create and place buttons for the board
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 30, 'bold'), width=8, height=3,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button
        
        # Display current player indicator
        self.player_label = tk.Label(self.root, text=f"Current Player: {self.current_player}", font=('Arial', 14))
        self.player_label.grid(row=3, column=0, columnspan=3, pady=10)

    def on_button_click(self, row, col):
        if not self.game_over and self.board[row][col] == ' ':
            # Update board state
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state='disabled', disabledforeground='black')
            
            # Check for winner
            winner = self.check_winner()
            if winner:
                self.game_over = True
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.highlight_winner(winner)
            elif self.is_board_full():
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a tie!")

            # Switch player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.player_label.config(text=f"Current Player: {self.current_player}")

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]  # Row win
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]  # Column win
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]  # Diagonal win
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]  # Diagonal win
        
        return None

    def is_board_full(self):
        # Check if the board is full (tie game)
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def highlight_winner(self, winner):
        # Highlight winning combination on the board
        for i in range(3):
            # Row highlight
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == winner:
                self.buttons[i][0].config(bg='green')
                self.buttons[i][1].config(bg='green')
                self.buttons[i][2].config(bg='green')
            # Column highlight
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == winner:
                self.buttons[0][i].config(bg='green')
                self.buttons[1][i].config(bg='green')
                self.buttons[2][i].config(bg='green')
        
        # Diagonal highlights
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == winner:
            self.buttons[0][0].config(bg='green')
            self.buttons[1][1].config(bg='green')
            self.buttons[2][2].config(bg='green')
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == winner:
            self.buttons[0][2].config(bg='green')
            self.buttons[1][1].config(bg='green')
            self.buttons[2][0].config(bg='green')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
