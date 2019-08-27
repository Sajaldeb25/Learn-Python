# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:55:26 2019

@author: Ryans
"""
y = 100<10
print(y)
type(y)

## slice notation 
a = [2,4,6,8]
# The general rule is that a[m:n] returns n - m elements, starting at a[m].
a[1:3]
a[1:]
a[-3:]

s = 'Sajal Debnath'
print (s)
s[-10:]


## with directories
d = {'name': 'Frodo', 'age': 33}
type(d)

## set
s1 = {'a', 'b'}
type(s1)

s3 = set(('foo', 'bar', 'foo'))
s3

## input and output 
f = open('newfile.txt', 'w')   # Open 'newfile.txt' for writing
f.write('Testing\n')           # Here '\n' means new line
f.write('\n')
f.write('Testing again')
f.close()

#path
%pwd

# read mode 
f = open('newfile.txt', 'r')
out = f.read()
out

print(out)
f = open('newfile.txt', 'a') # append
f.write("appended")

f = open('newfile.txt', 'r')  # read
out = f.read()

print(out)


names = ['Tom', 'John']
marks = ['E', 'F']
dict(zip(names, marks))



# Exercise 1
x_vals = [1, 2, 3]
y_vals = [1, 1, 1]
zip(x_vals, y_vals)
sum([x * y for x, y in zip(x_vals, y_vals)])

sum(x%2 == 0 for x in range(100) )

pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
sum( [ x%2==0 and y%2 == 0  for x,y in pairs ] )


#Exercise 3

def func(String):
    cnt = 0
    for letter in String :
        if letter == letter.upper() and letter.isalpha():
            cnt = cnt+1
    return cnt 

func('Sajal DebNath') # ans =3 

def func(seq_a, seq_b):
    is_subset = True
    for a in seq_a:
        if a not in seq_b:
            is_subset = False
    return is_subset

# == test == #

print(func ([1, 2], [1, 2, 3]) )
print(func ([1, 2, 3], [1, 2]) )



def func(seq_a, seq_b):
    return set(seq_a).issubset(set(seq_b))

print(func ([1, 2], [1, 2, 3]) )
print(func ([1, 2, 3], [1, 2]) )
