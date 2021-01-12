import random
global grid
global oldgrid
import sys

sys.setrecursionlimit(10**6)


def new_value(tab):
    try:
        user_input = input("Que voulez vous changer ? xy:valeur    : \n")
        user_input = user_input.split(":")
        temp = str(user_input[0])
        coo_x = temp[0]
        coo_y = temp[1]
        value = int(user_input[1])
        if value <= 0 or value > 9:
            print("Veuillez entrer des valeurs de 1 à 9 inclus")
            new_value(tab)
        tab[int(coo_y)][int(coo_x)] = value
    except:
        print("Erreur la donnée entrée n'a pas pu être enregistrée")
        new_value(tab)
    return tab

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
    temp = []
    l = 0
    # On vérifie les rows
    for i in grid[y]:
        if i == n:
            return False
    # On vérifie les colonnes
    for j in range(0,9):
        temp.append(grid[l][x])
        l+=1

    for p in temp:
        if n == p:
            return False
    return True


def resoudre():
    global grid


    r = list(range(1,10))
    random.shuffle(r)
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in r:
                    if estpossible(y,x,n):
                        grid[y][x] = n
                        resoudre()

        grid = oldgrid.copy()
        print(n_zero())


    return grid

def n_zero():
    compteur = 0
    for i in flatten(grid):
        if i == 0:
            compteur += 1
    return compteur




oldgrid = import_game()
grid = oldgrid.copy()
show_grid(resoudre())
