# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:47:24 2018

@author: etuhahm
"""

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                #L[i], L[j] = L[j], L[i]
                print(L)
    print("Final L: ", L)
    

test=[5,7,1,9,20,15,0]

'''
Does this function sort the list in increasing or decreasing order? (items at lower indices being smaller means it sorts in increasing order, and vice versa)

answer: Increasing
Decreasing

'''

'''
6-2
What is the worst case time complexity of swapSort? Consider different kinds of lists when the length of the list is large.

'''


'''
6-3
after changing line range(i+1, len(L)):
'''

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
test=[5,7,1,9,20,15,0]


'''
What happens to the behavior of swapSort with this new code?


No change
modSwapSort now orders the list in descending order for all lists.
modSwapSort now orders the list in descending order for SOME lists but not all
modSwapSort enters an infinite loop.
'''


'''
6-4
best and worst case
answer: Best and worst cases stay the same.

'''

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
test=[5,7,1,9,20,15,0]







    
    