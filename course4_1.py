#!/usr/bin/python3.6

import random

def userNumber():
    userNum = input("please enter number between 0 and 99:")
    return userNum

def play():
    numOfAttempts = 10
    randomNumber = int(random.random()*100)
    print(randomNumber)
    while (numOfAttempts != 0):
        userNum = userNumber()
        print(userNum) 
        if (randomNumber > userNum):
            numOfAttempts -= 1 
            print("Your Number is less than Rigth number.\nYour have {} attempts ".format(numOfAttempts))
        elif (randomNumber < userNum):
            numOfAttempts -= 1
            print("Your Number is greater than Rigth number.\nYour have {} attempts ".format(numOfAttempts))
        else: 
            print("This game is yours!\n Rigth number is {}".format(randomNumber))
            break
    if (numOfAttempts == 0):
        print("You Lose!:-(")
play()
