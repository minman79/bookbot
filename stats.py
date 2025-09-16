def number_of_words(text):
    words = text.split()
    return len(words)

def count_of_characters(text):
    no_of_letters = {}
    list_of_characters = list(text.lower())

    for character in list_of_characters:
        if character not in no_of_letters:
            no_of_letters[character] = 1
        else:
            no_of_letters[character] += 1
    
    return no_of_letters

def sort_dict(dictionary):
    new_dict_list = []

    for k, v in dictionary.items():
        if k.isalpha():
            new_dict_list.append({"char": k, "num": v})
    new_dict_list.sort(reverse=True, key=sort_on)
    return new_dict_list

def sort_on(items):
    return items["num"]
