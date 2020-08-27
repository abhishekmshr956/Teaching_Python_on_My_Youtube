#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:22:28 2020

@author: amishra
"""
import numpy as np

def display_matrix(game):
    print()
    print('  ', end = ' ')
    for i in range(len(game)):
        print(i, end = ' ')
    print("\n")
    for i in range(len(game)):
        print(i, end = '  ')
        for j in range(len(game)):
            print(game[i][j], end = ' ')
        print()

def ask_input(player, game):
    length = len(game)
    if player % 2 == 0:
        player_number = 2
    else:
        player_number = 1
    while True:
        while True:
            try:
                row = int(input(f'Player {player_number} enter row number [0-{length-1}]: '))
            except ValueError:
                print("\nOops !! Please choose valid row number")
            else:    
                if row in range(length) :
                    break
                else:
                    print("\nOops !! Please choose valid row number")
        while True:
            try:
                col = int(input(f'Player {player_number} enter col number [0-{length-1}]: '))
            except ValueError:
                print("\nOops !! Please choose valid column number")
            else:    
                if col in range(length):
                    break
                else:
                    print("\nOops !! Please choose valid column number")
        
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

def check_all_equal(l):
    """
    Checks if all elements in given list are equal and non-zero

    Parameters
    ----------
    l : list of integers

    Returns
    -------
    true if all elements are equal and non-zero
    false otherwise

    """
    if len(l) != 0 and (l.count(l[0]) == len(l)) and l[0] != 0:
        return True
    return False

def check_if_win(game):
    length = len(game)
    (row_win, col_win, diag_win) = (False, False, False)
    (diag_1, diag_2) = ([], [])
    [diag_1.append(game[i][i]) for i in range(length)]
    [diag_2.append(game[i][length-1-i]) for i in range(length)]
    if check_all_equal(diag_1) or check_all_equal(diag_2):
        diag_win = True
        return (row_win, col_win, diag_win)
    
    for i in range(length):
        row = []
        [row.append(game[i][j]) for j in range(length)]
        if check_all_equal(row):
            row_win = True
            return (row_win, col_win, diag_win)
        col = []
        [col.append(game[j][i]) for j in range(length)]
        if check_all_equal(col):
            col_win = True
            return (row_win, col_win, diag_win)
        
    return (row_win, col_win, diag_win)
            
            

def check_if_draw(game):
    draw = False
    length = len(game)
    (row_win, col_win, diag_win) = check_if_win(game)
    if (not (row_win or col_win or diag_win)) and np.count_nonzero(game) == (length*length):
        draw = True
        return draw
    return draw
        
    

def tictactoe():
    #n_dim represents dimension of the tictactoe game
    n_dim = 3
    
    #initialize game matrix to zeros
    game_matrix = np.zeros((n_dim, n_dim), int)
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
                game_matrix = np.zeros((n_dim, n_dim), int)
                display_matrix(game_matrix)
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
                            print("-----\nCongratulations !!! Player 2 won\n-----")
                        else:
                            print("-----\nCongratulations !!! Player 1 won\n-----")
                        break
                    check_draw = check_if_draw(game_matrix)
                    if check_draw:
                        print("------\nIt's a draw\n-----")
                        break
                    
                    player +=1 #update player
            else:
                print("\nOops !! Not a valid input. ")
    

tictactoe()


