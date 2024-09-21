import random
import time 
import sys
x = 0
z = 0
memory = []
colors = ["red","blue","green","yellow","purple"]


def choose_next(memory):
    current_color = random.randrange(0,len(colors))
    
    memory.append(colors[current_color])
    
def move_caret_up(n):
    # Move the caret up by n lines
    
    sys.stdout.write(f"\033[{n}A")
    for i in range(0,n):
        print("                                                                                                             ")
    sys.stdout.write(f"\033[{n}A")
 
    
    
        
while x < 10:
    choose_next(memory)
    
    for i in range(0,len(memory)):
        print(memory[i])
        time.sleep(1)
        move_caret_up(1)
        print("                                               ")
        move_caret_up(1)
        
    print() 
    for n in range(0,len(memory)):
        attempt = input("enter color: ")   

        if attempt != memory[n]:
            print("failed")
            exit()
    
    move_caret_up(2+len(memory))
    print()
    x += 1 
    z = 0
    
    
    
    
    
