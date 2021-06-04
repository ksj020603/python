# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:51:52 2021

@author: Mac_1
"""

import turtle as t
import random as r

for i in range(50):
    length = r.randint(1,100)
    t.forward(length)
    angle = r.randint(-180,180)
    t.left(angle)
    
t.done()