#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 11:47:50 2018

@author: tuheenahmmed
"""

def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)

linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)


##exercise 2

def program1(x):
    total = 0
    count=0
    for i in range(1000):
        total += i
        count+=1
    while x > 0:
        x -= 1
        total += x

    return total

program1(0)



def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x = x//2
        total += x

    return total

program2()




def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x

    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)

program3([q,a,b])




def program1(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples



def search(L, e):
    for i in range(len(L)):
        print(len(L))
        if L[i] == e:
            print(L[i])
            return True
            
        if L[i] > e:
            return False
            print(L[i])
    return False

search([],5)
search([0,1,2,5,10],10)





def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

search([],5)


search1([0,1,2,5,10],10)



def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

search([0,1,2,5,10],10)

search([],5)



def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False

search2([0,1,2,5,10],10)


search2([],5)



def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

search([],5)


search([0,1,2,5,10],10)



def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)

search3([],5)
    
search3([0,1,2,5,10],10)   



#selection sort

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        print(L)
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
            
test=[5,6,8,1,0,60]        
            
            

def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        print(L)
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            
test=[5,6,8,1,0,9]  


test1=[6,1,0,50,1,4,9,50]
            
            
            
def mySort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        print(L)
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                
                
test1=[1,2,3]
           
            
            
def newSort(L):
    """ L, list with unique elements """
    for i in range(len(L) - 1):
        j=i+1
        print(L)
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            
test1=[1,2,3]
            
            
            
            
            
            
            
            



















