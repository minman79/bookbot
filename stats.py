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
