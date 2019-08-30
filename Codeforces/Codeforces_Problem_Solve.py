# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:58:36 2019

@author: Ryans
"""
import numpy as np
## 4A - Watermelon
x = int(input())
#print(x)
if x%2 == 0 and x>=4:
    print("YES")
else:
    print("NO")


## 1A
m,n,a = map(int,raw_input().split() )
print(m)
print(n)
print(a)
print-n/a
print(-m/a)

print(-5/2)  # making ceil 

    
n,m,a=map(int,raw_input().split())
print( -n//a * (-m//a) )


### 71A
for _ in range(int(input())):
    s = input()
    print s[0]+str(len(s)-2)+s[-1] if len(s)>10 else s

