def uniqueCharMap(text):
    # cMap = {c: str(i + 1) for i, c in enumerate(sorted(set([i for i in text]))) if c.isalpha()}
    # try:
    #     out = ''.join([cMap[c] for c in text])
    # except:
    #     out = 'ERROR'
    # return out
    cMap = {}
    return ''.join([cMap.setdefault(c, str(len(cMap) + 1)) for c in text]) if text.isalpha() else 'ERROR'


for i in ('ABABCABD', 'NEXTGEN', 'AAAAAAAA', 'HmmM', 'ABCD', 'no5'):
    print(uniqueCharMap(i))
