import random

def show_tab(tab_9x9):
    k = 0
    print("      0     1     2  |  3     4     5  |  6     7     8")
    for i in range(0,9):
        if i == 0 or i == 3 or i == 6:
            print("   -----------------------------------------------------")
        print(k, " | ",tab_9x9[i][0], " | ", tab_9x9[i][1]," | ", tab_9x9[i][2]
        ," | ",tab_9x9[i][3], " | ", tab_9x9[i][4]," | ", tab_9x9[i][5]," | "
        ,tab_9x9[i][6], " | ", tab_9x9[i][7]," | ", tab_9x9[i][8])
        k+=1

def flatten(big_list):
    flat_list = []
    for sublist in big_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list


def import_game():

    tab = []
    temp = []
    big_tab = []
    final_grid = []
    with open('sudoku.txt', 'r') as f:
        for line in f:
            temp.append(line)



    k = 10
    del temp[0] # #Supprime le GRID (le 1er)
    del temp[k-1::k] #Supprime le GRID

    for string in temp:
        big_tab.append(string[:-1]) # Supprime le saut de ligne

    first_el = random.randint(0, 49)
    random_grid = big_tab[first_el*9:first_el*9+9]


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

def test():
    tab = [[0,0,3,0,2,0,6,0,0],
    [9,0,0,3,0,5,0,0,1],
    [0,0,1,8,0,6,4,0,0],
    [0,0,8,1,0,2,9,0,0],
    [7,0,0,0,0,0,0,0,8],
    [0,0,6,7,0,8,2,0,0],
    [0,0,2,6,0,9,5,0,0],
    [8,0,0,2,0,3,0,0,9],
    [0,0,5,0,1,0,3,0,0]]
    return tab

tab = test()
show_tab(tab)
