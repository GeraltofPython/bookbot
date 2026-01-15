def word_counter(book_string):
    return f"Found {len(book_string.split())} total words"

def char_counter(book_string):
    new_book_string = book_string.lower()
    # print(new_book_string + "\n\n")

    dict_counter = {}

    for char in new_book_string:
        if char not in dict_counter:
            dict_counter[char] = 1
        else:
            dict_counter[char] += 1
    
    return dict_counter

def sort_helper(temp_list):
    return temp_list["num"]

def sort_report(dict_counter):
    temp_list = []
    for key in dict_counter:
        item = {"char": key, "num": dict_counter[key]}
        temp_list.append(item)

    temp_list.sort(reverse=True, key=sort_helper)
    return temp_list