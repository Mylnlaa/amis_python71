n, k = [int(i) for i in input('Enter the number of pins and the number of throws: ').split()]
a = [1 for i in range(n)]                                                                                               
for i in range(k):
    x, y = [int(i) for i in input('Enter a number pair: ').split()]                                                     
    for i in range(x-1, y):                                                                                             
        if a[i] == 1:
            a[i] = 0
for i in a:
    if i == 1:
        print('|', end='')
    else:
        print('.', end='')
