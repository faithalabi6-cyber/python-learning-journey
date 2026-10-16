# ==========================================
#              SUDOKU GAME
# ==========================================


# 1. Create a variable board with a list to represent the board

board = [
    [4, 0, 0, 3, 7, 0, 0, 0, 0],
    [6, 0, 8, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [1, 0, 8, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 9],
    [2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 1, 0, 0, 9],
]


# 2. Create a function that displays the board

def display_board():

    # Go through each row in the board
    for row in board:

        # Go through each number in the row
        for number in row:

            # Display the number in the same row
            print(number, end=" ")

        # Move to the next line after each row
        print()


# 3. Check whether the board is complete

def is_complete():

    # Check each row
    for row in board:

        # Check each number in the row
        for number in row:

            # If a zero exists, the board is incomplete
            if number == 0:
                return False

    # No zeros remain
    return True


# 4. Check whether a move is valid

def is_valid_move(row, column, number):

    # Check the row
    for value in board[row]:

        if value == number:
            print("Invalid move: Number already exists in this row")
            return False

    # Check the column
    for i in range(9):

        value = board[i][column]

        if value == number:
            print("Invalid move: Number already exists in this column")
            return False

    # Find the starting position of the 3x3 box
    box_row = (row // 3) * 3
    box_column = (column // 3) * 3

    # Check the 3x3 box
    for i in range(3):

        for j in range(3):

            value = board[box_row + i][box_column + j]

            if value == number:
                print("Invalid move: Number already exists in the box")
                return False

    # The move is valid if no duplicate is found
    return True


# 5. Start the game

print("========== SUDOKU GAME ==========")

display_board()


# 6. Ask the player to enter moves

while True:

    # Check whether the board is complete
    if is_complete():

        print("Congratulations! Sudoku complete!")
        break

    # Get the player's input
    try:

        row = int(input("Enter row (0-8): "))
        column = int(input("Enter column (0-8): "))
        number = int(input("Enter number (1-9): "))

    except ValueError:

        print("Invalid input. Please enter numbers only.")
        continue

    # 7. Check that the row is valid

    if row < 0 or row > 8:

        print("Invalid row. Enter a number from 0 to 8.")
        continue

    # 8. Check that the column is valid

    if column < 0 or column > 8:

        print("Invalid column. Enter a number from 0 to 8.")
        continue

    # 9. Check that the number is valid

    if number < 1 or number > 9:

        print("Invalid number. Enter a number from 1 to 9.")
        continue

    # 10. Check whether the cell is empty

    if board[row][column] != 0:

        print("The cell is occupied. Choose an empty cell.")
        continue

    # 11. Validate the move before placing the number

    if is_valid_move(row, column, number):

        # Place the number on the board
        board[row][column] = number

        print("Move accepted!")

        # Display the updated board
        display_board()

    else:

        # Reject the invalid move
        print("Please try another move.")
        continue