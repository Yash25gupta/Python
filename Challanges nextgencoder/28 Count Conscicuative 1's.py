def repeatedCount(lst):
    ''' Return count of consiquative 1's in a list containing 1's and 0's. '''
    return len([i for i in ''.join(map(str, lst)).split('0') if len(i) > 1])


print(repeatedCount([1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1]))
