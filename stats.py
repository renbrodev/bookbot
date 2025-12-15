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

def get_sorted_char_log(unsorted_log):
    
    log_list = [] # list for holding char num key pairs
    char_count_list =[] # list for holding char count so we can sort
    sorted_chars = [] #list that will hold sorted version

    # create char num key pair list so we can fix new list in the end
    for log in unsorted_log:
        log_list.append({"char" : log, "num" : unsorted_log[log]})

    # make the char list from the log list
    for log in log_list:
        char_count_list.append(log["num"])

    # then sort it
    char_count_list.sort(reverse=True)

    sorted_chars = help_get_sorted_char_log(char_count_list, log_list)
    
    # pass the sorted char list and dictionary in to helper so it can be rearranged
    return sorted_chars

def help_get_sorted_char_log(num_list, char_dict):
    sorted_dicts = []

    # tedious but for each number check each entry in the dictionary
    for num in num_list:
        for dict in char_dict:
            # if you find a match append it to the list
            if dict["num"] == num:
                # skip non alpha characters
                if dict["char"].isalpha() == False:
                    continue
                sorted_dicts.append(dict)
    
    # since we are going down an ordered list of numbers to check we will end up with an ordered list of dictionaries
    return sorted_dicts