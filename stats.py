# this takes the text from the doc
# there is a copy in main.py
# this is currently for testing in this file only (and get rid of that error)
# input argument: python3 main.py <path_to_book>
import sys

def input_check():
    if not len(sys.argv) == 2:
        raise Exception("Usage: python3 main.py <path_to_book>")

filepath = sys.argv[1]

def get_book_txt(filepath):
    with open(filepath) as f:
        return f.read()

# this gets the number of words in the doc
def get_num_words(filepath):
    w = get_book_txt(filepath).split()
    num_words = (f"{len(w)}")
    return num_words

# this gets all of the characters in the doc, as a tuple
def get_characters(filepath):
    d = dict()
    str = get_book_txt(filepath).lower()
    for k in str:
        if k not in d:
            d[k] = str.count(k)
    return d

# this is the sorting argument for sort_list, it expects a dict
def sort_on(dict):
    return dict["num"]

# this sorts the list of characters by value
def sort_list():
    l = list()
    d = get_characters(filepath)
    for k in d:
        if k not in l:
            l.append({"char": k,"num": d[k]})
    l.sort(reverse=True, key=sort_on)
    return l

## comment out everything below this line before commit
##def test():
##    get_book_txt("books/frankenstein.txt")
##    print(get_characters())
##    sort_list()

##test()
