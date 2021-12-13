'''
Issues:
Play again function?
'''

import turtle
import time
import random

board = [[0,0,0], [0,0,0], [0,0,0],[0]]

def tic_tac_toe_board():
  b = turtle.Turtle()
  b.hideturtle()
  b.speed("fastest")
  b.pensize(5)
  b.up()
  b.right(90)
  b.goto(-80,240)
  b.down()
  b.forward(480)
  b.up()
  b.goto(80,240)
  b.down()
  b.forward(480)
  b.up()
  b.left(90)
  b.goto(-240,80)
  b.down()
  b.forward(480)
  b.up()
  b.goto(-240,-80)
  b.down()
  b.forward(480)
  time.sleep(0.5)

tic_tac_toe_board()

text = turtle.Turtle()
text.up()
text.hideturtle()
text.speed("fastest")
text.goto(0,300)
text.down()
text.write("You are X's. The computer is O's. Good luck!", align = "center", font=("Times new roman", 24, "bold", "normal"))
time.sleep(2)
text.clear()

s = turtle.Screen()
s.listen()

box_clicker = turtle.Turtle()
box_clicker.hideturtle()
box_clicker.speed("fastest")
box_clicker.up()
box_clicker.goto(-300,-300)

def box_click(x,y):
  box_clicker.up()
  box_clicker.speed("fastest")
  box_clicker.goto(x,y)
  return box_clicker

def update_board_player(board):
  s.onclick(box_click)
  if -240 < box_clicker.xcor() < -80:
    column = 1
  elif -80 < box_clicker.xcor() < 80:
    column = 2
  elif 80 < box_clicker.xcor() < 240:
    column = 3
  if -240 < box_clicker.ycor() < -80:
    row = 3
  elif -80 < box_clicker.ycor() < 80:
    row = 2
  elif 80 < box_clicker.ycor() < 240:
    row = 1
  else:
    row = 4
    column = 1
  a = column-2
  b = -1*row+2
  if (row == 4 and column == 1):
    X = turtle.Turtle()
    X.hideturtle()
    X.up()
    X.speed("fastest")
    X.goto(-40+a*160,40+b*160)
    board[-1*b+1][a+1] = 1
  if (board[-1*b+1][a+1] == 0 and row != 4):
    X = turtle.Turtle()
    X.hideturtle()
    X.speed(25)
    X.pensize(5)
    X.up()
    X.goto(-40+a*160,40+b*160)
    X.down()
    X.right(45)
    X.forward(120)
    X.up()
    X.goto(40+a*160,40+b*160)
    X.down()
    X.right(90)
    X.forward(120)
    board[-1*b+1][a+1] = 1
  else:
    time.sleep(0.1)
    update_board_player(board)

