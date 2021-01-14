import random
global grid

global original_grid



def new_value(grid):
    try:
        user_input = input("Que voulez vous changer ? xy:valeur    : \n")
        user_input = user_input.split(":")
        temp = str(user_input[0])
        coo_x = temp[0]
        coo_y = temp[1]
        value = int(user_input[1])
        if value <= 0 or value > 9:
            print("Veuillez entrer des valeurs de 1 à 9 inclus")
            new_value(grid)
        grid[int(coo_y)][int(coo_x)] = value
    except:
        print("Erreur la donnée entrée n'a pas pu être enregistrée")
        new_value(grid)
    return grid

def show_grid(grid_9x9):
    k = 0
    print("      0     1     2  |  3     4     5  |  6     7     8")
    for i in range(0,9):
        if i == 0 or i == 3 or i == 6:
            print("   -----------------------------------------------------")
        print(k, " | ",grid_9x9[i][0], " | ", grid_9x9[i][1]," | ", grid_9x9[i][2]
        ," | ",grid_9x9[i][3], " | ", grid_9x9[i][4]," | ", grid_9x9[i][5]," | "
        ,grid_9x9[i][6], " | ", grid_9x9[i][7]," | ", grid_9x9[i][8])
        k+=1

def flatten(big_list):
    flat_list = []
    for sublist in big_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list


def import_game():

    grid = []
    temp = []
    big_grid = []
    final_grid = []
    with open('sudoku.txt', 'r') as f:
        for line in f:
            temp.append(line)
    k = 10
    del temp[0] # #Supprime le GRID (le 1er)
    del temp[k-1::k] #Supprime les autres grids

    for string in temp:
        big_grid.append(string[:-1]) # Supprime les sauts de ligne

    first_el = random.randint(0, 49)
    random_grid = big_grid[first_el*9:first_el*9+9]


    temp = []
    sublist = []
    for i in random_grid:
        for row in i:
            temp.append(row)
    for x in range(len(temp)):
        temp[x] = int(temp[x])

    return split(temp)

def split(grid):

    final_grid = []
    for i in range(0,9):

        final_grid.append(grid[i*9:i*9+9])

    return final_grid


def estpossible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False


    return True


def resoudre():

    global grid

    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if estpossible(y,x,n):
                        grid[y][x] = n
                        show_grid(grid)
                        resoudre()
# Dans le cas où je suis dans une impasse, grid[y][x] == 0 mais aucune valeur en n ne permet de valider la case
    incr_last_possible_value(y,x)
    show_grid(grid)


    return grid




def n_zero():
    compteur = 0
    for i in flatten(grid):
        if i == 0:
            compteur += 1
    return compteur

def donttouchthose():
    coo = []
    for y in range(0,9):
        for x in range(0,9):
            if original_grid[y][x] != 0:
                coo.append(str(y)+str(x))
    return coo

def incr_last_possible_value(y,x):
    list = donttouchthose()

    if x != 0:
        x -= 1
    elif x == 0 :
        if y == 0:
            print("Nous sommes en 0 0")
        else:
            y -= 1
            x = 8

    if (str(y) + str(x)) in list:
        incr_last_possible_value(y,x)
    n = grid[y][x]
    for i in range(1, 8):

        if n < 9:
            n += 1
            if estpossible(y,x, n):
                grid[y][x] = n

                resoudre()

        if n >= 9:
            incr_last_possible_value(y,x)
    print(y,x)

    incr_last_possible_value(y,x)



original_grid = [[0,0,3,0,2,0,6,0,0],
                 [9,0,0,3,0,5,0,0,1],
                 [0,0,1,8,0,6,4,0,0],
                 [0,0,8,1,0,2,9,0,0],
                 [7,0,0,0,0,0,0,0,8],
                 [0,0,6,7,0,8,2,0,0],
                 [0,0,2,6,0,9,5,0,0],
                 [8,0,0,2,0,3,0,0,9],
                 [0,0,5,0,1,0,3,0,0]]


grid =          [[0,0,3,0,2,1,6,0,0],
                 [9,0,0,3,0,5,0,0,1],
                 [0,0,1,8,0,6,4,0,0],
                 [0,0,8,1,0,2,9,0,0],
                 [7,0,0,0,0,0,0,0,8],
                 [0,0,6,7,0,8,2,0,0],
                 [0,0,2,6,0,9,5,0,0],
                 [8,0,0,2,0,3,0,0,9],
                 [0,0,5,0,1,0,3,0,0]]

resoudre()
show_grid(grid)

    # if y - 1 == -1:
    #     for i in donttouchthose():
    #             if y == 0:
    #                 if (str(y) + str(x-1)) in donttouchthose():
    #                     print(str(y) + str(x-1))
    #             if (str(y-1) + str(8)) == i:
    #                 print(str(y-1) + str(8))
    #                 if grid[y][x-1] > 9:
    #                     grid[y][x-1] = grid[y][x-1] + 1
    #                 elif grid[y][x-1] == 9:
    #                     incr_last_possible_value(y,x)
    # elif y - 1 != -1:
    #     for i in donttouchthose():
    #             if (str(y) + str(x-1)) == i:
    #                 if grid[y][x] > 9:
    #                     grid[y][x] = grid[y][x] + 1
    #                 elif grid[y][x] == 9:
    #                     incr_last_possible_value(y,x)
