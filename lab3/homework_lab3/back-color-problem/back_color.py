from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    list_text =["blue","red","yellow","green"]
    list_text_color =["#3F51B5","#C62828","#FFD600","#4CAF50"]             
    n = randint(0,len(list_text)-1)   
    m = randint(0,len(list_text_color)-1)
    quiz_type = randint(0,1)
    return [
                list_text[n],
                list_text_color[m],
                quiz_type # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
  if quiz_type == 0:     
    if shapes[0]["rect"][0] <= x & x <= shapes[0]["rect"][0] + shapes[0]["rect"][2]:
        if shapes[0]["rect"][1] <= y & y <= shapes[0]["rect"][1]+ shapes[0]["rect"][3]:
            if text == "blue": 
                return True
            else: 
                return False
    if shapes[1]["rect"][0] <= x & x <= shapes[1]["rect"][0] + shapes[1]["rect"][2]:
        if shapes[1]["rect"][1] <= y & y <= shapes[1]["rect"][1]+ shapes[1]["rect"][3]:
            if text == "red": 
                return True
            else: 
                return False
    if shapes[2]["rect"][0] <= x & x <= shapes[2]["rect"][0] + shapes[2]["rect"][2]:
        if shapes[2]["rect"][1] <= y & y <= shapes[2]["rect"][1]+ shapes[2]["rect"][3]:
            if text == "yellow": 
                return True
            else: 
                return False        
    if shapes[3]["rect"][0] <= x & x <= shapes[3]["rect"][0] + shapes[3]["rect"][2]:
        if shapes[3]["rect"][1] <= y & y <= shapes[3]["rect"][1]+ shapes[3]["rect"][3]:
            if text == "green": 
                return True
            else: 
                return False 
  if quiz_type ==1:

    if shapes[0]["rect"][0] <= x & x <= shapes[0]["rect"][0] + shapes[0]["rect"][2]:
        if shapes[0]["rect"][1] <= y & y <= shapes[0]["rect"][1]+ shapes[0]["rect"][3]:
            if color == "#3F51B5": 
                return True
            else: 
                return False
    if shapes[1]["rect"][0] <= x & x <= shapes[1]["rect"][0] + shapes[1]["rect"][2]:
        if shapes[1]["rect"][1] <= y & y <= shapes[1]["rect"][1]+ shapes[1]["rect"][3]:
            if color == "#C62828": 
                return True
            else: 
                return False
    if shapes[2]["rect"][0] <= x & x <= shapes[2]["rect"][0] + shapes[2]["rect"][2]:
        if shapes[2]["rect"][1] <= y & y <= shapes[2]["rect"][1]+ shapes[2]["rect"][3]:
            if color == "#FFD600": 
                return True
            else: 
                return False        
    if shapes[3]["rect"][0] <= x & x <= shapes[3]["rect"][0] + shapes[3]["rect"][2]:
        if shapes[3]["rect"][1] <= y & y <= shapes[3]["rect"][1]+ shapes[3]["rect"][3]:
            if color == "#4CAF50": 
                return True
            else: 
                return False                                               