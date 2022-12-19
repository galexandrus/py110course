INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as f1, \
            open(OUTPUT_FILE, "w") as f2:
        for output_line in map(str.upper, f1):
            f2.write(output_line)
        # for text_line in f1:
        #     f2.write(text_line.upper())
    # TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
