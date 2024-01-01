import fonctions

def main():

    tab = fonctions.init()

    fonctions.print_tab(tab)

    for i in range(0, 201):
        tab = fonctions.life_game(tab)

    print("")
    fonctions.print_tab(tab)


main()
