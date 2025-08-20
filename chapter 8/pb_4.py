def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
    

n= int(input('Enter a number: '))
print("The sum of numbers from 1 to", n, "is:", sum(n))