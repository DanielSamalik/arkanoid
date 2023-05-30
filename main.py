import random

def desk_hit(cd, cb):
    desk = (cd[2]-cd[0])/2 + cd[0]
    if cb[2] <= desk:
        return [-d,-d]
    elif desk <= cb[0]:
        return [d,-d]
    elif cb[0] < desk and desk< cb[2]:
        return [0,-d]

def starter(e):
    global x
    canvas.delete(text)
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if desk in zoz:
        x = e.x
        ball_move()
def destroy_brick():
    global movement
    coords = canvas.coords(ball)
    items_list = canvas.find_overlapping(coords[0],coords[1],coords[2],coords[3])
    for i in items_list:
        if i in bricks:
            coord_brick = canvas.coords(i)
            if coord_brick[3] == coords[1]:
                bricks.remove(i)
                canvas.delete(i)
                movement[1] *= -1
            if coord_brick[2] == coords[0]:
                bricks.remove(i)
                canvas.delete(i)
                movement[0] *= (-1)
            if coord_brick[0] == coords[2]:
                bricks.remove(i)
                canvas.delete(i)
                movement[0] *= (-1)
            if coord_brick[1] == coords[3]:
                bricks.remove(i)
                canvas.delete(i)
                movement[1] *= -1
def ball_move():
    global movement
    canvas.move(ball,movement[0],movement[1])
    coords = canvas.coords(ball)
    coord_desk = canvas.coords(desk)
    destroy_brick()
    if ball in canvas.find_overlapping(coord_desk[0],coord_desk[1],coord_desk[2],coord_desk[3]):
        movement = desk_hit(coord_desk,coords)
    if coords[0] < 0:
        movement[0] *= (-1)
    if coords[1] < 0:
        movement[1] *= (-1)
    if coords[2] > w:
        movement[0] *= (-1)
    if coords[3] > h:
        canvas.delete("all")
        text = canvas.create_text(w/2,h/2, text="PREHRAL SI", fill="white")
    if len(bricks) == 0:
        canvas.configure(bg="black")
        canvas.delete("all")
        text = canvas.create_text(w/2,h/2, text="VYHRAL SI", fill="white")
        status = False
    canvas.after(35, ball_move)

def mover(e):
    global x
    if x != 0:
        mouse = e.x - x
        canvas.move(desk, mouse, 0)
        x = e.x



def prepare_bricks():
    for y in range(brick_count_y):
        for x in range(w//brick_w):
            bricks.append(canvas.create_rectangle(x*brick_w,y*brick_h,x*brick_w+brick_w, y*brick_h+brick_h, fill=colours[y%brick_count_y],  width=5, outline="black"))

colours = ["red", "blue", "green","yellow", "orange", "brown"]

import tkinter as tk

win = tk.Tk()

w = 650
h = 450

canvas = tk.Canvas(width = w, height = h, bg = "black")
canvas.pack()

d=5
movement = [1*d,1*d]

brick_w = 65
brick_h = 20
brick_count_x = 10
brick_count_y = len(colours)
bricks = []

ball = canvas.create_oval(w/2-20,h/2-20,w/2,h/2, fill="purple")
text = canvas.create_text(w/2,h/2+30,text="ZAČNI HRAŤ", fill="white")
desk = canvas.create_rectangle(w/2-50, h-20, w/2+50, h, fill="turquoise")

prepare_bricks()

canvas.bind("<Button-1>", starter)
canvas.bind("<B1-Motion>", mover)


win.mainloop()