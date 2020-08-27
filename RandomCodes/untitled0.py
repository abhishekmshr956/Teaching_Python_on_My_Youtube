#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:31:59 2020

@author: amishra
"""
def is_even(i):
    """
    checks if a number is even

    Parameters
    ----------
    i : integer number 

    Returns
    -------
    returns True if number is even & returns false otherwise

    """
    
    if i%2 == 0:
        return True
    else:
        return False
    
    
def print_about_number(n):
    """
    prints number is even or not

    Parameters
    ----------
    n : integer number

    Returns
    -------
    None.

    """
    check_even = is_even(n)
    if check_even:
        print(f'{n} is even')
    else:
        print(f'{n} is not even')
        


def f(x):
    """
    returns square of a number

    Parameters
    ----------
    x : expects a number 

    Returns
    -------
    square of number
    x

    """
    x = x**2
    print(f'x inside function f is {x}')
    return x

x = 3
z = f(x)
print(f'x in the global environment is {x}')
print(f'z in the global environment is {z}')





def f_1(p):
    print("I am in function f_1")
    #x = x + 5
    p = x**3
    print(f'p inside f_1 is {p}')
    
    
z_1 = f_1(x)
print(f'z_1 in global environment is {z_1}')




def f(x):
    return x + 1

def g(x):
    return x**2

def h(x):
    return g(f(x))

def m(x):
    return f(g(x))


        

        
        
        

        
        
        
    
