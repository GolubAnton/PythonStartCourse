import math


def task_1(a, search):
    low = 0
    high = len(a)-1
    middle = len(a)//2
    while a[middle] != search and low <= high:
        if search > a[middle]:
            low = middle+1
        else:
            high = middle-1
        middle = (low+high)//2
    return str(middle)


def task_2(input):
    is_prime_number = True
    for i in range(2, int(math.sqrt(input))):
        if input % i != 0:
            is_prime_number = False
    return is_prime_number