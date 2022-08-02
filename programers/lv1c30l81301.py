"""
숫자 문자열과 영단어
"""


def switch(s):
    dic = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for k, v in dic.items():
        if k in s:
            s = s.replace(k, v)

    return s


def solution(s):
    answer = int(switch(s))
    return answer
