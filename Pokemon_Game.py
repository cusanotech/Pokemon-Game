# juego de pikachu:
import random

def pokemon_game():
    # Definimos la vida de los pokemones
    hp_pikachu = 100
    hp_jiggypuff = 100      

    # Definimos el turno, el cual será aleatorio:
        # 1 Jigglypuff and 0 pikachu
    turn = random.randint(0, 1)

    print('Pikachu HP           : ' + str(hp_pikachu))
    print('Jigglypuff HP        : ' + str(hp_jiggypuff) )


    print('\t\n############# QUE COMIENCE EL JUEGO #############')
    # Entramos en combate
    while hp_pikachu > 0 and hp_jiggypuff > 0:

        # Esta partida esta arreglada (al menos le estamos dando ventaja a Pikachu)xD
        attack_pikachu = random.randint(0, 55)
        attack_jigglypuff = random.randint(0, 45)

        if turn == 1:
            print('\nTURN: ## JIGGLYPUUF ##')
            print('Pikachu HP           : ' + str(hp_pikachu) + ' HP')
            hp_pikachu -= attack_jigglypuff
            print('Jigglypuff attack    : -' + str(attack_jigglypuff))
            print('Pikachu HP           : ' + str(hp_pikachu))
            turn = 0

        else:
            print('\nTURN: ## PIKACHU ##')
            print('Jigglypuuf HP        : ' + str(hp_jiggypuff) + ' HP')
            hp_jiggypuff -= attack_pikachu
            print('Pikachu attack       : -' + str(attack_pikachu))
            print('Jigglypuff HP        : ' + str(hp_jiggypuff))
            turn = 1

    # Salimos del ciclo cuando la vida de uno de los 2 sea menor o igual a 0
    if hp_pikachu <= 0:
        win = '\n\t JIGGLYPUUF IS THE WINNER'
    else:
        win = '\n\t PIKACHU IS THE WINNER'

    print(win)

pokemon_game()