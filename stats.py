def get_word_count(text):
    text_list = text.split()
    return len(text_list)

def get_char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] = char_dict[char] + 1
    return char_dict

def sort_on(char_dict):
    sorted_list = []
    def sort_key(list):
        return list["num"]

    for entry in char_dict:
        if entry.isalpha() == True:
            sorted_list.append({"char":entry, "num":char_dict[entry]})
    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list

