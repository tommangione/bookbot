def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def word_counter():
    text = get_book_text()
    word_list = text.split()
    counter = 0
    for word in word_list:
        counter+=1
    print(f"{counter} words found in the document")
