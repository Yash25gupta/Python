def maxNoOfVillains(health, *villains):
    for i, villain in enumerate(sorted(villains)):
        health -= villain
        if health < 0: return i
    return len(villains)


print(maxNoOfVillains(200, 54, 23, 65, 87, 12))
