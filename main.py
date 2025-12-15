from stats import get_word_count, get_char_log, get_sorted_char_log

def get_book_text(filepath):

    with open(filepath) as file:
        contents = file.read()

    return contents

def main():
    # print(get_book_text("books/frankenstein.txt"))
    word_count = get_word_count(get_book_text("books/frankenstein.txt"))
    char_log = get_char_log(get_book_text("books/frankenstein.txt"))
    sorted_log = get_sorted_char_log(char_log)

    print_report(sorted_log)

def print_report(char_count_dict):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text("books/frankenstein.txt"))} total words")
    print("--------- Character Count -------")
    for dict in char_count_dict:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
    
main()