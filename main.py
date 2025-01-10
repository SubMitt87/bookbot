def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dictionary = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_dictionary)


    print(welcome_message(book_path))
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")


def welcome_message(path):
    return f"--- Begin report of {path} ---"

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_characters(text):
# count the characters and order the list
    lower_text = text.lower()
    char_dictionary = {}
    for char in lower_text:
        
        if char not in char_dictionary:
            char_dictionary[char] = 1
        elif char in char_dictionary:
            char_dictionary[char] += 1


    return char_dictionary

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char" : ch, "num" : num_chars_dict[ch]})
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list
    
main()
