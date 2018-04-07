# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:48:56 2018

@author: sharda
"""

class bank:
    def __del__(self):
        print('tank you')
    def __init__(self):
        self.bal=0
        print('your current balance is=',self.bal)
    def withdraw(self):
        self.amount=int(input('enter the amount you want withdraw'))
        if(self.bal>=self.amount):
            print('collect your cash')
            self.bal=self.bal-self.amount
            print('your current balance is',self.bal)
        else:
            print('insufficient balance')
    def deposite(self):
        self.add=int(input('enter the amount'))
        e=self.add+self.bal
        self.bal=e
        print('added successfully "\n" you new balance is',e )
        b=int(input('enter your choice'))
        if(b==1):
            self.withdraw()
        else:
            self.check()
        
    def check(self):
        print(self.bal)
obj=bank()
print('choose 1 for withdraw')
print('choose 2 for deposit')
print('choose 3 for check')
c=int(input('enter your choice'))        
if(c==1):
    obj.withdraw()
elif(c==2):
    obj.deposite()
else:
    obj.check()
    
            