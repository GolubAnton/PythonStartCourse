def task_1(N):
    answer = 1
    for i in range(1, N+1):
        answer *= i
    return answer


def task_2(N):
    a = 1
    answer = 1
    for i in range(1, N+1):
        answer += a
    return answer


def task_3(N):
    answer = []
    for i in range(1, N+1):
        if N % i == 0:
            answer.append(i)
    return answer
