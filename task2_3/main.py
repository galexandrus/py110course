import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename) as f1:
        input_data = json.load(f1)
    # scores = []
    # for dict_ in input_data:
    #     scores.append(dict_.get("score"))
    # max_score = max(scores)
    # # TODO найти максимальный элемент по ключу score
    # dict_with_max_score = {}
    # for dict_ in input_data:
    #     if dict_.get("score") == max_score:
    #         dict_with_max_score = dict_
    # return dict_with_max_score
    return max(input_data, key=lambda x: x.get("score"))


if __name__ == "__main__":
    print(task())
