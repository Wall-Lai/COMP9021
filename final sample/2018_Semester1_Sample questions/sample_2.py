
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    banknotes = dict.fromkeys(banknote_values, 0)

    while N >= 100:
        N -= 100
        banknotes[100] = banknotes[100] + 1

    while N >= 50:
        N -= 50
        banknotes[50] = banknotes[50] + 1

    while N >= 20:
        N -= 20
        banknotes[20] = banknotes[20] + 1

    while N >= 10:
        N -= 10
        banknotes[10] = banknotes[10] + 1

    while N >= 5:
        N -= 5
        banknotes[5] = banknotes[5] + 1

    while N >= 2:
        N -= 2
        banknotes[2] = banknotes[2] + 1

    while N >= 1:
        N -= 1
        banknotes[1] = banknotes[1] + 1


    # Insert your code here
    print('Here are your banknotes:')
    for value in sorted(banknotes):
        if banknotes[value]:
            print('${}: {}'.format(value, banknotes[value]))
                        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
