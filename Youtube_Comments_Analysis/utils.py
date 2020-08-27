# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:11:10 2020

@author: Abhishek
"""

def word_generator(file):
    """
    converts lyrics text file to list of words in it

    Parameters
    ----------
    file : .txt filename

    Returns
    -------
    word_list : list of words in the given text file

    """
    with open(file, 'r') as f:
        word_list=[word.lower() for line in f for word in line.split()]
        return word_list
    
def word_frequency_generator(words):
    """
    returns words frequency dictionary

    Parameters
    ----------
    words : list of all words

    Returns
    -------
    words_dict : dictionary {'word':count}

    """
    words_dict = {}
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return words_dict

def word_used_giventimes(words_frequency, times):
    """
    returns list of words with count as given number of times

    Parameters
    ----------
    words_frequency : dictionary {'word':count}
    times : int required number of times the word has occred

    Returns
    -------
    tuple (words list, times)

    """
    words = []
    for word in words_frequency:
        if words_frequency[word] == times:
            words.append(word)
    return(words, times)

def most_used_word(words_frequency):
    """
    returns word list containing words with highest count

    Parameters
    ----------
    words_frequency : dictionary {'word':count}

    Returns
    -------
    returns tuple (word list, highest count)

    """
    highest = max(words_frequency.values())
    words = []
    for word in words_frequency:
        if words_frequency[word] == highest:
            words.append(word)
    return(words, highest)

def min_repeat_words(words_frequency, mintimes):
    """
    returns word list with count atleast mintimes

    Parameters
    ----------
    words_frequency : dictionary {'word':count}
    mintimes : int words need to have count >= least mintimes

    Returns
    -------
    result : a list with tuples [(['words'], count)]

    """
    result = []
    done = False
    while not done:
        temp = most_used_word(words_frequency)
        if temp[1] >= mintimes:
            result.append(temp)
            for w in temp[0]:
                del words_frequency[w] #removed from original dictionary
        else:
            done = True
    return result

def words_in_sorted_order(words_frequency):
    for w in sorted(words_frequency, key=words_frequency.get, reverse=True):
        print(w, words_frequency[w])

#words = word_generator('DilSeReLyrics.txt')                


# with open('DilSeReLyrics.txt','r') as f:
#     for line in f:
#         print(line)

# with open('DilSeReLyrics.txt','r') as f:
#     for line in f:
#         for word in line.split():
#             print(word)