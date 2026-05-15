#!/usr/bin/python3
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """Lövhənin tam dolub-dolmadığını (heç-heçəni) yoxlayır"""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt):
    """İstifadəçidən yalnız 0, 1 və ya 2 rəqəmlərini qəbul edir"""
    while True:
        try:
            val = int(input(prompt))
            if val in [0, 1, 2]:
                return val
            print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Təhlükəsiz daxiletmə funksiyasını çağırırıq
        row = get_valid_input("Enter row (0, 1, or 2) for player " + player + ": ")
        col = get_valid_input("Enter column (0, 1, or 2) for player " + player + ": ")
        
        if board[row][col] == " ":
            board[row][col] = player
            
            # Gedişdən dərhal sonra uduş yoxlanılır
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
                
            # Heç-heçə yoxlanılır
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
                
            # Növbə yalnız uduş yoxlanıldıqdan sonra digər oyunçuya keçir
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
