import copy

def init():
    tab = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".","."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".",".","."],
            [".", ".", ".", "#", "#", ".", "#", "#", "#", "#", "#", "#", ".",".","."],
            [".", ".", ".", "#", "#", ".", "#", "#", "#", "#", "#", "#", ".", ".","."],
            [".", ".", ".", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".","."],
            [".", ".", ".", "#", "#", ".", ".", ".", ".", ".", "#", "#", ".", ".","."],
            [".", ".", ".", "#", "#", ".", ".", ".", ".", ".", "#", "#", ".", ".","."],
            [".", ".", ".", "#", "#", ".", ".", ".", ".", ".", "#", "#", ".",".","."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", ".", ".","."],
            [".", ".", ".", "#", "#", "#", "#", "#", "#", ".", "#", "#", ".",".","."],
            [".", ".", ".", "#", "#", "#", "#", "#", "#", ".", "#", "#", ".",".","."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".","."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".","."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]

    return tab


def print_tab(tab) :

    for i in range (0, len(tab)) :
        string = ""
        for j in range (0, len(tab[i])) :
            string += tab[i][j]
        print(string)



def life_game(tab):

    new_tab = copy.deepcopy(tab)

    for i in range(0, len(tab)):
        for j in range(0, len(tab)):

            is_alive = get_nb_cellule_alive(i, j, tab)

            cellule = tab[i][j]


            if cellule == "#":
                if is_alive == 2 or is_alive == 3:
                    new_cellule = "#"
                else :
                    new_cellule = "."
            else :
                if is_alive == 3:
                    new_cellule = "#"
                else :
                    new_cellule = "."

            new_tab[i][j] = new_cellule

    return new_tab



def get_nb_cellule_alive(i, j, tab):

    min_range_i, max_range_i, min_range_j, max_range_j = get_range(i,j, tab)

    is_alive= 0


    for a in range (min_range_i, max_range_i):
        for b in range (min_range_j, max_range_j):
            if 0<=a<len(tab) and 0 <=b<len(tab[0]):
                if a != i or b != j :
                    if tab[a][b] == "#":
                        is_alive += 1

    return is_alive





def get_range(i,j, tab):

    if i == 0 :
        min_range_i = 0
        max_range_i = 2
    elif i == 14:
        min_range_i = 13
        max_range_i = 15
    else :
        min_range_i = i-1
        max_range_i = i+2

    if j == 0:
        min_range_j = 0
        max_range_j = 2
    elif j == 14:
        min_range_j = 13
        max_range_j = 15
    else:
        min_range_j = j-1
        max_range_j = j+2

    return min_range_i, max_range_i, min_range_j, max_range_j
