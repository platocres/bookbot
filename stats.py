def num_words(book_contents):
    words = list(book_contents.split())
    return len(words)

def num_chars(book_contents):
    chars = book_contents.lower()
    letter_dict = {}
    for char in chars:
        letter_dict[char] = letter_dict.get(char, 0) + 1
    return letter_dict

def sorted_chars(dict):
    list_dict = []
    
    for key, value in dict.items():
        list_dict.append({"char": key, "count": value})
    
    # Define how to sort
    def sort_on(item):
        return item["count"]
    
    # Sort in-place
    list_dict.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return list_dict

    

