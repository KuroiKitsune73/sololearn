'''
You and your friends are going to Europe!
You have made plans to travel around Europe with your friends,
but one thing you need to take into account
so that everything goes according to play,
is that the format of their date is different
than from what is used in the United States.
Your job is to convert all your dates from MM/DD/YYYY to DD/MM/YYYY. 
 
Task:  
Create a function that takes in a string
containing a date that is in US format,
and return a string of the same date converted to EU. 
 
Input Format:  
A string that contains a date formatting 11/19/2019 or November 19, 2019. 
 
Output Format:  
A string of the same date but in a different format: 19/11/2019. 
 
Sample Input:  
7/26/2019 
 
Sample Output:  
26/7/2019

Note, that the input can be in two different formats,
11/19/2019 or November 19, 2019.
'''

def convert_to_eu_date(date):
    month_dict = {
        'January': '1',
        'February': '2',
        'March': '3',
        'April': '4',
        'May': '5',
        'June': '6',
        'July': '7',
        'August': '8',
        'September': '9',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    
    if '/' in date:
        date_parts = list(map(int, date.split('/')))
        day = date_parts[1]
        month = date_parts[0]
        year = date_parts[2]
        return f'{day}/{month}/{year}'
    else:
        date_parts = date.split(" ")
        #['Month','dnum,','ynum']
        month = month_dict[date_parts[0]]
        #['Month']
        day = date_parts[1].strip(',')
        #delete comma and return str with day only
        year = date_parts[2]
        return f'{day}/{month}/{year}'

# Sample Input
date = input()

# Convert to EU format and print
print(convert_to_eu_date(date))