import tkinter as tk
from tkinter import messagebox
import time

class SudokuSolver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("600x700")
        self.configure(bg="#f8f9fa")
        self.grid_widgets = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()
        self.start_time = None
        
    def create_widgets(self):
        # Create Sudoku grid with enhanced styling
        frame = tk.Frame(self, bg="#f8f9fa")
        frame.pack(pady=20)
        
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(frame, width=3, font=('Arial', 18, 'bold'), justify='center', 
                                 bg=self.get_cell_color(row, col), fg="#495057", relief="solid", bd=1)
                entry.grid(row=row, column=col, padx=1, pady=1, ipady=5)
                entry.bind("<KeyRelease>", self.validate_input)
                self.grid_widgets[row][col] = entry
        
        # Create buttons with enhanced styling
        button_frame = tk.Frame(self, bg="#f8f9fa")
        button_frame.pack(pady=20)
        
        solve_button = tk.Button(button_frame, text="Solve", command=self.solve_sudoku, width=10, font=('Arial', 14), 
                                 bg="#17a2b8", fg="white", relief="raised", bd=2)
        solve_button.grid(row=0, column=0, padx=10)
        
        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_grid, width=10, font=('Arial', 14), 
                                 bg="#dc3545", fg="white", relief="raised", bd=2)
        clear_button.grid(row=0, column=1, padx=10)
        
        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_grid, width=10, font=('Arial', 14), 
                                 bg="#28a745", fg="white", relief="raised", bd=2)
        reset_button.grid(row=0, column=2, padx=10)
        
        # Create timer label with enhanced styling
        self.timer_label = tk.Label(self, text="Time: 0s", font=('Arial', 14), bg="#f8f9fa", fg="#343a40")
        self.timer_label.pack(pady=10)
        
    def get_cell_color(self, row, col):
        if (row // 3 + col // 3) % 2 == 0:
            return "#e9ecef"
        else:
            return "#ffffff"
        
    def validate_input(self, event):
        entry = event.widget
        value = entry.get()
        if value and (not value.isdigit() or not (1 <= int(value) <= 9)):
            entry.delete(0, tk.END)
            
    def get_grid(self):
        grid = []
        for row in range(9):
            grid_row = []
            for col in range(9):
                value = self.grid_widgets[row][col].get()
                grid_row.append(value if value else '.')
            grid.append(grid_row)
        return grid
    
    def set_grid(self, grid):
        for row in range(9):
            for col in range(9):
                self.grid_widgets[row][col].delete(0, tk.END)
                if grid[row][col] != '.':
                    self.grid_widgets[row][col].insert(0, grid[row][col])
    
    def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.grid_widgets[row][col].delete(0, tk.END)
    
    def reset_grid(self):
        # Example reset grid, you can replace it with any Sudoku puzzle
        reset_puzzle = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9']
        ]
        self.set_grid(reset_puzzle)
    
    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time: {elapsed_time}s")
        self.after(1000, self.update_timer)
    
    def solve_sudoku(self):
        self.start_time = time.time()
        self.update_timer()
        
        grid = self.get_grid()
        if solve_sudoku(grid):
            self.set_grid(grid)
            messagebox.showinfo("Sudoku Solver", "Sudoku Solved!")
        else:
            messagebox.showerror("Sudoku Solver", "No solution exists!")

# Sudoku solving logic
def is_safe(x, y, num, board):
    for i in range(9):
        if (board[x][i] != '.' and board[x][i] == num) or (board[i][y] != '.' and board[i][y] == num):
            return False
    
    r, c = (x // 3) * 3, (y // 3) * 3

    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if board[i][j] != '.' and board[i][j] == num:
                return False
    
    return True

def solver(x, y, board):
    if y == 9:
        if x != 8:
            return solver(x + 1, 0, board)
        return True

    if board[x][y] != '.':
        if solver(x, y + 1, board):
            return True
    else:
        for i in range(1, 10):
            if is_safe(x, y, str(i), board):
                board[x][y] = str(i)
                if solver(x, y + 1, board):
                    return True
                board[x][y] = '.'
    
    return False

def solve_sudoku(board):
    return solver(0, 0, board)

if __name__ == "__main__":
    app = SudokuSolver()
    app.mainloop()
