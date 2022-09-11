def pattern19(n):
    for rows in range(0, n):
        for firstHalf in range(0, n):
            character = '*' if (firstHalf <= rows) else ' '
            print(character, end='')
        for secondHalf in range(n, -1, -1):
            character = '*' if (secondHalf <= rows) else ' '
            print(character, end='')
        print()
        
    for rows in range(n , -1, -1):
        for firstHalf in range(0, n):
            character = '*' if (firstHalf <= rows) else ' '
            print(character, end='')
        for secondHalf in range(n, -1, -1):
            character = '*' if (secondHalf <= rows) else ' '
            print(character, end='')
        print()

pattern19(5)