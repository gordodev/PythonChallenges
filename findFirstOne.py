#!/usr/bin/python3

#Program to find the first "1" in a list of randomly generated numbers
#This loop has a bug. There is some strange behavior. Should just show number and where the one is. One at time and consistently.

import random
import time
import time
import os

numbers=[]
numbersList=[]

def random_list():
    numbers=random.randrange(1000000000000, 1999999999999)
    #print (numbers)
    global numbersList
    numbersList = [int(x) for x in str(numbers)]
    random.shuffle(numbersList)

def first_one(num):              #Find first number
    #print (numbersList)   
    #print (num)     #81424
    found=0
    iteration=0
    lastDigit=0
    #print("First digit is: ",num[0])
    for x in range(len(num)):
        iteration=iteration+1
        #print ("iteration: ",iteration)
        currentDigit=num[x]
        #print (currentDigit)
        
        if num[x] != 1:
            lastDigit=num[x]
            #print ("Not a one. Moving to next digit.")
            print (".")
            time.sleep(0.2)
            os.system("clear")
            continue                                      #Starting loop again; check next number
        
        if iteration > 0:
            if num[x] == 1:
                print (num)
                print ("Found a one right after: ",lastDigit)
                time.sleep(3)
                break

        if num[x] == 1:
            found=1
            print ("The FIRST number is a ONE dude!")
            time.sleep(2)
            print ("Breaking!")
            time.sleep(0.8)
            break

while True:
    #print ("This is your random number")
    random_list()           #Generate random number list
    #print(numbersList)
    #print(numbersList[0])  #test: show fist element
    first_one(numbersList)
    time.sleep(0.5)
