#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while not is_board_full(board):
        print_board(board)
        player = players[turn % 2]
        print(f"\nPlayer {player}, it's your turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                return
            turn += 1
        else:
            print("That spot is already taken. Try again.")

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()


# In[2]:


b = str(151)
for i in b:
    print(i)


# In[4]:


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while not is_board_full(board):
        print_board(board)
        player = players[turn % 2]
        print(f"\nPlayer {player}, it's your turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                return
            turn += 1
        else:
            print("That spot is already taken. Try again.")

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()


# In[ ]:




