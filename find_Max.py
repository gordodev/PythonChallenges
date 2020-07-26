#!/usr/bin/python3

#Find the largest number
#This code is not working. If you enter a few numbers that are not larger, it will crash.

lastMax=0
#int(lastMax)

#FindMax function
def check_max(num,lastMax):
    if num > lastMax:
        print("new num is larger")
        print ("LastMax was:",lastMax);lastMax=num; print ("This is now lastMax",lastMax)
        return lastMax
    else:
        return print(lastMax)



#loop
#Ask user for numbers
while True:
    yourNum=int(input("Enter number: \n"))
    #biggest=check_max(yourNum,lastMax)
    #check_max(yourNum,lastMax)
    #print ("\n\nLargest is",biggest)
    check_max(yourNum,lastMax)
    print(lastMax)
    lastMax=check_max(yourNum,lastMax)
    print (lastMax)

#run largest function
  
