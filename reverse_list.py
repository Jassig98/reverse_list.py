# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 8, 2022
# Description: takes a list and reverses its order

def reverse_list(list1):
    i=0
    j= len(list1)-1
    while(i<j):
        t=list1[i]
        list1[i]=list1[j]
        list1[j]=t
        i+=1
        j-=1
"""reverses order of listed values"""
