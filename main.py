nb_intersections = int(input())
arr1 = list(map(int, input().split()))


def solution(shortcuts, nb_intersections):
    answers = [0] * nb_intersections
    shortcuts_dict = to_dict(shortcuts)
    # print(shortcuts_dict)
    for i in range(1, nb_intersections):
        # print(f"checking {i=}")
        if i not in shortcuts_dict:
            # print(f"{i=} not an end point")
            answers[i] = answers[i-1] + 1
            # print(f"{answers[i]=}")
        else:
            origins = shortcuts_dict[i] + [i-1]
            try:
                origins.remove(i)
            except ValueError:
                pass
            # print(f"{origins=}")
            answers[i] = min(answers[origin] for origin in origins) + 1
            # print(f"{answers[i]=}")
            retro_check(answers, i)
    return answers


def to_dict(shortcuts):
    """
    Dict with origin point for each shortcut's ending.

    All values are re-normalized to origin = 0.
    """
    shortcuts_dict = {}
    for index, value in enumerate(shortcuts):
        try:
            shortcuts_dict[value-1].append(index)
        except KeyError:
            shortcuts_dict[value-1] = [index]
    return shortcuts_dict


def retro_check(answers, i):
    if answers[i] <= answers[i-1] - 2:
        # print("retro-check needed")
        # print(f"{answers[i]=}")
        # print(f"before : {answers[i-1]=}")
        answers[i-1] = answers[i] + 1
        # print(f"after : {answers[i-1]=}")
        retro_check(answers, i-1)


answer = solution(arr1, nb_intersections)
print(" ".join([str(i) for i in answer]))
