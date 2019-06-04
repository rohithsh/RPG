
from classes.enemy import Enemy
from classes.enemy import bcolors as bc
from classes.magic import Spell
from classes.inventory import items

# defining the Spells
# black magic
fireblast = Spell("FireBlast", 20, 100, "BlackMagic")
thunderbolt = Spell("ThunderBolt", 25, 125, "BlackMagic")
blizzard = Spell("Blizzard", 20, 100, "BlackMagic")
quake = Spell("Earthquake", 30, 160, "BlackMagic")
poison = Spell("Poison", 35, 175, "BlackMagic")
# whitemagic
heal = Spell('Heal', 25, 50, 'WhiteMagic')
superheal = Spell('SuperHeal', 40, 125, 'WhiteMagic')

# defining the items
# heals and elixir
potion = items('Potion', 'potion', 'Heals 100HP', 100, 2)
max_potion = items('Max Potion', 'potion', 'Heals 150HP', 150, 1)
elixir = items('Elixir', 'elixir', 'Restore 35HP/35MP', 35, 2)
# offensive items
grenade = items('Grenade', 'attack', 'Deals 125 damage', 125, 2)
molotov = items('Molotov', 'attack', 'Deals 100 damage', 100, 2)

# creating list for spells and items
spell_list = [fireblast, thunderbolt, blizzard, quake, poison, heal, superheal]
items_list = [potion, max_potion, elixir, grenade, molotov]

# get players name
player1_name = input('Enter Player1\'s Name: ')
player2_name = input('Enter Player2\'s Name: ')

# initializing players and enemy
player_1 = Enemy(player1_name, 550, 100, 50, 15, spell_list, items_list)
player_2 = Enemy(player2_name, 550, 100, 50, 15, spell_list, items_list)
enemy1 = Enemy('Ultra Beast', 550, 200, 70, 30, [], [])

flag = True
print(bc.WARNING + bc.BOLD + "A WILD BEAST APPEARS" + bc.ENDC)
count = 0
players = [player_1, player_2]

# Game
while flag:
    print('---------------')
    for player1 in players:
        player1.choose_action()
        print(bc.FAIL + 'What will ' + player1.name + ' do?? ' + bc.ENDC)
        player_choice = int(input())-1

        # performing selected choice
        if player_choice == 0:
            dmg = player1.generate_damage()
            enemy1.take_dmg(dmg)
            print(bc.OKGREEN + player1.name + " ATTACKED. The Beast lost", dmg, 'HP.' + bc.ENDC)

        elif player_choice == 1:
            # getting spell choice
            player1.choose_spell()
            magic_choice = int(input("Choose Your Spell "))-1
            if magic_choice == -1:
                continue
            # finding spell attributes
            spell = player1.magic[magic_choice]
            magic_dmg = spell.generate_magic_dmg()
            mp_cost = spell.cost
            current_mp = player1.get_mp()
            if mp_cost > current_mp:
                print(bc.WARNING + 'No MP' + bc.ENDC)
                continue
            player1.reduce_mp(mp_cost)
            # attack or heal
            if spell.cty == 'WhiteMagic':
                player1.heal(magic_dmg)
                print(bc.OKBLUE + player1.name + ' healed. HP increased by ' + str(magic_dmg) + bc.ENDC)
            elif spell.cty == 'BlackMagic':
                enemy1.take_dmg(magic_dmg)
                print(bc.OKGREEN + player1.name + ' cast ' + spell.name + ' . It caused ' + str(magic_dmg)
                      + ' damage to the beast.' + bc.ENDC)

        elif player_choice == 2:
            # getting item choice
            player1.choose_item()
            items_choice = int(input('Choose Your Item '))-1
            if items_choice == -1:
                continue
            # finding item attributes
            item = player1.items[items_choice]
            item_type = item.type
            item_val = item.value
            qty = item.qty
            if qty > 0:
                if item_type == 'potion':
                    player1.heal(item_val)
                    print(bc.OKGREEN + player1.name + ' healed for ' + str(item_val) + 'HP.' + bc.ENDC)
                elif item_type == 'attack':
                    enemy1.take_dmg(item_val)
                    print(bc.OKGREEN + player1.name + ' used ' + item.name + '. It dealt ' + str(item_val) + ' damage.'
                          + bc.ENDC)
                elif item_type == 'elixir':
                    player1.heal_mp(item_val)
                    player1.heal(item_val)
                    print(bc.OKGREEN + 'Increased HP and MP by ' + str(item_val) + '.' + bc.ENDC)
                item.use_item(1)
            else:
                print(bc.WARNING + bc.BOLD + 'You don\'t have any ' + item.name + 'left.' + bc.ENDC)
                continue
    print('')
    if enemy1.get_hp() >= 0:
        for player1 in players:
            enemy_choice = 1
            dmg_enemy = enemy1.generate_damage()
            player1.take_dmg(dmg_enemy)
            print(bc.OKBLUE + "The Beast attacked " + player1.name + '. ' + player1.name + " lost " + str(dmg_enemy)
                  + 'HP.' + bc.ENDC)

    print('--------------------')

    player_1.print_stats()
    player_2.print_stats()
    enemy1.print_stats()

    if player_1.get_hp() == 0 and player_2.get_hp() == 0:
        print(bc.WARNING + 'The Beast killed both of you.' + bc.ENDC)
        flag = False
    elif player_1.get_hp() == 0:
        print(bc.WARNING + 'The Beast killed ' + player_1.name + '.' + bc.ENDC)
        players.remove(player_1)
    elif player_2.get_hp() == 0:
        print(bc.WARNING + 'The Beast killed ' + player_2.name + '.' + bc.ENDC)
        players.remove(player_2)
    elif enemy1.get_hp() == 0:
        print(bc.OKGREEN + 'You Slayed the Beast' + bc.ENDC)
        flag = False
