def pokemonTraners(type1, attack1, health1, type2, attack2, health2):
    strongWeak = (('Fire', 'Grass'), ('Grass', 'Water'), ('Water', 'Fire'))
    if (type1, type2) in strongWeak:
        attack1 *= 2
        attack2 *= 0.5
    elif (type2, type1) in strongWeak:
        attack2 *= 2
        attack1 *= 0.5
    count1 = health2 / attack1 if health2 % attack1 == 0 else health2 / attack1 + 1
    count2 = health1 / attack2 if health1 % attack2 == 0 else health1 / attack2 + 1
    return 'Trainer ' + ('1' if count1 < count2 else '2') + ' Wins'


print(pokemonTraners('Water', 100, 500, 'Fire', 200, 400))
print(pokemonTraners('Grass', 200, 100, 'Water', 100, 900))
