from turtle import *
def draw_square(length,colors):
    color(colors)
    for i in range(4):
        forward(length)
        left(90)
# colors="red"
# length = 100
# m = draw_square(length,colors)  
# mainloop()