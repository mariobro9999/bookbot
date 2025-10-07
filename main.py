from stats import word_count
from stats import char_count
from stats import sort_alpha

import sys



def get_book_text(b):
    with open(b) as f:
        file_contents = f.read()
    return file_contents
    

def main():
    book = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------", )

    count_words = word_count(book)
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")

    alpha = char_count(book)
    
    sort_char = sort_alpha(alpha)

    for char in sort_char:
        num = sort_char[char]
        print(f"{char}: {num}")
    print("============= END ===============")


if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()