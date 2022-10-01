# VALORANT STRAT ROULETTE

import random

def VSR():
    print("\nWelcome to my Valorant Strat Roulette!")

    playing = input("\nDo you want to play? ").lower()
    if playing != 'yes':
        print('\nPlease input yes to continue next time.')
        quit()
    else:
        print("Okay! Let's play :)")

    agents = ["Yoru", "Viper", "Sova", "Skye", "Sage", "Reyna", "Raze", "Phoenix", "Omen", "Neon", "Killjoy", "KAYO", "Jett", "Fade", "Cypher", "Chamber", "Brimstone", "Breach", "Astra"]
    rand_agent = None

    map_2sites = ["Ascent", "Icebox", "Fracture", "Pearl", "Breeze", "Bind"]
    map_3sites = ["Haven"]
    map_choices = map_2sites + map_3sites

    strat_attack = ["rush B", "group attack A", "rush A", "group attack B", "go mid", "play for picks", "play default"]
    strat_attack2 = ["rush C", "go garage into C", "peek mid window", "rush B", "group attack A", "rush A",
                     "group attack B", "go mid", "play for picks", "play default"]
    strat_defense = ["play A", "play B", "watch mid", "flank the enemy", "stack any site"]
    strat_defense2 = ["play A", "play B", "play C", "watch mid window and grass", "flank the enemy", "stack any site", "rush to enemy spawn", "play garage"]
    
    countdown = 3

    player_agent = input("\nWould you like to generate a random agent? ").lower()
    if player_agent == 'yes':
        rand_agent = random.choice(agents)
        print("You must choose " + rand_agent + ".")
        print("Hope you liked your pick!")

    else:
        print('\nPlease input yes for random agent next time.')

    print('\nMaps:')
    print(map_choices)

    player_map = input("\nWhat map are you playing? ").title()
    if player_map in map_choices:
        print("Nice! " + player_map + " is a great map!")

    else:
        print("Oops! Please type one of the maps provided above next time.")
        quit()

    player_side = input("\nAre you on defense or attack? ").lower()
    if player_map in map_3sites:
        if player_side == "attack":
            print("Attacking is tough but you got this!")
            print("\nNow for the strat roulette! Let's hope your lucky!")
            while countdown >= 1:
                print(countdown)
                countdown -= 1

            print("\nStrat: " + random.choice(strat_attack2) + ".")
        
        elif player_side == "defense":
            print("Cool! Defense is considered to be the best side!")
            print("\nNow for the strat roulette! Let's hope your lucky!")
            while countdown >= 1:
                print(countdown)
                countdown -= 1

            print("\nStrat: " + random.choice(strat_defense2) + ".")

    elif player_side == "attack":
        print("Attacking is tough but you got this!")
        print("\nNow for the strat roulette! Let's hope your lucky!")
        while countdown >= 1:
            print(countdown)
            countdown -= 1

        print("\nStrat: " + random.choice(strat_attack) + ".")

    elif player_side == "defense":
        print("Cool! Defense is considered to be the best side!")
        print("\nNow for the strat roulette! Let's hope your lucky!")
        while countdown >= 1:
            print(countdown)
            countdown -= 1

        print("\nStrat: " + random.choice(strat_defense) + ".")

    else:
        print('Oops! Please type either attack or defense next time.')
        quit()

    print("GOOD LUCK :)")

    print('\nThis run -')
    print('Map: ' + player_map)
    print('Side: ' + player_side)
    if rand_agent is not None:
        print('Agent: ' + rand_agent)


if __name__ == '__main__':
    VSR()
