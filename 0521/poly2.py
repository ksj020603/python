# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:32:39 2021

@author: Mac_1
"""

import turtle as t
t.shape("turtle")
while True:

    s = t.textinput("도형","원하는 다각형을 입력.")
    t.reset()
    if s == "사각형" :
        s = t.textinput("가로","가로 길이 :")
        w = int(s)
        s = t.textinput("세로", "세로 길이 :")
        h = int(s)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
    elif s == "삼각형" :
        s = t.textinput("길이","길이 입력 :")
        l = int(s)
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.forward(l)
    elif s == "원" :
        s = t.textinput("반지름","반지름 입력 :")
        sr = int(s)
        t.circle(sr)
    elif s == "종료" :
        t.bye()
    else:
        t.write("잘못된 입력", "삼각형, 사각형, 원 중 선")
t.exitonclick