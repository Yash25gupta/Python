def checkPalindrome(txt):
    txt, rev = txt.lower(), txt[::-1].lower()
    if txt == '' or len([i for i in range(len(txt)) if txt[i] != rev[i]]) > 2: return 'No'
    if txt == rev: return 'Yes'
    return 'Partially'


for i in ('ABABA', 'ABBAA', 'NEXTGEN', 'Ababa', ''):
    print(checkPalindrome(i))
