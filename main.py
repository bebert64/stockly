nb_intersections = int(input())
arr1 = list(map(int, input().split()))


def solution(shortcuts, nb_intersections):
    answers = [0] * nb_intersections
    shortcuts_dict = to_dict(shortcuts)
    for i in range(1, nb_intersections):
        if i not in shortcuts_dict:
            answers[i] = answers[i-1] + 1
        else:
            origins = shortcuts_dict[i] + [i-1]
            try:
                origins.remove(i)
            except ValueError:
                pass
            answers[i] = min(answers[origin] for origin in origins) + 1
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
    """Checks in opposite direction if shorter path is available by going backwards."""
    while i > 0 and (answers[i] <= answers[i-1] - 2):
        answers[i - 1] = answers[i] + 1
        i -= 1


answer = solution(arr1, nb_intersections)
print(" ".join([str(i) for i in answer]))
