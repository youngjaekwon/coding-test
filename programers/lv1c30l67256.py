"""
[카카오 인턴] 키패드 누르기
"""

keypad = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
    "*": (3, 0),
    0: (3, 1),
    "#": (3, 2),
}

left = "*"
right = "#"


def get_distance(current, target):
    target_x, target_y = keypad[target]
    current_x, current_y = keypad[current]

    return int(abs(target_x - current_x) + abs(target_y - current_y))


def move(number, hand):
    global left
    global right

    left_distance = get_distance(left, number)
    right_distance = get_distance(right, number)

    if left_distance == right_distance:
        if hand == "left":
            left = number
            return "L"
        else:
            right = number
            return "R"
    elif left_distance < right_distance:
        left = number
        return "L"
    else:
        right = number
        return "R"


def solution(numbers, hand):
    answer = ""
    global left
    global right
    for number in numbers:
        if number in [1, 4, 7]:
            left = number
            answer += "L"
        elif number in [3, 6, 9]:
            right = number
            answer += "R"
        else:
            answer += move(number, hand)
    return answer


if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"

    print(solution(numbers, hand))
