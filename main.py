from stats import get_word_count, get_char_log

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()

    return contents

def main():
    # print(get_book_text("books/frankenstein.txt"))
    print(f"Found {get_word_count(get_book_text("books/frankenstein.txt"))} total words.")
    print(f"Char Log: {get_char_log(get_book_text("books/frankenstein.txt"))}")


main()