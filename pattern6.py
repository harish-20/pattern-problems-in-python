def pat6(n):
    for row in range(0,n):
        for col in range(n,0,-1):
            print('*'if col<=row else ' ',end='')
        print('')
pat6(6)
        