import random
import copy

def win(matrix):
    i = 0
    for j in range(3):
        if matrix[i] != 0 and matrix[i] == matrix[i + 1] and matrix[i + 1] == matrix[i + 2]:        #horizontal
            if matrix[i] == 'X':
                print('Player 1 Won')
            elif matrix[i] == 'O':
                print('Player 2 Won')
            return True
        i = i + 3

    for j in range(3):
        if matrix[j] != 0 and matrix[j] == matrix[j + 3] and matrix[j + 3] == matrix[j + 6]:        #vertical
            if matrix[j] == 'X':
                print('Player 1 Won')
            elif matrix[j] == 'O':
                print('Player 2 Won')
            return True

    if (matrix[0] != 0 and matrix[0] == matrix[4] and matrix[4] == matrix[8]) or (matrix[2] != 0 and matrix[2] == matrix[4] and matrix[4] == matrix[6]):    #diagonal
        if matrix[4] == 'X':
            print('Player 1 Won')
        elif matrix[4] == 'O':
            print('Player 2 Won')
        return True
        
    return False

def draw(matrix):           #when the matrix is full
    for i in matrix:
        if i == 0:
            return False
    print("DRAW")
    return True        

def versus_player(matrix):  # 1v1
    current = 0
    while(not win(matrix) and not draw(matrix)):
        current = current + 1
        if current%2 != 0:
            turn = 'X'
            print()
            print('Player 1(X):')
        else:
            turn = 'O'
            print()
            print('Player 2(O):')
        x = int(input())
        if x < 1 or x > 9 or matrix[x - 1] != 0:

            print("Invalid Input")
            current = current - 1
            continue
        matrix[x - 1] = turn
        value = 0
        for i in [7, 8, 9, 4, 5, 6, 1, 2, 3]:
            value = value + 1
            if matrix[i - 1] != 0:
                print(matrix[i - 1], end = '')
            else:
                print(end = ' ')
            if value%3 != 0:
                print(end = ' | ')
            if value%3 == 0 and value != 9:
                print()
                print("---------")
        print()

def find_win(matrix):
    for i in [0, 3, 6]:         #horizontal
        index = -1
        count = 0
        k = i
        for j in range(3):
            if matrix[k] == 'O':
                count = count + 1
            elif matrix[k] == 0:
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
            elif matrix[k] == 0:
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
        elif matrix[i] == 0:
            index = i
    if count == 2 and index != -1:
        matrix[index] = 'O'
        return True

    index = -1
    count = 0
    for i in [6, 4, 2]:         #diagonal 2
        if matrix[i] == 'O':
            count = count + 1
        elif matrix[i] == 0:
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
            elif matrix[k] == 0:
                index = k
            k = k + 1
        if count == 2 and index != -1:
            #print('index(h): ', index)
            matrix[index] = 'O'
            return True

    for i in range(3):         #vertical
        index = -1
        count = 0
        k = i
        for j in range(3):
            if matrix[k] == 'X':
                count = count + 1
            elif matrix[k] == 0:
                index = k
            k = k + 3
        if count == 2 and index != -1:
            #print('index(v): ', index)
            matrix[index] = 'O'
            return True

    index = -1
    count = 0
    for i in [0, 4, 8]:         #diagonal 1
        if matrix[i] == 'X':
            count = count + 1
        elif matrix[i] == 0:
            index = i
    if count == 2 and index != -1:
        #print('index(d1): ', index)
        matrix[index] = 'O'
        return True

    index = -1
    count = 0
    for i in [6, 4, 2]:         #diagonal 2
        if matrix[i] == 'X':
            count = count + 1
        elif matrix[i] == 0:
            index = i
    if count == 2 and index != -1:
        #print('index(d2): ', index)
        matrix[index] = 'O'
        return True
        
    return False

def find_move(matrix):
    # if matrix == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
    #     matrix[random.randint(0, 8)] = 'O'
    # else:
    l = []
    for i in range(9):
        if matrix[i] == 0:
            l.append(i)
    matrix[random.choice(l)] = 'O'

def find_GoodMove(matrix):
    l = []
    for i in range(9):
        if matrix[i] == 0:
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
                elif matrix[k] == 0:
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
                elif matrix[k] == 0:
                    index = k
                k = k + 3
            if count == 2 and index != -1:
                win = win + 1

        index = -1
        count = 0
        for i in [0, 4, 8]:         #diagonal 1
            if matrix[i] == 'O':
                count = count + 1
            elif matrix[i] == 0:
                index = i
        if count == 2 and index != -1:
            win = win + 1

        index = -1
        count = 0
        for i in [6, 4, 2]:         #diagonal 2
            if matrix[i] == 'O':
                count = count + 1
            elif matrix[i] == 0:
                index = i
        if count == 2 and index != -1:
            win = win + 1
            
        matrix[ind] = 0
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


def versus_AI(matrix):
    current = 0
    print('First turn:')
    print('1: Yours')
    print('2: A.I.')
    y = int(input('Input: '))
    if y == 2:
        current = 1
    while(not win(matrix) and not draw(matrix)):
        current = current + 1
        if current%2 != 0:
            turn = 'X'
            print()
            print('Player 1(X):')
            x = int(input())
            if x < 1 or x > 9 or matrix[x - 1] != 0:
                print("Invalid Input")
                current = current - 1
                continue
            matrix[x - 1] = turn
        else:
            turn = 'O'
            print()
            print('A.I.(O):')
            if not find_win(matrix):
                if not find_save(matrix):
                    #find_move(matrix)      #prototype 1
                    find_GoodMove(matrix)   #prototype 2
        
        value = 0
        for i in [7, 8, 9, 4, 5, 6, 1, 2, 3]:
            value = value + 1
            if matrix[i - 1] != 0:
                print(matrix[i - 1], end = '')
            else:
                print(end = ' ')
            if value%3 != 0:
                print(end = ' | ')
            if value%3 == 0 and value != 9:
                print()
                print("---------")
        print()

def main():
    matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0]    #base of game
    value = 0
    for i in [7, 8, 9, 4, 5, 6, 1, 2, 3]:   #pattern on numpad keys
        value = value + 1
        print(i, end = '')
        if value%3 != 0:
            print(end = ' | ')
        if value%3 == 0 and value != 9:
            print()
            print("---------")
    print()
    inp = int(input('\nChoose one:\n1. 1 Player\n2. 2 Players\nInput: '))
    if inp == 2:
        versus_player(matrix)
    elif inp == 1:
        versus_AI(matrix)

if __name__=="__main__" :
    main()
