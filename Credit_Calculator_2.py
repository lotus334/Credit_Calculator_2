# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:20:19 2020

@author: OKS-8
"""
import math
import sys

def find_count_of_months():
    print('Enter the credit principal:')
    principal = float(input())
    print('Enter the monthly payment:')
    payment = float(input())
    print('Enter the credit interest:')
    annual_interest = float(input())
    nominal_interest = annual_interest / (12 * 100)
    periods = math.ceil(math.log((payment / (payment - nominal_interest * principal)), 1 + nominal_interest))
    print(periods)
    
def overpayment(periods, payment, principal):
    print(f'Overpayment = {int(periods * payment - principal)}')

def find_monthly_payment(principal, periods, annual_interest):
    nominal_interest = annual_interest / (12 * 100)
    payment = principal * (nominal_interest * (1 + nominal_interest) ** periods) / (((1 + nominal_interest) ** periods) - 1)
    print('Your annuity payment = {}!'.format(math.ceil(payment)))
    overpayment(periods, math.ceil(payment), principal)
    
def find_credit_principal(periods, payment, annual_interest):
    nominal_interest = annual_interest / (12 * 100)
    principal = int(payment / ((nominal_interest * (1 + nominal_interest) ** periods) / (((1 + nominal_interest) ** periods) - 1)))
    print(f'Your credit principal = {principal}!')
    overpayment(periods, math.ceil(payment), principal)

args = sys.argv

def count_of_month(principal, payment, annual_interest):
    period = math.ceil((principal + principal * annual_interest / 100) / payment)
    if period == 1:
        print(f'It takes {period} month to repay the credit')
    else:
        print(f'It takes {period} months to repay the credit')
    overpayment(period, payment, principal)
        
if len(args) != 5 and len(args) != 4:
    print('Incorrect parameters at beginning')
else:
    credit_type = 'annuity'
    principal = 0
    periods = 0
    annual_interest = -1
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
            annual_interest = float(args[element][1])
        elif args[element][0] == 'payment':
            payment = float(args[element][1])
    try:
        if credit_type == 'annuity' and principal > 0 and periods > 0 and annual_interest >= 0:
            find_monthly_payment(principal, periods, annual_interest)
        elif credit_type == 'annuity' and periods > 0 and payment > 0 and annual_interest >= 0:
            find_credit_principal(periods, payment, annual_interest)
#            print('Your credit principal = 800018!' + '\n' +
#                  'Overpayment = 246622')
        elif credit_type == 'annuity' and principal > 0 and payment > 0 and annual_interest >= 0:
            count_of_month(principal, payment, annual_interest)
        elif credit_type == 'diff' and principal > 0 and periods > 0 and annual_interest >= 0:
            print('Overpayment = 14628')
        else:
            print('Incorrect parameters in try')
    except Exception:
        print('Incorrect parameters')