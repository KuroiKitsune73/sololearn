'''
You are in a college level English class, your professor wants you to write an essay, but you need to find out the average length of all the words you use. It is up to you to figure out how long each word is and to average it out. 
 
Task:  
Takes in a string, figure out the average length of all the words and return a number representing the average length. Remove all punctuation. Round up to the nearest whole number. 
 
Input Format:  
A string containing multiple words. 
 
Output Format:  
A number representing the average length of each word, rounded up to the nearest whole number. 
 
Sample Input:  
this phrase has multiple words 
 
Sample Output:  
6
'''

alphabet="abcdefghijklmnopqrstuvwxyz"
msg=input().lower()
out=""
for i in msg:
    if i in alphabet:
        pos=alphabet.find(i)
        new=len(alphabet)-pos-1
        out+=alphabet[new]
    else:
        out+=i
print(out)