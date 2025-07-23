from stats import word_count, char_count, sort_dictionaries
import sys

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents
    
def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    relative_path = sys.argv[1]
    print("Analyzing book found at", relative_path, "...")

    book_text = get_book_text(relative_path)
    print("----------- Word Count ----------")
    print("Found", word_count(book_text), "total words")

    chars_dict = char_count(book_text)
    sorted_dicts = sort_dictionaries(chars_dict)
    print("--------- Character Count -------")
    for dict in sorted_dicts:
        if dict["char"].isalpha():
            print(str(dict["char"]) + ":", dict["num"])

    print("============= END ===============")

main()