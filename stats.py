def number_of_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    lowered_text = list(text.lower())
    for character in lowered_text:
        if character not in chars:
            chars[character] = 1
        else:
            chars[character] += 1
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for k, v in num_chars_dict.items():
        if k.isalpha():
            sorted_list.append({"char": k, "num": v})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


