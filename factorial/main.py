n = input('Enter a number greater than 3: ')
n = int(n)


def recursion(n):
    # initialize to 1 to avoid divide by 0 error
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


print(recursion(n))
