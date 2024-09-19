import time
import sys

previous_y = 0
previous_x = 0
top_border = input("enter top borders: ").split(',')
x = int(input("enter x position: ")) 
y = int(input("enter y position: ")) 

for i in range(0,len(top_border)):
    top_border[i] = int(top_border[i])

bottom_border = [0,0]
x_adder = int(input("enter x gradient: ")) * -1
y_adder = int(input("enter y gradient: ")) * -1
board = []
screen = {}

def create():
    
    for m in range(0,top_border[1]):
        screen[f'{m}'] = []
    
    for i in range(0,top_border[1]):
        for l in range(0,top_border[0]):
            screen[f'{i}'].append(" ")
         
def move_caret_up(n):
    # Move the caret up by n lines
    sys.stdout.write(f"\033[{n}A")

def display(x,y):
    
    screen[f"{previous_y}"][previous_x] = " "
    screen[f'{y}'][x] = "o"
    
    for i in screen:
        print(screen[i])
    move_caret_up(len(screen))

def _main_():
    create()

    while True:

        time.sleep(0.01)

        display(x,y)
        previous_y = y
        previous_x = x

        if x >= top_border[0]-1 or x <= bottom_border[0]:
            x_adder = x_adder * -1
        if y >= top_border[1]-1 or y <= bottom_border[1]:
            y_adder = y_adder * -1

        x += x_adder
        y += y_adder

_main_()