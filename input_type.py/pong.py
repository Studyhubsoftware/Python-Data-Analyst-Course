import pgzrun

WIDTH=800
HEIGHT=500

box_red= Rect((10,10), (20,60))
box_blue=Rect((WIDTH-30,10),(20,60))
ball= Rect((WIDTH/2,HEIGHT/2),(20,20))
brs,bbs,bs=5,6,(10,10)

def draw():
    screen.fill("white")
    screen.draw.filled_rect(box_red,'red')
    screen.draw.filled_rect(box_blue,'blue')
    screen.draw.filled_rect(ball,'black')


def update():
    global brs,bbs,bs
    brs=move_vertically(box_red,brs)
    bbs=move_vertically(box_blue,bbs)
    bs=move_ball(ball,bs)
        
