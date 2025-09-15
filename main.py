from stats import number_of_words, count_of_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    character_list = count_of_characters(text)

    print(f"{num_words} words found in the document")
    print(character_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()