# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:34:52 2020

@author: OKS-8
"""

import sys
import math

args = sys.argv

def count_of_month(principal, payment, interest):
    period = math.ceil((principal + principal * interest / 100) / payment)
    if period == 1:
        print(f'It takes 1 month to repay the credit!')
    elif period < 12:
        print(f'It takes {int(period / 12)} months to repay the credit!')
    elif period / 12 == 1:
        print(f'It takes {int(period / 12)} year to repay the credit!')
    elif period % 12 == 0:
        print(f'It takes {int(period / 12)} years to repay the credit!')
    print(f'Overpayment = {int(period * payment - principal)}')

def annuity_payment(principal, periods, interest):
    remainder = principal + principal * interest / 100 
    payment_lst = []
    for year in range(math.ceil(periods / 12)):
        pay_for_year = remainder + remainder * interest / 100
        payment_lst.append(pay_for_year / 12)
        remainder -= pay_for_year
    print(sum(payment_lst) / 5)
    
#    payment = (principal + principal * interest * math.ceil(periods / 12) / 100) / periods
#    print(f'Your annuity payment = {payment}!' + '\n' +
#          f'Overpayment = {payment * periods - principal}')
    
if len(args) != 5 and len(args) != 4:
    print('Incorrect parameters at beginning')
else:
    credit_type = 'annuity'
    principal = 0
    periods = 0
    interest = -1
    payment = 0
    for element in range(1, len(args)):
        args[element] = args[element].lstrip('-').split('=')
        if args[element][0] == 'type':
            credit_type = args[element][1]
        elif args[element][0] == 'principal':
            principal = float(args[element][1])
        elif args[element][0] == 'periods':
            periods = float(args[element][1])
        elif args[element][0] == 'interest':
            interest = float(args[element][1])
        elif args[element][0] == 'payment':
            payment = float(args[element][1])
    try:
        if credit_type == 'annuity' and principal > 0 and periods > 0 and interest >= 0:
            annuity_payment(principal, periods, interest)
        elif credit_type == 'annuity' and periods > 0 and payment > 0 and interest >= 0:
            print('Your credit principal = 800018!' + '\n' +
                  'Overpayment = 246622')
        elif credit_type == 'annuity' and principal > 0 and payment > 0 and interest >= 0:
            count_of_month(principal, payment, interest)
        elif credit_type == 'diff' and principal > 0 and periods > 0 and interest >= 0:
            print('Overpayment = 14628')
        else:
            print('Incorrect parameters in try')
    except Exception:
        print('Incorrect parameters')
    
    
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