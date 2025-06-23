import sys

def input_check():
    if not len(sys.argv) == 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
try:
    input_check()
except Exception as e:
    print(e)
    sys.exit(1)
    
filepath = sys.argv[1]

def get_book_txt(filepath):
    with open(filepath) as f:
        return f.read()

from stats import get_characters, get_num_words, sort_on, sort_list

def main():
    get_book_txt(filepath)
    words = get_num_words(filepath)
    get_characters(filepath)
    sort_on(dict)
    char_list = sort_list()
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------
    """)
    for k in char_list:
        if not k['char'].isalpha():
            pass
        else:
            print(f"{k['char']}: {k['num']}")
    print("""
============= END ===============
    """)

main()