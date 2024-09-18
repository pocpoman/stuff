x = int(input("enter x position: ")) 
y = int(input("enter y position: ")) 
previous_y = 0
previous_x = 0
top_border = input("enter top borders: ").split(',')
for i in range(0,len(top_border)):
    top_border[i] = int(top_border[i])
bottom_border = [-1,-1]
x_adder = 1
y_adder = 1
board = []

def create():
    
    for m in range(0,top_border[1]):
        screen[f'{m}'] = []
    
    for i in range(0,top_border[1]):
        for l in range(0,top_border[0]):
            screen[f'{i}'].append(0)
         
        
        
        
        
        
        

screen = {
    
}
create()

def display(x,y):
    

    screen[f"{previous_y}"][previous_x] = 0
    screen[f'{y}'][x] = 1
    
    for i in screen:
        print(screen[i])
    
    
while True:

    input("")
    print(x,y)
    display(x,y)
    previous_y = y
    previous_x = x
    
    
    if x >= top_border[0]-1 or x <= bottom_border[0]-1:
        x_adder = x_adder * -1

    if y >= top_border[1] -1 or y <= bottom_border[1]-1:
        y_adder = y_adder * -1

    x += x_adder
    y += y_adder