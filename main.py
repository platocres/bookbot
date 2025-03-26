import sys
from stats import num_words
from stats import num_chars
from stats import sorted_chars

#If sys.argv does not have 2 strings, 
# exit the program with a status code
# of 1
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

path_file = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return(contents)
 
def main():
    book = get_book_text(path_file)
    word_count = num_words(book)
    letter_count = num_chars(book)
    sort_list = sorted_chars(letter_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sort_list:
            char = char_dict["char"]
            if char.isalpha():
                print(f"{char}: {char_dict['count']}")
    
    print("============= END ===============")


main()

