def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def word_counter(book_text):
    word_list = book_text.split()
    counter = 0
    for word in word_list:
        counter+=1
    return f"Found {counter} total words"

def char_counter(book_text):
    counter_dict = {}
    text = book_text.lower()
    fakenum = 0
    for char in text:
        if char.isalpha() == True:
            if char in counter_dict:
                counter_dict[char]+=1
            else:
                counter_dict[char]=1
        else:
            fakenum+=1
    return(counter_dict)

def sorter(my_dict):
    return my_dict["num"]

def char_counter_sort(counter_dict):
    dict_list = []
    for entry in counter_dict:
        new_dict = {"letter": entry, "num": counter_dict[entry]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sorter)
    #print(dict_list)
    return dict_list

def report(dict_list):
    for entry in dict_list:
        print(f"{entry['letter']}: {entry['num']}")
