def similarCharAtSameIndex(txt1, txt2):
    txt1, txt2 = txt1.lower(), txt2.lower()
    
    # # Code without list Comprehension
    count = 0
    for i in range(min(len(txt1), len(txt2))):
        if txt1[i] == txt2[i]:
            count += 1
    return count

    # # Code using list Comprehension
    # return len([i for i in range(min(len(txt1), len(txt2))) if txt1[i] == txt2[i]])


s1 = 'NEXT Gen Coder HELLO Keep Coding'.split(' ')
s2 = 'VeST Mens Sholder hello sleep Running'.split(' ')
for i, j in zip(s1, s2):
    print(similarCharAtSameIndex(i, j))
