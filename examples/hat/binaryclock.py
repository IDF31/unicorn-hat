#!/usr/bin/env python
import unicornhat as uh
import datetime

uh.rotation(0)
uh.brightness(1)

def draw_time(b,x,idx,color):
    
    month = bin(month)[2:][::-1]
    day = bin(day)[2:][::-1]
    hour = bin(hour)[2:][::-1]
    minute = bin(minute)[2:][::-1]
    second = bin(second)[2:][::-1]
    
    if b == '1':
        uh.set_pixel(x,idx,color)

while True:
    uh.clear()
    
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    for idx,b in enumerate(hour):
        draw_time(b,7,idx,'red')

    for idx,b in enumerate(minute):
        draw_time(b,6,idx,'yellow')

    for idx,b in enumerate(second):
        draw_time(b,5,idx,'blue')

    for idx,b in enumerate(day):
        draw_time(b,3,idx,'green')

    for idx,b in enumerate(month):
        draw_time(b,2,idx,'purple')
    uh.show()
