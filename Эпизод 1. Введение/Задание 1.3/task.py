# Пример 1
def task_1(n):
    answer = 0
    i = 1
    while i < 11:
        answer += 1/i
        i += 1
    return answer


# Пример 2
def task_2(x, n):
    answer = x
    i = 1
    while i < 9:
        answer += x/(2*i+1)
        i += 1
    return answer


# Пример 3
def task_3(n):
    answer = 1
    i = 2
    while i < n+1:
        answer *= i
        i += 1
    return answer


# Пример 4
def task_4(x, n):
    answer = 1
    i = 2
    while i < 10:
        answer *= (x+i)/i
        i += 1
    return answer


# Пример 5
def task_5(x, n):
    answer = 0
    i = 1
    while i < n+1:
        answer += x/2
        i += 1
    return answer


# Пример 6
def task_6(n):
    answer = 1
    i = 1
    while i < 11:
        answer *= 2*i
        i += 1
    return answer
