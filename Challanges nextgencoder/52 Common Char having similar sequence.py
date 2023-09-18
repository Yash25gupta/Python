def cc52(txt1, txt2):
    stxt, ltxt = (txt1, txt2) if len(txt1) < len(txt2) else (txt2, txt1)
    common = [(0, -1)]
    for i in stxt:
        if i in ltxt:
            nxtIndex = common[-1][1] + 1
            if nxtIndex != 0 or len(common) == 1:
                common.append((i, ltxt.find(i, nxtIndex)))
    return common[1:]


t1 = 'hello hello heLlo corram nextgencoder'.split(' ')
t2 = 'oleh bell bell comply nerde'.split(' ')
for i, j in zip(t1, t2):
    print(cc52(i, j))
