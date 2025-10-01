from stats import *
import sys 
def main(): 
    try:
        book = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    char_usage = get_char_usage(book)
    sort_chars = sort_char_usage(char_usage)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book)
    print("----------- Word Count ----------")
    print(get_num_words(book))
    print("--------- Character Count -------")
    for word in sort_chars:
        if word["char"].isalpha():
            print(f"{word["char"]}: {word["num"]}")
        else:
            continue
    print("============= END ===============")
    return None
main()
