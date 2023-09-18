from contextlib import suppress
cp, sp, mp, diff, diffPercent, dis, disPercent = None, None, None, None, None, None, None
# Enter value below
disPercent = 50
cp = 400
diffPercent = 80

def calculateAll():
    global cp, sp, mp, diff, diffPercent, dis, disPercent
    for _ in range(3):
        if cp is None:
            with suppress(TypeError): cp = sp - diff
            with suppress(TypeError): cp = (sp * 100) // (100 + diffPercent)
            with suppress(TypeError): cp = diff * 100 // diffPercent
        if sp is None:
            with suppress(TypeError): sp = diff + cp
            with suppress(TypeError): sp = cp * (100 + diffPercent) // 100
            with suppress(TypeError): sp = mp - dis
            with suppress(TypeError): sp = mp - (disPercent * mp // 100)
        if diff is None:
            with suppress(TypeError): diff = sp - cp
            with suppress(TypeError): diff = diffPercent * cp // 100
        if diffPercent is None:
            with suppress(TypeError): diffPercent = diff * 100 // cp
        if mp is None:
            with suppress(TypeError): mp = dis * 100 // disPercent
            with suppress(TypeError): mp = dis + sp
            with suppress(TypeError): mp = (sp * 100) // (100 - disPercent)
        if dis is None:
            with suppress(TypeError): dis = mp - sp
            with suppress(TypeError): dis = disPercent * mp // 100
        if disPercent is None:
            with suppress(TypeError): disPercent = dis * 100 // mp
            with suppress(TypeError): disPercent = 100 - (sp * 100 // mp)


if __name__ == '__main__':
    calculateAll()
    print('cp =', cp)
    print('sp =', sp)
    print('diff =', diff)
    print('diffPercent =', diffPercent)
    print('mp =', mp)
    print('dis =', dis)
    print('disPercent =', disPercent)
