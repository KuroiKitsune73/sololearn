'''
You are in a college level English class,
your professor wants you to write an essay,
but you need to find out the average length of all the words you use.
It is up to you to figure out how long each word is and to average it out. 
 
Task:  
Takes in a string, figure out the average length of all
the words and return a number representing the average length.
Remove all punctuation. Round up to the nearest whole number. 
 
Input Format:  
A string containing multiple words. 
 
Output Format:  
A number representing the average length of each word,
rounded up to the nearest whole number. 
 
Sample Input:  
this phrase has multiple words 
 
Sample Output:  
6
'''

import string
input_string = input()

# Remove punctuation from the input string
translator = str.maketrans('', '', string.punctuation)
input_string = input_string.translate(translator)

# Split the input string into words
words = input_string.split()

# Calculate the length of each word and store them in a list
word_lengths = [len(word) for word in words]

# Calculate the average length of words, rounding up to the nearest whole number
average_length = -(-sum(word_lengths) // len(word_lengths))

print(average_length)