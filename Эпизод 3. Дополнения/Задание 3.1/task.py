import math

def task_1(text):
    answer = {}
    text = text.strip(".")
    sentences = text.split(". ")
    for sentence in sentences:
        word_counter = len(sentence.split())
        answer[sentence] = word_counter

    return answer

def task_2(x1, y1, x2, y2):
    return math.hypot(x2-x1,y2-y1)