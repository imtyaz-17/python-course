def pattern(n):
    if n==0:
        return
    else:
        print('*' * n)
        pattern(n - 1)
    # while n > 0:
    #     print('*' * n)
    #     n -= 1

n = int(input('Enter a number: '))
pattern(n)