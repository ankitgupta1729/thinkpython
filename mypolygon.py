import turtle
bob = turtle.Turtle()
print(bob)
for i in range(4):
    #turtle.fd(30)
    turtle.pu()
    turtle.fd(10)    
    turtle.pd()
    turtle.fd(50) 
# import time
# time.sleep(10)
# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob, 7, 70)

import math
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
#n is the number of line segments in our approximation of a circle, so length is the length
#of each segment. Thus, polygon draws a 50-sided polygon that approximates a circle with
#radius r.
circle(bob, 15)

def circle1(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)
circle(bob, 50)

#4.7 Refactoring
#When I wrote circle, I was able to re-use polygon because a many-sided polygon is a good
#approximation of a circle. But arc is not as cooperative; we can’t use polygon or circle to
#draw an arc.
#One alternative is to start with a copy of polygon and transform it into arc. The result
#might look like this:
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
arc(bob,100,45)

# The second half of this function looks like polygon, but we can’t re-use polygon without
# changing the interface. We could generalize polygon to take an angle as a third argument,
# but then polygon would no longer be an appropriate name! Instead, let’s call the more
# general function polyline:
    
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polyline(bob, 3, 120, 45)
        
#Now we can rewrite polygon and arc to use polyline:
    
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

polygon(bob, 7, 70)
    
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
arc(bob,100,45)
#Finally, we can rewrite circle to use arc:
    
def circle(t, r):
    arc(t, r, 360)    

circle(bob, 50)
turtle.mainloop()