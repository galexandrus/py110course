def task() -> str:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    # используй ключевую функцию у функции min, по которой она должна определять минимальный элемент
    return min(list_words, key=len)


if __name__ == "__main__":
    print(task())
