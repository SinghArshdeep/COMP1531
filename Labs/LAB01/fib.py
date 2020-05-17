#hey new comment
'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    a = 1
    b = 1
    c = 0
    list = []
    
    if int(n) == 1:
        list.append(a)
    elif int(n) == 2:
        list.append(a)
        list.append(b)
    elif int(n) >= 3:
        list.append(a)
        list.append(b)
        for i in range(2, int(n)):
            c = a + b
            list.append(c)
            a = b
            b = c
    return list
    # TODO = fill in the code here, and return the correct result using the return keyword
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    n = input("Enter the number")
    print(produceFibsList(n))
