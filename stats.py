def word_count(text):
    return len(text.split())

def char_count(text):
    lowercase_text = text.lower()
    split_text = lowercase_text.split()
    chars_dict = {}
    for word in split_text:
        for char in word:
            if (char in chars_dict):
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1

    return dict(chars_dict.items())

def sort_on(items):
    return items['num']

def sort_dictionaries(dictionary):
    list_of_dicts = list()
    for record in list(dictionary):
        list_of_dicts.append({'char': record, 'num': dictionary[record]})

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def words_frequency(text):
    lowercase_text = text.lower()
    split_text = lowercase_text.split()
    words_dict = {}
    for word in split_text:
        if (word in words_dict):
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    return dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))