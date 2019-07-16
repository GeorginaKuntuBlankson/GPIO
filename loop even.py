#!/usr/bin/python
def evens():
    numb1=input('enter first number')
    numb2=input('enter second number')
    for x in reversed(range (int(numb1),int(numb2))):
        if(x%2==0):
            print (x)
evens()