import sys
from stats import get_book_text
from stats import word_counter
from stats import char_counter
from stats import sorter
from stats import char_counter_sort
from stats import report

def main():
    if len(sys.argv)>1:
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        book_text = get_book_text(book_path)
        print("----------- Word Count ----------")
        print(word_counter(book_text))
        print("--------- Character Count -------")
        #print(char_counter(book_text))
        report(char_counter_sort(char_counter(book_text)))
        return 0
    else:
        sys.exit("Usage: python3 main.py <path_to_book>")
main()
