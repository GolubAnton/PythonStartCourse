# Пример 1
def task_1(A):
    answer = 0
    for N_elements in A:
        if N_elements > 0:
            answer += N_elements
    return answer


# Пример 2
def task_2(A):
    answer = 0
    for N_elements in A:
        answer += N_elements
    return answer/len(A)


# Пример 3
def task_3(A):
    answer = 0
    average = task_2(A)
    for N_elements in A:
        answer += (N_elements-average)**2
    answer *= 1/len(A)
    return answer**0.5
