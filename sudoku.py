

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


# 2. Create a function that is able to display the board

def display_board():

    # We want to go through each row in the board
    for row in board:

        # After checking each row, loop through each number
        for number in row:

            # Print numbers in the same row
            print(number, end=" ")

        # The row is finished, move to the next line
        print()


# 3. Check if our board is complete or not

def is_complete():

    for row in board:

        for number in row:

            # If a zero still exists, the board is not complete
            if number == 0:
                return False

    return True


# 4. We want the player to enter a move

while True:

    # Get the row
    row = int(input("Enter row (0-8): "))

    # Get the column
    column = int(input("Enter column (0-8): "))

    # Get the number
    number = int(input("Enter number (1-9): "))


    # 5. Check that row and column are valid

    if row < 0 or row > 8:
        print("Invalid row. Enter a number from 0 to 8.")
        continue

    if column < 0 or column > 8:
        print("Invalid column. Enter a number from 0 to 8.")
        continue


    # Check that number is between 1 and 9

    if number < 1 or number > 9:
        print("Invalid number. Enter a number from 1 to 9.")
        continue


    # 6. Check if the cell is empty

    if board[row][column] == 0:

        print("The cell is empty")

    else:

        print("The cell is occupied")

        # Do not continue checking this move
        continue


    # 7. Set found to False because we are looking for
    # a number that would make the move invalid

    found = False


    # 8. Check the row

    # We want to check each value in the row
    for value in board[row]:

        # Check if the value is the same as our number
        if value == number:

            print("Invalid move: Number already exists in this row")

            found = True


    # 9. Check the column

    for i in range(9):

        value = board[i][column]

        if value == number:

            print("Invalid move: Number already exists in this column")

            found = True


    # 10. Find the starting position of the 3x3 box

    box_row = (row // 3) * 3
    box_column = (column // 3) * 3


    # 11. Check the 3x3 box

    # i represents the row inside the 3x3 box
    for i in range(3):

        # j represents the column inside the 3x3 box
        for j in range(3):

            # Give me the cell at the current row and column
            value = board[box_row + i][box_column + j]


            # Check if the value is equal to our number
            if value == number:

                print("Invalid move: Number already exists in the box")

                found = True


    # 12. ONLY place the number AFTER checking
    # the row, column and box

    if not found:

        board[row][column] = number

        print("Move accepted!")

        display_board()


    # 13. Check if the Sudoku is complete

    if is_complete():

        print("Congratulations! Sudoku complete!")

        break