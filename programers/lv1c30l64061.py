"""
크레인 인형뽑기 게임
"""


def explode(basket, answer):
    for idx in range(len(basket)):
        v = basket[idx]
        if idx != len(basket) - 1 and v == basket[idx + 1]:
            answer = answer + 2
            basket.pop(idx)
            basket.pop(idx)
            answer = explode(basket, answer)
            break
    return answer


def move(board, target):
    target = target - 1
    result = -1
    for idx, row in enumerate(board):
        if row[target] != 0:
            result = row[target]
            board[idx][target] = 0
            break
    return board, result


def solution(board, moves):
    basket = list()
    answer = 0
    for i in moves:
        board, result = move(board, i)
        if result != -1:
            basket.append(result)

    answer = explode(basket, answer)

    return answer


def main():
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1],
    ]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]

    print(solution(board, moves))


if __name__ == "__main__":
    main()
