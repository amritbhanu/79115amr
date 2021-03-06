from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
#pu(bob)
#fd(bob, 60)
#pd(bob)

'''def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)'''

'''def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 2) + 1
    step_length = arc_length / n
    #1#step_angle = float(angle) / (2*n)
    step_angle = float(angle) / n
    polyline(t, n, step_length/2, step_angle/2)

def circle(t, r):
    arc(t, r, 360)

for i in range(0,8):
	circle(bob,50)
	#1#lt(bob,135)
	lt(bob,90)

wait_for_user()'''

#tried some code above but the correct one referenced from http://www.greenteapress.com/thinkpython/code/flower.py

#4.1
'''
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)
	
def small_eclipse(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)


def shape_center(t, n, r, angle):
    for i in range(n):
        small_eclipse(t, r, angle)
        lt(t, 360.0/n)

#shape_center(bob, 7, 60.0, 60.0)
#shape_center(bob, 10, 40.0, 80.0)
shape_center(bob, 20, 140.0, 20.0)

wait_for_user()'''

#4.2
def pie(t, n, r):
    for i in range(n):
        fd(t,size)
        rt(t,180.0)
        pu(t)
        fd(t,size)
        pd(t)
        lt(t,180 - 360.0/n)

    fd(t,size)
    lt(t,90 + 180.0/n)
    x=size*(math.sin(360/n * math.pi / 180)/math.sin((90-180.0/n)*math.pi/180))
    for j in range(n):
        fd(t,x)
        lt(t,360/n)
        

size = 40
#pie(bob,5,size)
#pie(bob,6,size)
pie(bob,7,size)

wait_for_user()
