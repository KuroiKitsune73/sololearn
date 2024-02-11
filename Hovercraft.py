'''
You run a hovercraft factory.
Your factory makes ten hovercrafts in a month.
Given the number of customers you got that month,
did you make a profit? It costs you 2,000,000 to build a hovercraft,
and you are selling them for 3,000,000. You also pay 1,000,000 each month
for insurance. 
 
Task:  
Determine whether or not you made a profit based on how many
of the ten hovercrafts you were able to sell that month. 
  
Input Format:  
An integer that represents the sales that you made that month. 
 
Output Format:  
A string that says 'Profit', 'Loss', or 'Broke Even'. 
 
Sample Input:  
5 
 
Sample Output:  
Loss

Explanation:  
If you only sold 5 hovercrafts, you spent 21,000,000
to operate but only made 15,000,000.
'''

sales_num = int(input())
build_cost_per_hovercraft = 2000000
sell_price_per_hovercraft = 3000000
insurance_cost = 1000000
total_hovercrafts = 10

total_build_cost = total_hovercrafts * build_cost_per_hovercraft
total_sell_revenue = sales_num * sell_price_per_hovercraft
total_insurance_cost = insurance_cost

total_cost = total_build_cost + total_insurance_cost
total_revenue = total_sell_revenue

if total_revenue < total_cost:
    print('Loss')
elif total_revenue == total_cost:
    print('Broke Even')
else:
    print('Profit')