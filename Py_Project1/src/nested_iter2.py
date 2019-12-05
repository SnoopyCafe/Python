import sys
import operator

'''Provided is a dictionary that contains pokemon go player data, where each player reveals the amount of 
candy each of their pokemon have. If you pooled all the data together, which pokemon has the highest number of candy? 
Assign that pokemon to the variable most_common_pokemon'
'''
pokemon_go_data = {'bentspoon':
                  {'Rattata': 203, 'Pidgey': 120, 'Drowzee': 89, 'Squirtle': 35, 'Pikachu': 3, 'Eevee': 34, 'Magikarp': 300, 'Paras': 38},
                  'Laurne':
                  {'Pidgey': 169, 'Rattata': 245, 'Squirtle': 9, 'Caterpie': 38, 'Weedle': 97, 'Pikachu': 6, 'Nidoran': 44, 'Clefairy': 15, 'Zubat': 79, 'Dratini': 4},
                  'picklejarlid':
                  {'Rattata': 32, 'Drowzee': 15, 'Nidoran': 4, 'Bulbasaur': 3, 'Pidgey': 56, 'Weedle': 21, 'Oddish': 18, 'Magmar': 6, 'Spearow': 14},
                  'professoroak':
                  {'Charmander': 11, 'Ponyta': 9, 'Rattata': 107, 'Belsprout': 29, 'Seel': 19, 'Pidgey': 93, 'Shellder': 43, 'Drowzee': 245, 'Tauros': 18, 'Lapras': 18}}

stats = {}
most_common_pokemon = 0
for k in pokemon_go_data.keys():
    for l2_key in pokemon_go_data[k]:
        the_value = pokemon_go_data[k][l2_key]
        if l2_key in stats:
            stats[l2_key] += the_value
        else:
            stats[l2_key] = the_value

most_common_pokemon = max(stats, key=lambda key: stats[key])
#most_common_pokemon = max(stats.items(), key=operator.itemgetter(1))[0]

print(most_common_pokemon, stats[most_common_pokemon])
sys.exit()

'''we have provided a nested list called big_list. Use nested iteration to create a dictionary, word_counts, 
that contains all the words in big_list as keys, and the number of times they occur as values.
'''
 
big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]
word_counts = {}
for words in big_list:
    if isinstance(words, list):
        for word in words:
            if isinstance(word, list):
                 for w in word:
                    if w in word_counts: #exists
                        word_counts[w] = word_counts[w] + 1
                    else:
                        word_counts[w] = 1
print(word_counts)
sys.exit()

''' The nested dictionary, pokemon, shows the number of various Pokemon that 
 each person has caught while playing Pokemon Go. Find the total number of 
 rattatas, dittos, and pidgeys caught and assign to the variables r, d, and p respectively.
 Do not hardcode. Note: Be aware that not every trainer has caught a ditto.
'''

pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}},}

r,d,p = 0,0,0
for k in pokemon.keys():
    for l2_key in pokemon[k]:
        lvl2 = pokemon[k][l2_key]
        for k2 in lvl2.keys():
            if k2 == 'rattatas':
                r += lvl2[k2]
            elif k2 == 'ditto':
                d += lvl2[k2]
            elif k2 == 'pidgey':
                p += lvl2[k2]
            #print(k2, rat[k2])
            
print(r,d,p)