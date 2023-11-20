import os
import math
import sys
import re

n = int(input("Enter the number of cities in Goodland :"))
k = int(input("Enter the plant's range constant :"))
arr = []
for i in range(n):
    val = int(input("Enter the values :"))
    arr.append(val)



def pylons(k,arr):
    count = i = 0
    loc = i+k-1
    while i<n:
        if arr[loc] ==1:
            i=loc+k
            loc = i+k-1
            count +=1
            if loc>=n:
                loc = n-1
        else:
            loc -=1
            if loc<i-k+1 or loc<0:
                return -1

    return count

print(pylons(k,arr))





