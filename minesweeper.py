import random
# 2D list that will act as the board. (Board user cannot see.)
# (Solution)
board = [[0, 0, 0, 0, 0],  # 0 = no mine
         [0, 0, 0, 0, 0],  # 1 = mine
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

# Board user can see.
board_display = [[-1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1],
                 [-1, -1, -1, -1, -1]]


# Function display number of mines around user's guess.
def check_mines_around(row, col):
    total_mines = 0  # total mines around spot.
    i = row - 1
    while i <= row + 1:
        if i >= 0 and i < 5:
            j = col - 1
            while j <= col + 1:
                if j >= 0 and j < 5:
                    total_mines = total_mines + board[i][j]
                j = j + 1
        i = i + 1
    return total_mines


# Add mines
num_mines = int(input("How many mines do you want?: "))
if num_mines > 25:
    print("Too many mines. Default = 5")
    num_mines = 5

num = 0  # num mines.
while num < num_mines:
    row = random.randint(0, 4)
    col = random.randint(0, 4)
    if board[row][col] == 0:
        board[row][col] = 1  # Add mine.
        num = num + 1


# Function to display solution.
def display_solution():
    for row in range(0, 5):
        for col in range(0, 5):
            print(board[row][col], end=" ")
        print("")


# Function yo display board.
def display_board():
    for row in range(0, 5):
        for col in range(0, 5):
            if board_display[row][col] == -1:
                print("-", end=" ")
            else:
                print(board_display[row][col], end=" ")
        print("")


display_board()

# User guessing.
guess = 0
while guess < (25 - num_mines):
    row = int(input("Guess a row(1-5): ")) - 1
    col = int(input("Guess a collum(1-5): ")) - 1
    if board[row][col] == 1:
        print("Boom! You hit a mine.")
        display_solution()
    else:
        board_display[row][col] = check_mines_around(row, col)
        display_board()
