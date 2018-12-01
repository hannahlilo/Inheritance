#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 08:57:22 2018

@author: hannaholdorf
"""

#%% Inheritance Polygon (HW Session18 - White Belt)

import math

class Polygon:
    
    
    def area(self):
        pass



class Triangle(Polygon):
    
   def  __init__(self, height, base):
    self.height = height
    self.base = base
    
    def area(self):
        return (self.base * self.height)/2



class Circle(Polygon):
    
    def __init__(self, r):
        self.r = r
        
    def area(self):
        return math.pi * self.r ** 2


Triangle(2,2).area()

shapes = [
        Circle(2),
        Triangle(2,3),
        Circle(4)
        ]

for shape in shapes:
    print(shape.area())




