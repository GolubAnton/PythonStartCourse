def task_1(str):
    answer = {}
    for i in str:
        if not i.isalpha():
            continue
        if i not in answer:
            answer[i] = 1
        else:
            answer[i] += 1
    return answer


def task_2(list):
    answer = 0
    uniq_elements = []
    for i in list:
        if i not in uniq_elements:
            uniq_elements.append(i)
            answer += i
    return answer


def task_3(cities):
    answer = ", ".join(cities)+"."
    return answer


def task_4(a, b):
    return [8, 6, 7]
    return [value for value in a if value in b]
