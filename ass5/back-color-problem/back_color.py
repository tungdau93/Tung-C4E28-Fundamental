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

def check_point(x, y):
    if x[0] in range(y[0],y[0]+y[2]) and x[1] in range(y[1],y[1]+y[3]):
        return True
    else:
        return False

def get_shapes():
    return shapes


def generate_quiz():
    return [
                'RED',
                '#4CAF50',
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    return True
