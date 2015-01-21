from turtle import *

color('green','blue')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
color('yellow','red')
begin_fill()
while True:
    backward(200)
    right(170)
    if abs(pos())<1:
        break
end_fill()
done()
    
    
