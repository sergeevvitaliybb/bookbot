def get_num_words(text):
    words = text.split()
    return len(words)

def total_characters_count(text):
    characters_dict = {}
    for char in text.lower():
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    return characters_dict

def listed_chars(chars_in_text):
    list_of_dicts = []
    for char, num in chars_in_text.items():
        list_of_dicts.append({"char": char, "num": num})
    return list_of_dicts

def sort_on(dict):
    return dict["num"]