def get_popular_words(string, words_number=1):
    string = string.lower()
    characters_to_remove = '.,:;!"'"?'"'(){}[]-—_@#$%^&*№/\\|~'
    for character in characters_to_remove:
        string = string.replace(character, "")
    words_array = string.split()

    dictionary = dict()
    for word in words_array:
        dictionary[word] = dictionary.get(word, 0) + 1

    result = []
    for key, value in dictionary.items():
        result.append((value, key))
    result.sort()
    result.reverse()
    for i in range(words_number):
        if i < len(result):
            print(result[i][1])


if __name__ == '__main__':
    input_string = input()
    N = int(input())
    get_popular_words(input_string, N)
