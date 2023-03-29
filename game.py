import pygame
import random
import time

pygame.init()

# Pixel variables
WIN_width = 400
WIN_height = 350
PLAY_width = 150
PLAY_height = 300
square_edge = 15
PLAY_LOC_X = (WIN_width - PLAY_width) // 2
PLAY_LOC_Y = (WIN_height - PLAY_height)
next_shape_x = 25
next_shape_y = 75

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
DARK_GRAY = (100,100,100)
LIGHT_GRAY = (180,180,180)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (80,80,255)
PURPLE = (200,0,200)
YELLOW = (200,200,0)

# Shapes, 7 shapes in total (s,z,i,o,j,l,t)

S = [['00000',
      '00000',
      '00110',
      '01100',
      '00000'],
     ['00000',
      '00100',
      '00110',
      '00010',
      '00000']]  # 2 STATUSES

Z = [['00000',
      '00000',
      '01100',
      '00110',
      '00000'],
     ['00000',
      '00100',
      '01100',
      '01000',
      '00000']]  # 2 STATUSES

I = [['00000',
      '00100',
      '00100',
      '00100',
      '00100'],
     ['00000',
      '11110',
      '00000',
      '00000',
      '00000']]  # 2 STATUSES

O = [['00000',
      '00000',
      '01100',
      '01100',
      '00000']]  # 1 STATUS

J = [['00000',
      '01000',
      '01110',
      '00000',
      '00000'],
     ['00000',
      '00110',
      '00100',
      '00100',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '00010',
      '00000'],
     ['00000',
      '00100',
      '00100',
      '01100',
      '00000']]  # 4 STATUSES

L = [['00000',
      '00010',
      '01110',
      '00000',
      '00000'],
     ['00000',
      '00100',
      '00100',
      '00110',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '01000',
      '00000'],
     ['00000',
      '01100',
      '00100',
      '00100',
      '00000']]  # 4 STATUSES

T = [['00000',
      '00100',
      '01110',
      '00000',
      '00000'],
     ['00000',
      '00100',
      '00110',
      '00100',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '00100',
      '00000'],
     ['00000',
      '00100',
      '01100',
      '00100',
      '00000']]  # 4 STATUSES

list_of_shapes = [T, L, J, O, I, Z, S]  # 7
list_of_colors = [WHITE, DARK_GRAY, RED, YELLOW, PURPLE, GREEN, BLUE]  # 7

class Shape():  # Creating a Shape class for fundamental variables of shapes

    def __init__(self, width, height, shape_code):
        self.width = width
        self.height = height
        self.shape_code = shape_code
        self.color = list_of_colors[list_of_shapes.index(shape_code)]
        self.status = 0

def create_playground(color_dict):  # Creating playground matrix and send color info to relevant elements of the matrix
    playground_matrix = [[BLACK for _ in range(10)] for _ in range(20)]  # Creating row and columns, for '_'s thanks to gulb

    for column in range(len(playground_matrix)):
        for row in range(len(playground_matrix[column])):  # Get the index
            if (row, column) in color_dict:
                key = color_dict[(row, column)]  # Get color key from the dict
                # print("========================")
                # print("column: ", column)
                # print("row: ", row)
                # print("========================")
                playground_matrix[column][row] = key  # Set the color of this index (BLACK is default)
    
    return playground_matrix

def draw_playground(WIN, playground_matrix):
    for column in range(len(playground_matrix)):
        pygame.draw.line(WIN, LIGHT_GRAY, (PLAY_LOC_X, PLAY_LOC_Y + column * square_edge), 
                         (PLAY_LOC_X + PLAY_width, PLAY_LOC_Y + column * square_edge))
        for row in range(len(playground_matrix[column])):  # Get the index
            pygame.draw.line(WIN, LIGHT_GRAY, (PLAY_LOC_X + row * square_edge, PLAY_LOC_Y), 
                         (PLAY_LOC_X + row * square_edge, PLAY_LOC_Y + PLAY_height))



def draw_WIN(WIN, playground_matrix):
    WIN.fill(BLACK)  # Get a black screen

    # print("=================================")
    # print("column: ", len(playground_matrix))
    # print("row: ", len(playground_matrix[1]))
    # print("=================================")

    for column in range(len(playground_matrix)):
        for row in range(len(playground_matrix[column])):  # Get the index
            pygame.draw.rect(WIN, playground_matrix[column][row], 
                             (PLAY_LOC_X + row * square_edge, PLAY_LOC_Y + column * square_edge, square_edge, square_edge), 0)
            pygame.draw.rect(WIN, (DARK_GRAY), (PLAY_LOC_X, PLAY_LOC_Y, PLAY_width, PLAY_height), 3)  # Draw playground borders
    
    draw_playground(WIN, playground_matrix)

def get_random_shape():  # Get a random shape from the list_of_shapes
    return Shape(5, 0, random.choice(list_of_shapes))

def next_shape_status(shape):
    positions = []
    form = shape.shape_code[shape.status % len(shape.shape_code)]

    for i, line in enumerate(form):
        row = list(line)
        for j, column in enumerate(row):
            if column == '1':
                positions.append((shape.width + j, shape.height + i))

    for i, position in enumerate(positions):
        positions[i] = (position[0] - 2, position[1] - 4)  # try without -2 and -4

    return positions

def display_next_shape(WIN, shape):
    form = shape.shape_code[shape.status % len(shape.shape_code)]
    # print("=============================")
    # print(form)
    # print("=============================")
    # time.sleep(.5)

    for i, line in enumerate(form):
        row = list(line)
        for j, column in enumerate(row):
            if column == '1':  #flag
                #print("i saw a rect!")
                pygame.draw.rect(WIN, shape.color, (next_shape_x + j * square_edge, next_shape_y + i * square_edge, square_edge, square_edge), 0)
                #pygame.draw.rect(WIN, shape.color, (next_shape_x, next_shape_y, square_edge, square_edge), 0)

def valid_space(shape, playground_matrix):
    valid_pos = [[(j,i) for j in range(10) if playground_matrix[i][j] == BLACK] for i in range(20)]
    valid_pos = [j for a in valid_pos for j in a]  # Overriding to 1-dimensional list

    formed = next_shape_status(shape)

    for pos in formed:
        if pos not in valid_pos:
            if pos[1] > -1:  # related with 'positions[i] = (position[0] - 2, position[1] - 4)'
                return False
    return True

def handle_full_row(playground_matrix, l):
    increment = 0
    for i in range(len(playground_matrix) - 1, -1, -1):
        row = playground_matrix[i]
        if (0,0,0) not in row:  # if no black in row
            increment += 1
            index = i
            for j in range(len(row)):
                try:
                    del l[(j,i)]
                except:
                    continue

    # shifting upper row (like LIFO)
    if increment > 0:
        for key in sorted(list(l), key = lambda x: x[1])[::-1]:  #get 'l' sorted with lambda and reverse
            # if not reversed upper rows will overwrite the lower ones
            x, y = key
            if y < index:
                new_key = (x, y + increment)
                l[new_key] = l.pop(key)



def is_lost(positions):
    for position in positions:
        height = position[1]
        if height < 1:
            return True
    
    return False