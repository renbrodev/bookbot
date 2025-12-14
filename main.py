from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()

    return contents

def main():
    # print(get_book_text("books/frankenstein.txt"))
    print(f"Found {get_word_count(get_book_text("books/frankenstein.txt"))} total words.")

main()