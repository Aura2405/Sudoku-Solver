import sys
import copy
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt

# Check if a number is valid in the grid at a specific position
def is_possible(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

# Solve Sudoku using backtracking
def sudoku_solver(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_possible(grid, row, col, num):
                        grid[row][col] = num
                        if sudoku_solver(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Check if the initial grid is valid
def is_valid_grid(grid):
    for row in range(9):
        row_seen = set()
        col_seen = set()
        for col in range(9):
            # Check row
            if grid[row][col] in row_seen and grid[row][col] != 0:
                return False
            if grid[row][col] != 0:
                row_seen.add(grid[row][col])
            
            # Check column
            if grid[col][row] in col_seen and grid[col][row] != 0:
                return False
            if grid[col][row] != 0:
                col_seen.add(grid[col][row])
        
        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (row % 3)
        subgrid_seen = set()
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] in subgrid_seen and grid[i][j] != 0:
                    return False
                if grid[i][j] != 0:
                    subgrid_seen.add(grid[i][j])
    return True

# Main Application Class
class SudokuApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Sudoku Solver")
        self.layout = QGridLayout()
        self.cells = [[None for _ in range(9)] for _ in range(9)]

        # Create the grid with empty cells
        for row in range(9):
            for col in range(9):
                cell = QLineEdit()
                cell.setAlignment(Qt.AlignCenter)
                cell.setMaxLength(1)
                cell.setStyleSheet("background-color: white;")
                self.layout.addWidget(cell, row, col)
                self.cells[row][col] = cell

        # Solve button
        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.solve_sudoku)
        self.layout.addWidget(solve_button, 9, 4)

        # Reset button
        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset_grid)
        self.layout.addWidget(reset_button, 9, 5)

        self.setLayout(self.layout)

    # Get user input from the grid
    def get_input_grid(self):
        grid = [[0 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                text = self.cells[row][col].text()
                if text.isdigit():
                    grid[row][col] = int(text)
        return grid

    # Solve the Sudoku puzzle
    def solve_sudoku(self):
        user_grid = self.get_input_grid()
        
        # Check if the initial grid is valid
        if not is_valid_grid(user_grid):
            self.display_error("Invalid Sudoku: Repeated numbers in row, column, or subgrid!")
            return

        temp_grid = copy.deepcopy(user_grid)
        if sudoku_solver(temp_grid):
            for row in range(9):
                for col in range(9):
                    self.cells[row][col].setText(str(temp_grid[row][col]))
                    self.cells[row][col].setStyleSheet("background-color: lightgreen;")
        else:
            self.display_error("Sudoku cannot be solved!")

    # Display error message
    def display_error(self, message):
        error_box = QMessageBox(self)
        error_box.setIcon(QMessageBox.Warning)
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        error_box.setStandardButtons(QMessageBox.Ok)
        error_box.exec_()

    # Reset the grid to its initial empty state
    def reset_grid(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].clear()
                self.cells[row][col].setStyleSheet("background-color: white;")

# Main function
def main():
    app = QApplication(sys.argv)
    window = SudokuApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
