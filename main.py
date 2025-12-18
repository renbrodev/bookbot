import sys
from stats import get_word_count, get_char_log, get_sorted_char_log

def get_book_text(filepath):

    with open(filepath) as file:
        contents = file.read()

    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    word_count = get_word_count(get_book_text(f"{sys.argv[1]}"))
    char_log = get_char_log(get_book_text(f"{sys.argv[1]}"))
    sorted_log = get_sorted_char_log(char_log)

    print_report(sorted_log)

def print_report(char_count_dict):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(f"{sys.argv[1]}"))} total words")
    print("--------- Character Count -------")
    for dict in char_count_dict:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
    
main()