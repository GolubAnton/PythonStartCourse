import math

# Пример 1
def task_1(a, d, c):
    answer = (c-d/5+(321**0.5))/(1+3*a)
    return answer


# Пример 2
def task_2(a, d, c):
    answer = (math.log10(c/3)-d+25)/(5*a-1)
    return answer


# Пример 3
def task_3(a, d, c):
    answer = (c/2+math.log(d)-35)/(5*a+1)
    return answer


# Пример 4
def task_4(a, d, c):
    answer = (math.tan(c)+d/32)/(a/3+1)
    return answer


# Пример 5
def task_5(a, d, c):
    answer = (c/5-d+1)/(c+math.tan(2*a))
    return answer


# Пример 6
def task_6(a, d, c):
    answer = (((25*c)**0.5)+d-3)/(d-a**2+1)
    return answer


# Пример 7
def task_7(a, d, c):
    answer = (5*math.log10(c)+3*d-32)/(a**2+1)
    return answer


# Пример 8
def task_8(a, d, c):
    answer = (c*d-math.log(4*3*a))/(c+a-1)
    return answer
