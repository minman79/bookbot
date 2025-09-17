import sys

from stats import (
    number_of_words, 
    get_chars_dict, 
    chars_dict_to_sorted_list,
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    character_list = get_chars_dict(text)
    isalpha_character_count = chars_dict_to_sorted_list(character_list)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in isalpha_character_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()