# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:05:50 2023

@author: Alex Nolan
"""

def MCint(f, a, b, n):
    """
    
    Parameters
    ----------
    f : TYPE function
        f returns a float between a and b
    a : TYPE float 
        DESCRIPTION. lower limit
    b : TYPE float
        DESCRIPTION. upper limit
    n : TYPE int
        DESCRIPTION, number of random points to take in the box

    Returns
    -------
    integral of f from a to b

    """

    from random import random
    # random returns a random number betwee 0 and 1
    
    
    maxF = 4
    
    area = 0
    saveX = []
    saveY = []
    
    for i in range(n):
        
        #generate a random point in the boxc
        #x between a and b
        #z between 0 and maxF
        randNoX = random()*(b-a)+(b-a) + a
        randNoY = random()*maxF
        saveX.append(randNoX)
        saveY.append(randNoY)
        
        
        
        
        if randNoY <= f(randNoX): area += 1
    
    boxArea = (b-a)*maxF
    integral = area/n * boxArea
    print(min(saveX), max(saveX))
    print(min(saveY), max(saveY))
    return(integral)
    
if __name__ == "__main__":
    
    import numpy as np    
    import matplotlib.pyplot as plt
    
    def f(x) :
        return x**2
    
    area = MCint(f, 0.5, 2., 50000)
    
    print(round(area, 2))