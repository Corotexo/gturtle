from random import randint
import turtle as t
from math import sqrt
from time import sleep
from tkinter import messagebox

tr = t.Turtle()
screen = t.Screen()
SIZE_MULT = 3

class _screen():
    def onkey(self, function, key) -> None:
        t.onkey(function, key)
        
    def onclick(self, function) -> None:
        t.onscreenclick(function)
        
    def listen(self) -> None:
        t.listen()

_screen = _screen()

def Screen():
    return _screen

def makeTurtle() -> None:
    tr.pensize(SIZE_MULT)
    tr.setheading(90)
    tr.shape("turtle")
    tr.shapesize(SIZE_MULT, SIZE_MULT, SIZE_MULT)
    t.title("gTurtle")

def forward(steps: float) -> None:
    tr.forward(steps * SIZE_MULT)

def back(steps: float) -> None:
    tr.back(steps * SIZE_MULT)

def left(degrees: float) -> None:
    tr.left(degrees)

def right(degrees: float) -> None:
    tr.right(degrees)

def setPenColor(color: str) -> None:
    tr.pencolor(color)

def setPenWidth(width: int) -> None:
    tr.pensize(width * SIZE_MULT)

def delay(ms: int) -> None:
    sleep(ms / 1000)

def speed(speed: float) -> None:
    tr.speed(speed)

def hideTurtle() -> None:
    tr.speed(-1)
    tr.hideturtle()
    t.tracer(0, 0)

def showTurtle() -> None:
    tr.showturtle
    t.tracer(1, 0)

def penUp() -> None:
    tr.penup()

def penDown() -> None:
    tr.pendown()

def dot(diameter: float) -> None:
    tr.dot(diameter * SIZE_MULT)

def setHeading(angle: float) -> None:
    tr.setheading(angle + 90)

def heading(angle: float = None) -> float:
    if angle != None:
        setHeading(angle)
    return tr.heading

def setRandomHeading() -> None:
    tr.setheading(randint(0, 359))

def leftCircle(radius: float) -> None:
    tr.circle(radius * SIZE_MULT)

def rightCircle(radius: float) -> None:
    tr.circle(radius * SIZE_MULT * -1)

def leftArc(radius: float, angle: int) -> None:
    tr.circle(radius * SIZE_MULT, angle)

def rightArc(radius: float, angle: int) -> None:
    tr.circle(radius * SIZE_MULT * -1, angle)


def label(text: str) -> None:
    tr.write(text, move=False, align='left', font=('Arial', tr.pensize() * SIZE_MULT, 'normal'))

def setFillColor(color: str):
    tr.fillcolor(color)

def startPath() -> None:
    tr.begin_fill()

def fillPath() -> None:
    tr.end_fill()

def sqrt(number: float) -> float:
    return sqrt(number)

def isInteger(number: float) -> bool:
    return isinstance(number, int)

def getPos() -> list:
    return [tr.xcor, tr.ycor]

def setPos(x, y) -> None:
    tr.penup()
    tr.setpos(x, y)
    tr.pendown()

def getX() -> float:
    return tr.xcor()

def getY() -> float:
    return tr.ycor()

def setX(x) -> None:
    tr.penup()
    tr.setx(x)
    tr.pendown()

def setY(y) -> None:
    tr.penup()
    tr.sety(y)
    tr.pendown()
  
def update() -> None:
    t.update()

def clean():
    tr.clear()
    
def clearScreen() -> None:
    tr.clear()
    tr.setpos(0, 0)

def clear() -> None:
    tr.clear()
    tr.hideturtle()

def done() -> None:
    t.done()

fd = forward
bk = back
lt = left
rt = right
spc = setPenColor
spw = setLineWidth = setPenWidth
ht = hideTurtle
st = showTurtle
cs = clearScreen