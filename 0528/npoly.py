# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:42:18 2021

@author: Mac_1
"""

import turtle as t

s = t.textinput("input", "원하는 다각형 입력 : ")
n = int(s)

for i in range(n):
    t.forward(50)
    t.left(360/n)
    
t.done()