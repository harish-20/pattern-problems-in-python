def pat7(n):
    for row in range(0,n):
        for col in range(0,n):
            print('*' if col>=row else ' ',end='')
        print('')
pat7(7)
        