def update_board_computer(board):
  row = random.randint(1,3)
  column = random.randint(1,3)
  if ((board[0][0] == board[0][1] == 2 or board[1][2] == board[2][2] == 2 or board[2][0] == board[1][1] == 2) and board[0][2] != 1):
    a = 1
    b = 1
  elif ((board[0][0] == board[0][2] == 2 or board[2][1] == board[1][1] == 2) and board[0][1] != 1):
    a = 0
    b = 1
  elif ((board[0][0] == board[1][0] == 2 or board[0][2] == board[1][1] == 2 or board[2][1] == board[2][2] == 2) and board[2][0] != 1):
    a = -1
    b = -1
  elif ((board[0][0] == board[2][0] == 2 or board[1][2] == board[1][1] == 2) and board[1][0] != 1):
    a = -1
    b = 0
  elif ((board[0][0] == board[1][1] == 2 or board[0][2] == board[1][2] == 2 or board[2][0] == board[2][1] == 2) and board[2][2] != 1):
    a = 1
    b = -1
  elif ((board[0][0] == board[2][2] == 2 or board[0][1] == board[2][1] == 2 or board[0][2] == board[2][0] == 2 or board[1][0] == board[1][2] == 2) and board[1][1] != 1):
    a = 0
    b = 0
  elif ((board[0][1] == board[0][2] == 2 or board[1][0] == board[2][0] == 2 or board[2][2] == board[1][1] == 2) and board[0][0] != 1):
    a = -1
    b = 1
  elif ((board[0][1] == board[1][1] == 2 or board[2][0] == board[2][2] == 2) and board[2][1] != 1):
    a = 0
    b = -1
  elif ((board[0][2] == board[2][2] == 2 or board[1][0] == board[1][1] == 2) and board[1][2] != 1):
    a = 1
    b = 0
  elif ((board[0][0] == board[0][1] == 1 or board[1][2] == board[2][2] == 1 or board[2][0] == board[1][1] == 1) and board[0][2] != 2):
    a = 1
    b = 1
  elif ((board[0][0] == board[0][2] == 1 or board[2][1] == board[1][1] == 1) and board[0][1] != 2):
    a = 0
    b = 1
  elif ((board[0][0] == board[1][0] == 1 or board[0][2] == board[1][1] == 1 or board[2][1] == board[2][2] == 1) and board[2][0] != 2):
    a = -1
    b = -1
  elif ((board[0][0] == board[2][0] == 1 or board[1][2] == board[1][1] == 1) and board[1][0] != 2):
    a = -1
    b = 0
  elif ((board[0][0] == board[1][1] == 1 or board[0][2] == board[1][2] == 1 or board[2][0] == board[2][1] == 1) and board[2][2] != 2):
    a = 1
    b = -1
  elif ((board[0][0] == board[2][2] == 1 or board[0][1] == board[2][1] == 1 or board[0][2] == board[2][0] == 1 or board[1][0] == board[1][2] == 1) and board[1][1] != 2):
    a = 0
    b = 0
  elif ((board[0][1] == board[0][2] == 1 or board[1][0] == board[2][0] == 1 or board[2][2] == board[1][1] == 1) and board[0][0] != 2):
    a = -1
    b = 1
  elif ((board[0][1] == board[1][1] == 1 or board[2][0] == board[2][2] == 1) and board[2][1] != 2):
    a = 0
    b = -1
  elif ((board[0][2] == board[2][2] == 1 or board[1][0] == board[1][1] == 1) and board[1][2] != 2):
    a = 1
    b = 0
  else:
    a = column-2
    b = -1*row+2

  O = turtle.Turtle()
  if board[-1*b+1][a+1] == 0:
    O.hideturtle()
    O.speed(100)
    O.pensize(5)
    O.up()
    O.goto(a*160,-50+b*160)
    time.sleep(0.5)
    O.down()
    O.circle(50)
    board[-1*b+1][a+1] = 2
  else:
    O.hideturtle()
    update_board_computer(board)

while True:
  update_board_player(board)
  if (board[0][0] == board[1][0] == board[2][0] == 1 or board[0][1] == board[1][1] == board[2][1] == 1 or board[0][2] == board[1][2] == board[2][2] == 1 or board[0][0] == board[0][1] == board[0][2] == 1 or board[1][0] == board[1][1] == board[1][2] == 1 or board[2][0] == board[2][1] == board[2][2] == 1 or board[0][0] == board[1][1] == board[2][2] == 1 or board[0][2] == board[1][1] == board[2][0] == 1):
    pw = turtle.Turtle()
    pw.up()
    pw.hideturtle()
    pw.speed("fastest")
    pw.goto(0,300)
    pw.down()
    pw.write("Congratulations, you won!", align = "center", font=("Times new roman", 24, "bold", "normal"))
    break
  if (board[0][0] != 0 and board[0][1] != 0 and board[0][2] != 0 and board[1][0] != 0 and board[1][1] != 0 and board[1][2] != 0 and board[2][0] != 0 and board[2][1] != 0 and board[2][2] != 0):
    draw = turtle.Turtle()
    draw.up()
    draw.hideturtle()
    draw.speed("fastest")
    draw.goto(0,300)
    draw.down()
    draw.write("It's a draw!", align = "center", font=("Times new roman", 24, "bold", "normal"))
    break
  update_board_computer(board)
  if (board[0][0] == board[1][0] == board[2][0] == 2 or board[0][1] == board[1][1] == board[2][1] == 2 or board[0][2] == board[1][2] == board[2][2] == 2 or board[0][0] == board[0][1] == board[0][2] == 2 or board[1][0] == board[1][1] == board[1][2] == 2 or board[2][0] == board[2][1] == board[2][2] == 2 or board[0][0] == board[1][1] == board[2][2] == 2 or board[0][2] == board[1][1] == board[2][0] == 2):
    cw = turtle.Turtle()
    cw.up()
    cw.hideturtle()
    cw.speed("fastest")
    cw.goto(0,300)
    cw.down()
    cw.write("You lost, better luck next time!", align = "center", font=("Times new roman", 24, "bold", "normal"))
    break
