# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:34:52 2020

@author: OKS-8
"""

import sys

args = sys.argv
    
if len(args) != 4:
    print('Incorrect parameters')
else:
    for element in range(1, len(args)):
        args[element] = args[element].lstrip('-').split('=')
    print(args)
    
'''        
def mon_payment(principals, period):
    global payment
    if principals % period == 0:
        payment = int(principals / period)
        return f'Your monthly payment = {payment}'
    else:
        payment = int(round(principals / period, 0)) + 1
        global last_payment
        last_payment = principals - (period - 1) * payment
        return f'Your monthly payment = {payment} with last month payment = {last_payment}.'
        
print('Enter the credit principal:')
principals = int(input())
print('What do you want to calculate?')
print('type "m" - for count of months,')
print('type "p" - for monthly payment:')
action = input()
if action == 'm':
    print('Enter monthly payment:')
    mon_pay = int(input())
    period = int(round(principals / mon_pay, 0))
    print()
    if period == 1:
        print(f'It takes {period} month to repay the credit')
    else:
        print(f'It takes {period} months to repay the credit')
elif action == 'p':
    print('Enter count of months:')
    period = int(input())
    print()
    print(mon_payment(principals, period))
'''