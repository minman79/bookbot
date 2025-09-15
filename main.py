def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    print(f"{num_words} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    count = 0
    words = text.split()

    for word in words:
        count += 1
    return count

main()