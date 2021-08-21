import pygame
import random
import copy

#base
matrix = ['', '', '', '', '', '', '', '', ''] 

#initialize pygame
pygame.init()                       #IMPORTANT

#box of the game
window = pygame.display.set_mode((600, 750))        #(x, y)

#title and icon
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load('tic-tac-toe.png')   #32 pixel
pygame.display.set_icon(icon)

#board
boardIMG = pygame.image.load('board.png')

#players icon
player1IMG = pygame.image.load('Player 1.png')
player2IMG = pygame.image.load('Player 2.png')

#computer icon
computerIMG = pygame.image.load('computer.png')

#score
score1 = 0
score2 = 0
font2 = pygame.font.SysFont('timesnewroman', 60, True)
def display_score(x, y, score_value):
    score = font2.render(': ' + str(score_value), True, (255, 255, 255))
    window.blit(score, (x, y))

#buttons
class option():
    def __init__(self, color, x, y, width, height, font_size):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size

    def draw(self, window, str = '', border = None):
        #Call this method to draw the button on the screen

        if border:
            pygame.draw.rect(window, border, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            #pygame.draw.rect(Surface, color, Rect, width=0)
        pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
        
        if str != '':
            font = pygame.font.SysFont('verdana', self.font_size)
            text = font.render(str, True, (0,0,0))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates

        if pos[0] > self.x and pos[0] < self.x + self.width and pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

# X's and O's
font = pygame.font.SysFont('verdana', 170, True)
def X_O(x, y, str):
    xo = font.render(str, True, (255, 255, 255))
    window.blit(xo, (x, y))
print_coordinates = [(30, 0), (230, 0), (425, 0), (30, 195), (230, 195), (425, 195), (30, 390), (230, 390), (425, 390)]
x_range = [(0, 190), (225, 378), (412, 600)]
y_range = [(0, 192), (225, 380), (415, 600)]    #almost same as x_range tho

def draw_line(x_start, y_start, x_end, y_end):
    pygame.time.wait(400)
    pygame.draw.line(window, (0, 0, 0), (x_start, y_start), (x_end, y_end), width = 20)
    pygame.display.update()
    pygame.time.wait(1000)

#win 
def win(matrix):
    global score1, score2
    i = 0
    for j in range(3):
        if matrix[i] != '' and matrix[i] == matrix[i + 1] and matrix[i + 1] == matrix[i + 2]:        #horizontal
            if j == 0:
                draw_line(5, 96, 595, 96)
            elif j == 1:
                draw_line(5, 305, 595, 305)
            else:
                draw_line(5, 510, 595, 510)
                
            if matrix[i] == 'X':
                score1 += 1
                finish.draw(window, 'Player 1 Won', (255, 255, 255))
                pygame.display.update()
                pygame.time.wait(1000)
            elif matrix[i] == 'O':
                score2 += 1
                finish.draw(window, 'Player 2 Won', (255, 255, 255))
                pygame.display.update()
                pygame.time.wait(1000)
            return True
        i = i + 3

    for j in range(3):
        if matrix[j] != '' and matrix[j] == matrix[j + 3] and matrix[j + 3] == matrix[j + 6]:        #vertical
            if j == 0:
                draw_line(94, 5, 94, 595)
            elif j == 1:
                draw_line(301, 5, 301, 595)
            else:
                draw_line(507, 5, 507, 595)

            if matrix[j] == 'X':
                score1 += 1
                finish.draw(window, 'Player 1 Won', (255, 255, 255))
                pygame.display.update()
                pygame.time.wait(1000)
            elif matrix[j] == 'O':
                score2 += 1
                finish.draw(window, 'Player 2 Won', (255, 255, 255))
                pygame.display.update()
                pygame.time.wait(1000)
            return True

    if matrix[0] != '' and matrix[0] == matrix[4] and matrix[4] == matrix[8]:    #diagonal 1
        draw_line(0, 0, 600, 600)
        if matrix[4] == 'X':
            score1 += 1
            finish.draw(window, 'Player 1 Won', (255, 255, 255))
            pygame.display.update()
            pygame.time.wait(1000)
        elif matrix[4] == 'O':
            score2 += 1
            finish.draw(window, 'Player 2 Won', (255, 255, 255))
            pygame.display.update()
            pygame.time.wait(1000)
        return True
    elif matrix[2] != '' and matrix[2] == matrix[4] and matrix[4] == matrix[6]:    #diagonal 2
        draw_line(600, 0, 0, 600)
        if matrix[4] == 'X':
            score1 += 1
            finish.draw(window, 'Player 1 Won', (255, 255, 255))
            pygame.display.update()
            pygame.time.wait(1000)
        elif matrix[4] == 'O':
            score2 += 1
            finish.draw(window, 'Player 2 Won', (255, 255, 255))
            pygame.display.update()
            pygame.time.wait(1000)
        return True
        
    return False

#draw
def draw(matrix):           #when the matrix is full
    for i in matrix:
        if i == '':
            return False
    finish.draw(window, 'DRAW!', (255, 255, 255))
    pygame.display.update()
    pygame.time.wait(1000)
    return True

def find_win(matrix):
    for i in [0, 3, 6]:         #horizontal
        index = -1
        count = 0
        k = i
        for j in range(3):
            if matrix[k] == 'O':
                count = count + 1
            elif matrix[k] == '':
                index = k
            k = k + 1
        if count == 2 and index != -1:
            matrix[index] = 'O'
            return True

    for i in range(3):         #vertical
        index = -1
        count = 0
        k = i
        for j in range(3):
            if matrix[k] == 'O':
                count = count + 1
            elif matrix[k] == '':
                index = k
            k = k + 3
        if count == 2 and index != -1:
            matrix[index] = 'O'
            return True

    index = -1
    count = 0
    for i in [0, 4, 8]:         #diagonal 1
        if matrix[i] == 'O':
            count = count + 1
        elif matrix[i] == '':
            index = i
    if count == 2 and index != -1:
        matrix[index] = 'O'
        return True

    index = -1
    count = 0
    for i in [6, 4, 2]:         #diagonal 2
        if matrix[i] == 'O':
            count = count + 1
        elif matrix[i] == '':
            index = i
    if count == 2 and index != -1:
        matrix[index] = 'O'
        return True
        
    return False

def find_save(matrix):
    for i in [0, 3, 6]:         #horizontal
        index = -1
        count = 0
        k = i
        for j in range(3):
            if matrix[k] == 'X':
                count = count + 1
            elif matrix[k] == '':
                index = k
            k = k + 1
        if count == 2 and index != -1:
            matrix[index] = 'O'
            return True

    for i in range(3):         #vertical
        index = -1
        count = 0
        k = i
        for j in range(3):
            if matrix[k] == 'X':
                count = count + 1
            elif matrix[k] == '':
                index = k
            k = k + 3
        if count == 2 and index != -1:
            matrix[index] = 'O'
            return True

    index = -1
    count = 0
    for i in [0, 4, 8]:         #diagonal 1
        if matrix[i] == 'X':
            count = count + 1
        elif matrix[i] == '':
            index = i
    if count == 2 and index != -1:
        matrix[index] = 'O'
        return True

    index = -1
    count = 0
    for i in [6, 4, 2]:         #diagonal 2
        if matrix[i] == 'X':
            count = count + 1
        elif matrix[i] == '':
            index = i
    if count == 2 and index != -1:
        matrix[index] = 'O'
        return True
        
    return False

def find_GoodMove(matrix):
    l = []
    for i in range(9):
        if matrix[i] == '':
            l.append(i)

    l_copy = copy.deepcopy(l)
    greater_win = 0
    good_indexes = []

    while l:
        ind = l.pop()
        matrix[ind] = 'O'
        win = 0
        
        for i in [0, 3, 6]:         #horizontal
            index = -1
            count = 0
            k = i
            for j in range(3):
                if matrix[k] == 'O':
                    count = count + 1
                elif matrix[k] == '':
                    index = k
                k = k + 1
            if count == 2 and index != -1:
                win = win + 1

        for i in range(3):         #vertical
            index = -1
            count = 0
            k = i
            for j in range(3):
                if matrix[k] == 'O':
                    count = count + 1
                elif matrix[k] == '':
                    index = k
                k = k + 3
            if count == 2 and index != -1:
                win = win + 1

        index = -1
        count = 0
        for i in [0, 4, 8]:         #diagonal 1
            if matrix[i] == 'O':
                count = count + 1
            elif matrix[i] == '':
                index = i
        if count == 2 and index != -1:
            win = win + 1

        index = -1
        count = 0
        for i in [6, 4, 2]:         #diagonal 2
            if matrix[i] == 'O':
                count = count + 1
            elif matrix[i] == '':
                index = i
        if count == 2 and index != -1:
            win = win + 1
            
        matrix[ind] = ''
        if win > greater_win:
            greater_win = win
            good_indexes.clear()
            good_indexes.append(ind)
        elif win == greater_win:
            good_indexes.append(ind)

    if good_indexes:
        #print(greater_win)
        matrix[random.choice(good_indexes)] = 'O'
    else:
        matrix[random.choice(l_copy)] = 'O'

#setting images
running = True
start_game = 0
#for center: x-coordinate = center of width of window - width of button/2, y-coordinate = center of height of window - height of button/2
vs_player = option((135,206,235), 150, 405, 300, 100, 60)
vs_computer = option((135,206,235), 150, 245, 300, 100, 60)
finish = option((135,206,235), 50, 250, 500, 100, 60)
boxes = [option((255, 128, 255), 0, 0, 190, 193, 120), option((255, 128, 255), 225, 0, 154, 193, 120), option((255, 128, 255), 412, 0, 190, 193, 120), option((255, 128, 255), 0, 225, 190, 157, 120), option((255, 128, 255), 225, 225, 154, 157, 120), option((255, 128, 255), 412, 225, 190, 157, 120), option((255, 128, 255), 0, 415, 190, 185, 120), option((255, 128, 255), 225, 415, 154, 185, 120), option((255, 128, 255), 412, 415, 190, 185, 120)]

#game loop
current = 0
while running:
    pos = pygame.mouse.get_pos()
    #print(pos)
    window.fill((255, 128, 255))         #RGB value (mint green) (in case u don't want any background image, u can colour background using this)

    #turns
    if current%2 == 0:
        turn = 'X'
    else:
        turn = 'O'
        if start_game == 1:
            if not find_win(matrix):
                if not find_save(matrix):
                    find_GoodMove(matrix)
            current = current + 1
            pygame.time.wait(500)

    #input
    for input in pygame.event.get():    #Here, event detects any input
        #quit
        if input.type == pygame.QUIT:
            running = False

        #mouse click
        if input.type == pygame.MOUSEBUTTONDOWN:
            if start_game:
                for i in range(9):
                    if boxes[i].isOver(pos) and matrix[i] == '':
                        current = current + 1
                        matrix[i] = turn
            else:
                if vs_player.isOver(pos):
                    start_game = 2
                elif vs_computer.isOver(pos):
                    start_game = 1
        
        #mouse hovering
        if start_game == 0 and input.type == pygame.MOUSEMOTION:
            if vs_player.isOver(pos):
                vs_player.color = (0, 0, 139)
            else:
                vs_player.color = (135, 206, 235)
            if vs_computer.isOver(pos):
                vs_computer.color = (0, 0, 139)
            else:
                vs_computer.color = (135, 206, 235)
    
    #Start Screen
    if start_game > 0:
        window.blit(boardIMG, (0, 0))
        for i in range(9):
            boxes[i].draw(window, matrix[i])

        window.blit(player1IMG, (118, 660))
        if start_game == 2:
            window.blit(player2IMG, (418, 660))
        else:
            window.blit(computerIMG, (418, 660))
    else:
        #start_option.draw(window, 'Play', (255, 255, 255))
        vs_player.draw(window, '2 Players', (255, 255, 255))
        vs_computer.draw(window, '1 Player', (255, 255, 255))

    #score
    if start_game > 0:
        display_score(185, 660, score1)
        display_score(485, 660, score2)

    pygame.display.update() #IMPORTANT

    if win(matrix) or draw(matrix):
        matrix = ['', '', '', '', '', '', '', '', '']  #resets the board
