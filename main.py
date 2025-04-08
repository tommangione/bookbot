from stats import get_book_text
from stats import word_counter
from stats import char_counter
from stats import sorter
from stats import char_counter_sort
from stats import report

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_text = get_book_text()
    print("----------- Word Count ----------")
    print(word_counter(book_text))
    print("--------- Character Count -------")
    #print(char_counter(book_text))
    report(char_counter_sort(char_counter(book_text)))

main()
