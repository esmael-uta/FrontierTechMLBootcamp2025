import random

def create_board(rows, cols):
    return [['*' for _ in range(cols)] for _ in range(rows)]

def display_board(board, hide_secrets=True):
    # Display board, optionally hiding treasure and trap
    print("\n  ", end=" ")
    for col in range(len(board[0])):
        print(col, end=" ")
    print()
    
    for i, row in enumerate(board):
        print(i, end=" ")
        for cell in row:
            if hide_secrets and cell in ['T', 'X']:
                print('*', end=" ")  # Hide T and X during game
            else:
                print(cell, end=" ")
        print()

def get_valid_input(prompt, max_value):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value < max_value:
                return value
            print(f"Please enter a number between 0 and {max_value - 1}")
        except ValueError:
            print("Please enter a valid number")

def place_treasure_and_trap(board):
    rows, cols = len(board), len(board[0])
    
    # Place treasure
    print("\nWhere would you like to hide the treasure?")
    treasure_row = get_valid_input("Enter row: ", rows)
    treasure_col = get_valid_input("Enter column: ", cols)
    board[treasure_row][treasure_col] = 'T'
    
    # Place trap
    while True:
        trap_row = random.randint(0, rows - 1)
        trap_col = random.randint(0, cols - 1)
        if board[trap_row][trap_col] == '*':
            board[trap_row][trap_col] = 'X'
            break

def play_game():
    print("Welcome to Treasure Hunt!")
    print("Find the treasure (T). Avoid the trap (X). Enter -1 to quit.")
    
    # Get board size
    rows = get_valid_input("Enter number of rows: ", 100)
    cols = get_valid_input("Enter number of columns: ", 100)
    
    # Create and set up board
    board = create_board(rows, cols)
    place_treasure_and_trap(board)
    
    # Show initial board with treasure location (for setup)
    print("\nHere's where everything is placed (this will be hidden during play):")
    display_board(board, hide_secrets=False)
    
    # Game loop
    attempts = 0
    while True:
        print("\nGame Board:")
        display_board(board, hide_secrets=True)
        
        # Get player's guess
        guess_row = input("\nGuess row (-1 to quit): ")
        if guess_row == '-1':
            print("Thanks for playing! The treasure was at", 
                  f"({treasure_row}, {treasure_col})")
            break
            
        guess_col = input("Guess column (-1 to quit): ")
        if guess_col == '-1':
            print("Thanks for playing! The treasure was at", 
                  f"({treasure_row}, {treasure_col})")
            break
            
        try:
            guess_row = int(guess_row)
            guess_col = int(guess_col)
            
            if not (0 <= guess_row < rows and 0 <= guess_col < cols):
                print("Invalid coordinates! Try again.")
                continue
                
            attempts += 1
            
            # Check result
            cell = board[guess_row][guess_col]
            if cell == 'T':
                print(f"\nCongratulations! You found the treasure in {attempts} attempts!")
                display_board(board, hide_secrets=False)
                break
            elif cell == 'X':
                print(f"\nGame Over! You hit a trap after {attempts} attempts!")
                display_board(board, hide_secrets=False)
                break
            else:
                print("Nothing here. Keep searching!")
                
        except ValueError:
            print("Please enter valid numbers!")

# Start the game
play_game()