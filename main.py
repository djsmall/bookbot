import sys
from stats import get_word_count, get_char_count, sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def pretty_list(list):
    for entry in list:
        print(f"{entry['char']}: {entry['num']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        text = get_book_text(file_path)
        word_count = get_word_count(text)
        char_count = get_char_count(text)
        sorted_list = sort_on(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        print(pretty_list(sorted_list))
        print("============= END ===============")

main()
