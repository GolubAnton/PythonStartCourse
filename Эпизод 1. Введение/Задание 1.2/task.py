import math

# Пример 1
def task_1(a, b):
    if a > b:
        return (a*b)**0.5-3
    elif a == b:
        return math.log10(2)
    elif a < b:
        return (math.log(a ** 3 + 1)) / b
    return


# Пример 2*
def task_2(a, b):
    if a < b:
        return math.tan(a/b)+1
    elif a == b:
        return math.tan(-1)
    elif a > b:
        return ((a*b-5)**0.5)/a
    return


# Пример 3
def task_3(a, b):
    if a > b:
        return math.log10(a*b)+21
    elif a == b:
        return math.tan(-5)
    elif a < b:
        return math.log(3*a/b)+1
    return


# Пример 4
def task_4(a, b):
    if a > b:
        return (a*b-1)**0.5
    elif a == b:
        return math.log10(255)
    else:
        return math.tan(a-5)/b
    return


# Пример 5
def task_5(a, b):
    if a > b:
        return math.log(a/b)+31
    elif a == b:
        return math.tan(-25)
    else:
        return (math.cos(a*5-1))/a
    return


# Пример 6
def task_6(a, b):
    if a < b:
        return (b/a+1)**0.5
    elif a == b:
        return 25**0.5
    return math.log10(a**3-5)/b
