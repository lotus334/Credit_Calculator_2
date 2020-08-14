# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:20:19 2020

@author: OKS-8
"""
import math

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

def find_monthly_payment():
    print('Enter the credit principal:')
    principal = float(input())
    print('Enter the number of periods:')
    periods = int(input())
    print('Enter the credit interest:')
    annual_interest = float(input())
    nominal_interest = annual_interest / (12 * 100)
    payment = principal * (nominal_interest * (1 + nominal_interest) ** periods) / (((1 + nominal_interest) ** periods) - 1)
    print(payment)
    
def find_credit_principal():
    print('Enter the monthly_payment:')
    payment = float(input())
    print('Enter the count of periods:')
    periods = int(input())
    print('Enter the credit interest:')
    annual_interest = float(input())
    nominal_interest = annual_interest / (12 * 100)
    principal = payment / ((nominal_interest * (1 + nominal_interest) ** periods) / (((1 + nominal_interest) ** periods) - 1))
    print(principal)

def what_to_calculate():
    print('''What do you want to calculate?
          type "n" for the count of months,
          type "a" for the annuity monthly payment,
          type "p" for the credit principal:''')
    choice = input()
    if choice == 'n':
        find_count_of_months()
    elif choice == 'a':
        find_monthly_payment()
    elif choice == 'p':
        find_credit_principal()


#ordinary_annuity = principal * (nominal_interest * (1 + nominal_interest) ** periods) / (((1 + nominal_interest) ** periods) - 1)
        
what_to_calculate()