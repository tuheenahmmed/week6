# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:33:14 2018

@author: etuhahm
"""

def search(L, e):
    for i in range(len(L)):
        print(len(L))
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

search([4,5,6],6)

search([1,2,3,4,5],3)


def newsearch(L, e):
    size = len(L)
    print(size)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

newsearch([4,5,6],6)

newsearch([1,2,3,4,5],3)



'''

Which of the following statements is correct? You may assume that each function is tested with a list L whose elements are sorted in increasing order; for simplicity, assume L is a list of positive integers.


x search and newsearch return the same answers for all L and e.
x search and newsearch return the same answers provided L is non-empty.
x search and newsearch return the same answers provided L is non-empty and e is in L.
x search and newsearch never return the same answers.
correct: search and newsearch return the same answers for lists L of length 0, 1, or 2.
'''