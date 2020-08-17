# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:30:09 2020

@author: Abhishek
"""
import utils

#words = utils.word_generator('Dil_Se_Re.txt')
words = utils.word_generator('Ye_Dil.txt')
#words = utils.word_generator('my_test_words.txt')
#print(words)

words_frequency = utils.word_frequency_generator(words)
#print(words_frequency)

most_used = utils.most_used_word(words_frequency)
#print(most_used)

word_used_onetime = utils.word_used_giventimes(words_frequency, 2)
#print(word_used_onetime)

utils.words_in_sorted_order(words_frequency)

# word_used_mintimes = utils.min_repeat_words(words_frequency, 10) 
# print(word_used_mintimes)




            
        
    
        
    