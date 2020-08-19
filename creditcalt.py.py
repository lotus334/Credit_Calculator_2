# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:20:19 2020

@author: OKS-8
"""

'''
How to use:
    1) Type in command line interface (CLI) command 'python' and after 
    whitespace the name of the program
    2) After whitespace type options:
    --annual OR --diff
    --principal=
    --periods=
    --interest=
    --payment=
    3) The program will return informatino about credit
    If there is no combination of parameters or they are incorrect, 
    the program return 'Incorrect parameters'
    
For example:
    Input: python creditcalc.py --type=diff --principal=1000000 --periods=10 
    --interest=10
    Output: Month 1: paid out 108334
            Month 2: paid out 107500
            Month 3: paid out 106667
            Month 4: paid out 105834
            Month 5: paid out 105000
            Month 6: paid out 104167
            Month 7: paid out 103334
            Month 8: paid out 102500
            Month 9: paid out 101667
            Month 10: paid out 100834
            
            Overpayment = 45837
            
    Input: python creditcalc.py --type=annuity --principal=1000000 
    --periods=60 --interest=10
    Output: Your annuity payment = 21248!
            Overpayment = 274880

    Input: python creditcalc.py --type=diff --principal=1000000 
    --payment=104000
    Output: Incorrect parameters.

    Input:  python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
    Output: Month 1: paid out 65750
            Month 2: paid out 65344
            Month 3: paid out 64938
            Month 4: paid out 64532
            Month 5: paid out 64125
            Month 6: paid out 63719
            Month 7: paid out 63313
            Month 8: paid out 62907
            
            Overpayment = 14628

    Input:  python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
    Output: Your credit principal = 800018!
            Overpayment = 246622

    Input: python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
    Output: You need 2 years to repay this credit!
            Overpayment = 52000
'''

'''
Import the necessary modules
'''
import math
import sys
'''
Get the list of arguments
'''
args = sys.argv

def find_count_of_months(principal, annual_interest, periods):
    '''
    Parameters
    ----------
    principal : float or int
    annual_interest : float or int
        as an percentage: type 10 instead of 10% or 0.1..
    periods : float or int

    Returns
    -------
    Calculate the payments for all months.
    '''
    nominal_interest = annual_interest / (12 * 100)
    count = 1
    paid = 0
    while count <= periods:
        diff_pay = (principal / periods) + nominal_interest * (principal - (principal * (count - 1)) / periods)
        print(f'Month {count}: paid out {math.ceil(diff_pay)}')
        count += 1
        paid += math.ceil(diff_pay)
    print(f'Overpayment = {int(paid - principal)}')
    
def overpayment(periods, payment, principal):
    print(f'Overpayment = {int(periods * payment - principal)}')

def find_monthly_payment(principal, periods, annual_interest):
    '''
    Parameters
    ----------
    principal : float or int
    periods : float or int
    annual_interest : float or int
        as an percentage: type 10 instead of 10% or 0.1.

    Returns
    -------
    The text message.
    '''
    nominal_interest = annual_interest / (12 * 100)
    payment = principal * (nominal_interest * (1 + nominal_interest) ** periods) / (((1 + nominal_interest) ** periods) - 1)
    print('Your annuity payment = {}!'.format(math.ceil(payment)))
    overpayment(periods, math.ceil(payment), principal)
    
def find_credit_principal(periods, payment, annual_interest):
    '''
    Parameters
    ----------
    periods : float or int
    payment : float or int
    annual_interest : float or int
        as an percentage: type 10 instead of 10% or 0.1.

    Returns
    -------
    The text message.
    '''
    nominal_interest = annual_interest / (12 * 100)
    principal = int(payment / ((nominal_interest * (1 + nominal_interest) ** periods) / (((1 + nominal_interest) ** periods) - 1)))
    print(f'Your credit principal = {principal}!')
    overpayment(periods, math.ceil(payment), principal)

def count_of_month(principal, payment, annual_interest):
    '''
    Parameters
    ----------
    principal : float or int
    payment : float or int
    annual_interest : float or int
        as an percentage: type 10 instead of 10% or 0.1.

    Returns
    -------
    The text message.
    '''
    period = math.ceil((principal + principal * annual_interest / 100) / payment)
    if period == 1:
        print(f'It takes {period} month to repay the credit')
    elif period % 12 == 0 and period // 12 == 1:
        print(f'It takes {period // 12} year to repay the credit')
    elif period % 12 == 0:
        print(f'It takes {period // 12} years to repay the credit')
    elif period > 12 and period // 12 == 1 and period % 12 == 1:
        print(f'It takes {period // 12} year and {period % 12} month to repay the credit')
    elif period > 12 and period // 12 == 1:
        print(f'It takes {period // 12} year and {period % 12} months to repay the credit')
    elif period > 12 and period % 12 == 1:
        print(f'It takes {period // 12} years and {period % 12} month to repay the credit')
    elif period > 12:
        print(f'It takes {period // 12} years and {period % 12} months to repay the credit')
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
            find_count_of_months(principal, annual_interest, periods)
        else:
            print('Incorrect parameters in try')
    except Exception:
        print('Incorrect parameters')