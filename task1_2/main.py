OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as f:
        sign = "*"
        for i in range(1, 11):
            text_line = "{:>10s}".format(sign * i)
            f.write(text_line + "\n")
    # TODO записать лесенку в файл


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
