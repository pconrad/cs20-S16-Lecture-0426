import turtle

def drawSquare(sideLen,t):
    '''
    draw a square.  current pos of t is lower left
    we force t to be pen down, and heading 0
    '''
    t.down()

    t.setheading(0)

    for i in range(4):    
      t.forward(sideLen)
      t.left(90)

jane = turtle.Turtle()
jane.color('green')
george = turtle.Turtle()
george.color('red')
mark= turtle.Turtle()
mark.color('blue')
  


def go():
    drawSquare(20, jane)
    drawSquare(200, george)
 
  
