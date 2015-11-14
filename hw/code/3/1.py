from __future__ import division, print_function
from random import randint,random

#1
def has_duplicates(a):
    for x in a:
	if a.count(x) > 1:
	    return True
    return False

#print has_duplicates([1,2,3,4,4])

#2
def rand_birthdays(size):
    lst = []
    for i in range(0,size):
        lst.append(randint(1,365))
    return lst

def paradox(size,chances):
    dup_count = 0
    for i in range(0,chances):
        lst = rand_birthdays(size)
        if has_duplicates(lst):
            dup_count +=1
    return dup_count/chances

if __name__ == '__main__':
    size = 23
    chances = 1000
    print ("the probability of having the birthday on the same day is :",paradox(size,chances))
