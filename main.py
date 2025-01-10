def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_dictionary = count_characters(text)
    print(char_dictionary)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_characters(text):
    lower_text = text.lower()
    char_dictionary = {}
    for char in lower_text:
        if char not in char_dictionary:
            char_dictionary[char] = 1
        elif char in char_dictionary:
            char_dictionary[char] += 1

    return char_dictionary

    
main()
