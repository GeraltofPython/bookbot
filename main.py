import sys
from stats import word_counter, char_counter, sort_report


def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_string = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_counter(book_string))
    print("--------- Character Count -------")
    
    sorted_report = sort_report(char_counter(book_string)) 
    for item in sorted_report:
        print(f"{item["char"]}: {item["num"]}")
            
    print("============= END ===============")


main()