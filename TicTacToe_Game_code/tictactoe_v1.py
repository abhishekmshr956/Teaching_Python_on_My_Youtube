#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:22:28 2020

@author: amishra
"""
import numpy as np

def display_matrix(game):
    print('  ', 0, 1, 2)
    print()
    for i in range(len(game)):
        print(i, end = '  ')
        for j in range(len(game)):
            print(game[i][j], end = ' ')
        print()

def ask_input(player, game):
    if player % 2 == 0:
        player_number = 2
    else:
        player_number = 1
    while True:
        while True:
            try:
                row = int(input(f'Player {player_number} enter row number [0-2]: '))
            except ValueError:
                print("Oops !! Please choose row number among [0, 1, 2]")
            else:    
                if row in [0, 1, 2] :
                    break
                else:
                    print("\n Oops !! Please choose row number among [0, 1, 2]")
        while True:
            try:
                col = int(input(f'Player {player_number} enter col number [0-2]: '))
            except ValueError:
                print("Oops !! Please choose column number among [0, 1, 2]")
            else:    
                if col in [0, 1, 2]:
                    break
                else:
                    print("\n Oops !! Please choose column number among [0, 1, 2]")
        
        if is_valid_move(row, col, game):
            return(row, col)
        else:
            print("\nOops !! Not a valid move. The position is already filled")
            print("Please enter your move again")
        
    
    return (row, col)

def is_valid_move(row, col, game):
    valid = True
    if game[row][col] != 0:
        valid = False
        return valid
    return valid

def insert_move(row, col, player, game_matrix):
    """
    returns modified game map with new move inserted. inserts 1 if player is odd
    and inserts 2 if player is even

    Parameters
    ----------
    row : int row number
    col : int col number
    player : int odd for player 1, even for player 2
    game_matrix : current game_matrix

    Returns
    -------
    game_matrix : Updated game matrix

    """
    if player % 2 == 0:
        game_matrix[row][col] = 2
    else:
        game_matrix[row][col] = 1
    return game_matrix

def check_if_win(game):
    (row_win, col_win, diag_win) = (False, False, False)
    if (game[0][0] == game[1][1] == game[2][2] != 0) or (game[0][2] == game[1][1] == game[2][0] != 0):
        diag_win = True
        return (row_win, col_win, diag_win)
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != 0 :
            row_win = True
            return (row_win, col_win, diag_win)
        if game[0][i] == game[1][i] == game[2][i] != 0 :
            col_win = True
            return (row_win, col_win, diag_win)
    return (row_win, col_win, diag_win)

def check_if_draw(game):
    draw = False
    (row_win, col_win, diag_win) = check_if_win(game)
    if (not (row_win or col_win or diag_win)) and np.count_nonzero(game) == 9:
        draw = True
        return draw
    return draw
        
    

def tictactoe():
    #n_dim represents dimension of the tictactoe game
    #n_dim = 3
    
    #initialize game matrix to zeros
    game_matrix = np.zeros((3, 3), int)
    #display game matrix
    display_matrix(game_matrix)
    
    #player number 1 or 2
    player = 1
    check_win = False #checks if there is a winner
    check_draw = False #checks if game is draw
    
    want_to_play = True
    while want_to_play:
        while True:
            user_input = input("Enter n for a new game, enter e to exit game: ")
            if user_input.lower() == 'e':
                want_to_play = False
                break
            elif user_input.lower() == 'n':
                while not (check_win or check_draw):
                    #ask for row and column number for entry into matrix
                    (row, col) = ask_input(player, game_matrix)
                    
                    #update game_matrix
                    game_matrix = insert_move(row, col, player, game_matrix)
                    
                    display_matrix(game_matrix) #display game matrix
                    
                    #check if win 
                    (row_win, col_win, diag_win) = check_if_win(game_matrix)
                    if row_win or col_win or diag_win :
                        if player % 2 == 0:
                            print("\n Congratulations !!! Player 2 won")
                        else:
                            print("\n Congratulations !!! Player 1 won")
                        break
                    check_draw = check_if_draw(game_matrix)
                    if check_draw:
                        print("It's a draw")
                        break
                    
                    player +=1 #update player
            else:
                print("\nOops !! Not a valid input. ")
    

tictactoe()


