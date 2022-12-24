import json
import re

BOOKS_FILE = "books.md"
# TODO записать ругулярное выражения для поиска книги
position_r = r"#{4} (?P<position>\d{1,2})\. "
book_name_r = r"\[(?P<book>[\w: '\-]+)\]"
book_url_r = r"\((?P<book_url>https:[/\w.]+)\)"
author_r = r" by +(?P<author>[\w'&. Г§]+\b)"
recommended_r = r" +\((?P<recommended>[\d.]{,5})\% +(?:recommended)\)"
cover_url_r = r"\n+!\[\]\((?P<cover_url>https:[/\w._#]+)\)"
description_r = r"(?P<description>(?:\n{1,2}[\"\w:;,. \'\’\[\]/?\-\—\(\)!&“”]+)+)"
BOOK_REGEX = position_r + book_name_r + book_url_r + author_r + recommended_r + cover_url_r + description_r


def task():
    # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)
    books_list = []

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            books_list.append(book.groupdict())
            # json_books_dict = json.dumps(book.groupdict(), indent=4)

    sorted_books_list = sorted(books_list, key=lambda x: float(x.get("recommended")), reverse=True)
    # for book_dict in sorted_books_list:
    #     print(book_dict)
    # print(len(books_list))

    with open("sorted_books.json", "w") as f2:
        json.dump(sorted_books_list, f2, indent=4)

    with open("sorted_books.json") as f3:
        for line in f3:
            print(line, end="")

if __name__ == '__main__':
    task()
