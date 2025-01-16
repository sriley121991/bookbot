def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = count_characters(book_text)
    sorted_chars = char_dict_to_sorted_list(character_count)
    book_report(book_path, word_count, sorted_chars)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book):
    words = book.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    lowercase_text = text.lower()

    for character in lowercase_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict

def sort_on(dict):
    return dict['num']

def char_dict_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"ch": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def book_report(book, word_count, char_list):
    print(f"--- Begin report of {book}")
    print(f"{word_count} words found in the document")
    print()

    for char_count in char_list:
        if char_count['ch'].isalpha():
            print(f"The {char_count['ch']} character was found {char_count['num']} times")

    print("--- End report ---")

main()
