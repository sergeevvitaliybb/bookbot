import sys
from stats import get_num_words
from stats import total_characters_count
from stats import listed_chars
from stats import sort_on


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_in_text = total_characters_count(text)
        list_of_dicts = listed_chars(chars_in_text)
        list_of_dicts.sort(reverse=True, key=sort_on)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dict in list_of_dicts:
            if dict["char"].isalpha():
                print (f'{dict["char"]}: {dict["num"]}')
        print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()