# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:31:39 2023
matala 1
@author: Linoy Medalsy
"""
#ex1
def my_func(x1,x2,x3):
    
    if type(x1) == int or type(x2) == int or type(x3) == int:
        print("Error: parameters should be float")
        
    elif type(x1) != float or type(x2) != float or type(x3) != float:
        print("None")
        
    elif x1+x2+x3 == 0:
        print("Not a number – denominator equals zero")
        
    calc = float(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))
    return calc
print(my_func(2.0, 6.0, 3.0))

