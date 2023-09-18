def shiftDirection(txt1, txt2):
    if txt1 == txt2 or txt2 not in (txt1 * 2): return 'Not Shifted'
    shift = (txt1 * 2).find(txt2)
    if shift < len(txt1) / 2: return 'Left Shifted by ' + str(shift)
    return 'Right Shifted by ' + str(len(txt1) - shift)


t1 = ('nextgencoder', 'nextgencoder', 'ngc', 'a')
t2 = ('gencodernext', 'odernextgenc', 'cng', 'a')
for i, j in zip(t1, t2):
    print(shiftDirection(i, j))
