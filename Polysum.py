# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

monthlyInterestRate = annualInterestRate/12
lowestBal = int((balance + (balance*annualInterestRate)) / 12)
if lowestBal%10 != 0:
    lowestBal -= (lowestBal%10)
    lowestBal += 10

for i in range(0, 12):
    monthlyUnpaidBalance = balance - lowestBal
    updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    balance = updatedBalance
while balance < -120 - 120*annualInterestRate:
    lowestBal -= 10
    balance += 120 + 120*annualInterestRate
if balance < -100:
    lowestBal -= 10
    30323.19
    28129.27
 """   
balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12 
lowerBound = balance/12 
upperBound = (balance * (1 + monthlyInterestRate)**12)/12
balCheck = 1
guess = (lowerBound + upperBound) / 2

def calcBal (guess, balance):
    result = balance 
    i = 0
    while i < 12:
        monthsInterest = balance*monthlyInterestRate
        result += monthsInterest
        balance += monthsInterest
        balance -= guess
        i += 1
    return result 
    
while balCheck > 0.01:
    #compute the interested balance here - fakeBalance***
    interestedBalance = calcBal(guess, balance)
    balCheck = interestedBalance - 12*guess
    if balCheck > 0:
        #Upper Loop
        lowerBound = guess 
        guess = round((upperBound+guess)/2, 2)
    elif balCheck < 0: 
        #lower Loop
        upperBound = guess
        guess = round((lowerBound+guess)/2, 2)
    elif balCheck == 0: 
        break
print("Lowest Payment: " + str(guess))

