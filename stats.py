def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
    return f"Found {word_count} total words"

def get_char_usage(filepath):
    char_usage = {}
    with open(filepath) as f:
        file_contents = f.read()
    for word in file_contents.lower():
        char_usage[word] = char_usage.get(word, 0) + 1
    return char_usage

def sort_on(items):
    return items["num"]

def sort_char_usage(Dict) -> list:
    char_list = []
    for word in Dict:
        char_list.append({"char": word, "num": Dict[word]}) 
    char_list.sort(reverse=True, key=sort_on)
    return char_list
