def task_1(list):
    answer = max(list, key=list.count)
    return answer

def task_2(x, y):
    N = 8
    is_correct = True
    for j in range(N):
        for i in range(j+1, N):
            if x[j] == x[i] or y[j] == y[i] or abs(x[j]-x[i]) == abs(y[j]-y[i]):
                is_correct = False
    if is_correct:
        return 'NO'
    else:
        return 'YES'


def task_3(x, y, xc, yc, r):
    answer = ((x-xc)**2+(y-yc)**2) <= (r*r)
    return answer


def task_4(list):
    count = 0
    for i in range(1, len(list)-1):
        if list[i-1] < list[i] > list[i+1]:
            count += 1
    return count


def task_5(key):
    text_file = open("file.txt", "r").read()
    lines = text_file.split('\n')
    answer = []
    for line in lines:
        if '' == line:
            continue
        line = line.lower()
        newLine = ''
        for char in line:
            if char.isalpha():
                newChar = chr((ord(char) + key - 96) % 26 + 96)
            else:
                newChar = chr((ord(char) + key) + 64)
            newLine += newChar
        answer.append(newLine)
    return answer