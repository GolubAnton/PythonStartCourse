
def task_1(str):
    words_split = str.split()
    answer = words_split[-1]
    return len(answer)


def task_2(str):
    words_split = str.split()
    counter = len(words_split)
    answer = []
    for i in range(0, counter, 2):
        if i + 1 < counter:
            answer.append(words_split[i+1])
        answer.append(words_split[i])
    return " ".join(answer)


def task_3(str):
    words_split = str.split()
    previous_word = ""
    answer = 0
    for word in words_split:
        if previous_word == "":
            previous_word = word
            continue
        if word[0] == previous_word[len(previous_word)-1]:
            answer += 1
        previous_word = word
    return answer
