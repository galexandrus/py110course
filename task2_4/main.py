import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename) as f1:
        input_data = json.load(f1)

    gen_exr = [x.get("contains_improvement_appeals") for x in input_data]
    # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
