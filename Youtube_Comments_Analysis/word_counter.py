# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:30:09 2020

@author: Abhishek
"""
import utils

#words = utils.word_generator('Dil_Se_Re.txt')
words = utils.word_generator('youtube_comments.txt')
#words = utils.word_generator('my_test_words.txt')
#print(words)

words_frequency = utils.word_frequency_generator(words)
#print(words_frequency)

most_used = utils.most_used_word(words_frequency)
#print(most_used)

word_used_onetime = utils.word_used_giventimes(words_frequency, 2)
#print(word_used_onetime)

words_frequency_modified = words_frequency.copy()
keys_to_remove = utils.word_generator('words_to_remove.txt')
important_keys = utils.word_generator('important_words.txt')
important_words_frequency = {}
#keys_to_remove = ['are','the','and','to','is','will','a','in','my','I','for','it\'s','by','want','we','have',
 #                 ]
for key in keys_to_remove:
    try: 
        del words_frequency_modified[key]
    except KeyError:
        continue
    
for key in important_keys:
    try:
        important_words_frequency[key] = words_frequency[key]
    except KeyError:
        continue
#words_frequency_modified = words_frequency_modified.remove

#utils.words_in_sorted_order(words_frequency)
#print()
utils.words_in_sorted_order(words_frequency_modified)
print("\n------------------")
print("Important words")
print()
utils.words_in_sorted_order(important_words_frequency)

# word_used_mintimes = utils.min_repeat_words(words_frequency, 10) 
# print(word_used_mintimes)




            
        
    
        
    