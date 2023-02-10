import pgzrun
WIDTH = 640
# A box with 50,50 as x,y coordinates, (100,100) as width and height
box = Rect((50,50), (100,100))
box2 = Rect((150,150), (130,30))

def draw():
    screen.fill('white') # white background
    screen.draw.filled_rect(box, 'red') # Red box
    screen.draw.filled_rect(box2, 'blue') # Blue box

def update():
    #check for boundary
    if box.x > 640:
        box.x = 0 
    box.x += 3    
# moves box 3 pixels to the right every frame            

pgzrun.go()    
