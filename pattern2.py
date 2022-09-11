def pat2(n):
    for row in range(0,n+1):
        print(end='\n\n')
        for col in range(0,n-row):
            print('*   ',end='')
pat2(int(input('Enter a num...')))