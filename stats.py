def get_word_count(input_string):
    return len(input_string.split())

def get_char_log(input_string):
    char_list = {}

    for i in range(len(input_string)):
        if input_string[i].lower() not in char_list:
            char_list[input_string[i].lower()] = 1
        else:
            char_list[input_string[i].lower()] += 1

    return char_list