# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:29:46 2021

@author: Mac_1
"""

import turtle as t

def drawRect(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
        
t.up()
t.goto(-200,0)
t.down()
drawRect(100)
t.up()
t.goto(0,0)
t.down()
drawRect(100)
t.up()
t.goto(200,0)
t.down()
drawRect(100)

t.done()
t.bye()