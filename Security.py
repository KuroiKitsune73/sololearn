'''
You are in charge of security at a casino,
and there is a thief who is trying to steal the casino's money!
Look over the security diagrams to make sure that you always
have a guard between the thief and the money! 
There is one money location, one thief,
and any number of guards on each floor of the casino. 
 
Task:  
Evaluate a given floor of the casino to determine
if there is a guard between the money and the thief,
if there is not, you will sound an alarm. 
 
Input Format: 
A string of characters that includes $ (money), T (thief),
and G (guard), that represents the layout of the casino floor.   
Space on the casino floor that is not occupied by either money,
the thief, or a guard is represented by the character x. 
 
Output Format:  
A string that says 'ALARM' if the money is in danger
or 'quiet' if the money is safe. 
 
Sample Input:  
xxxxxGxx$xxxT 
 
Sample Output: 
 ALARM

Explanation:  
This input should set off the alarm because there is
no guard between the money and the thief!
'''

floor_layout = input()
money_index = floor_layout.index('$')
thief_index = floor_layout.index('T')
guards_indices = [i for i, char in enumerate(floor_layout) if char == 'G']

money_in_danger = True
for guard_index in guards_indices:
    if min(money_index, thief_index) < guard_index < max(money_index, thief_index):
        money_in_danger = False
        break

if money_in_danger:
    print('ALARM')
else:
    print('quiet')