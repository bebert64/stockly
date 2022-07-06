nb_intersections = int(input())
arr1 = list(map(int, input().split()))


def solution(shortcuts, nb_intersections):
    answers = [0] * nb_intersections
    try:
        shortcuts_dict = to_dict(shortcuts)
    except:
        print("error to_dict")
        exit()
    # print(shortcuts_dict)
    for i in range(1, nb_intersections):
        # print(f"checking {i=}")
        if i not in shortcuts_dict:
            # print(f"{i=} not an end point")
            try:
                answers[i] = answers[i-1] + 1
            except:
                print("error in initial value")
                exit()
            # print(f"{answers[i]=}")
        else:
            try:
                origins = shortcuts_dict[i] + [i-1]
            except:
                print("error trying generate origins")
                exit()
            try:
                origins.remove(i)
            except ValueError:
                pass
            # print(f"{origins=}")
            try:
                answers[i] = min(answers[origin] for origin in origins) + 1
            except:
                print("error getting minimum")
                exit()

            try:
                retro_check(answers, i)
            except Exception as err:
                print(err)
                exit()
            # print(f"{answers[i]=}")
            
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
    assert i>0
    assert i<nb_intersections
    # if answers[i] <= answers[i-1] - 2:
    #     # print("retro-check needed")
    #     # print(f"{answers[i]=}")
    #     # print(f"before : {answers[i-1]=}")
    #     answers[i-1] = answers[i] + 1
    #     # print(f"after : {answers[i-1]=}")
    #     retro_check(answers, i-1)
    while i > 0 and (answers[i] <= answers[i-1] - 2):
        answers[i - 1] = answers[i] + 1
        i -= 1

answer = solution(arr1, nb_intersections)
print(" ".join([str(i) for i in answer]))
