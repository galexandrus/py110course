import json


def task(input_filename: str, output_filename: str) -> None:
    # TODO считать содержимое json файл input.json
    with open(input_filename) as f1:
        input_data = json.load(f1)  # python object
    # TODO записать содержимое в json файл output.json с отступами
    with open(output_filename, "w") as f2:
        json.dump(input_data, f2, indent=4)


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
