# more function practice

from inspect import ArgSpec


#def area(a,b):
    ##return a * b

#print(area(4,5))

def mean(*args):
    return sum (args) / len(args) 

print(mean(1, 3, 4))