from turtle import *
from time import sleep

bgcolor("black")
color("purple")
width(5)

def line(start_x,start_y,end_x,end_y):
    pu()
    goto(start_x,start_y)
    pd()
    goto(end_x,end_y)

line(0,0,0,300)
line(0,300,-128,221)
line(-128,221,-120,105)
line(194,-183,138,47)
line(138,47,0,0)
line(0,0,-104,-81)
line(-104,-81,-254,5,)
line(166,229,54,159)
line(54,159,0,300)

begin_fill()
circle(50)
end_fill()

sleep(60)