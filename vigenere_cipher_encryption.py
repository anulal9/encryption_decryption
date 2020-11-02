import operator


def map_alphabet_to_position():
    """
    Creates a dictionary that maps the letters of the alphabet to their position
    :return: dict
        A dictionary mapping letters of the alphabet to their position
    """
    dict_alphabet_to_pos = {}

    for i in range(26):
        letter = chr(ord('a') + i)
        dict_alphabet_to_pos[letter] = i

    return dict_alphabet_to_pos


def map_position_to_alphabet():
    """
    Creates a dictionary that maps the position of letters in the alphabet, to the letters
    :return: dict
        A dictionary mapping the position of letters in the alphabet, to the letters
    """
    dict_pos_to_alphabet = {}

    for i in range(26):
        letter = chr(ord('a') + i)
        dict_pos_to_alphabet[i] = letter

    return dict_pos_to_alphabet


def get_letter_from_num(num):
    """
    Get's the letter that corresponds to the given position in the alphabet
    :param num: int
        position of letter in alphabet
    :return: char
        The corresponding letter in the alphabet
    """
    dict_alph = map_position_to_alphabet()

    return dict_alph[num % 26]


def get_num_from_letter(letter):
    """
    Get's the position that corresponds to the given letter in the alphabet
    :param letter: char
        letter in alphabet
    :return: int
        The corresponding position of the letter in the alphabet
    """
    dict_pos = map_alphabet_to_position()
    return dict_pos[letter]


def get_nums_from_sequence(sequence):
    """
    For each letter in the given sequence, gets the position of the letter in the
        alphabet
    :param sequence: str
        string of lowercase letters in alphabet
    :return: list-of int
        The corresponding positions of the letters in the sequence, in the alphabet
    """
    nums = [get_num_from_letter(letter) for letter in sequence]

    return nums


def get_letters_from_sequence(sequence):
    """
    For each number in the given sequence, gets the corresponding letter in the
        alphabet
    :param sequence: str
        string of lowercase integers, corresponding to positions in the alphabet
    :return: list-of char
        The letters in the alphabet, that correspond to the positions in the sequence
    """
    letters = [get_letter_from_num(num) for num in sequence]
    return letters


def map_vigenere(text, key, func):
    key_length = len(key)
    enumerated_text = enumerate(text)
    result = []

    for i, letter in enumerated_text:
        key_index = i % key_length
        key_letter = key[key_index]
        result.append(manipulate_letters(letter, key_letter, func))

    string_result = ''.join(result)

    return string_result


def manipulate_letters(letter_a, letter_b, func):
    num_a = get_num_from_letter(letter_a)
    num_b = get_num_from_letter(letter_b)

    num_c = func(num_a, num_b) % 26

    result_letter = get_letter_from_num(num_c)

    return result_letter

def standard_frequency_analysis(letter_to_frequency, num_of_chars):

    min_diff = 1
    best_g = None
    best_mg = 0
    possible_gs = []
    possible_mgs = []
    possible_keys = []

    y_num = get_num_from_letter('y')

    for g in range(25):
        mg = 0
        for letter in letter_to_frequency:
            i = get_num_from_letter(letter)
            possible_pt = get_letter_from_num((i+g)%26)
            if possible_pt in letter_to_frequency:
                pi = letter_to_frequency[letter]/ num_of_chars
                fp_n = letter_to_frequency[possible_pt]/num_of_chars
                mg += (pi * fp_n)
        if g == y_num:
            print(mg)

        if abs(mg-0.065) < min_diff:
            min_diff = abs(mg-0.065)
            best_g = g
            best_mg = mg
        if abs(mg-0.065) < 0.01:
            possible_gs.append(g)
            possible_mgs.append(mg)
            possible_keys.append(get_letter_from_num(g))

    key = get_letter_from_num(best_g)
    return best_g, best_mg, key, possible_keys, possible_mgs


def get_shift_cipher_strings_from_vigenere(key_length, string):
    dict_equiv_class_to_string = {}

    for i, c in enumerate(string):
        i = i + 1
        equiv_class = i % key_length
        if equiv_class in dict_equiv_class_to_string:
            ec_string = dict_equiv_class_to_string[equiv_class]
            ec_string = ec_string + c
            dict_equiv_class_to_string[equiv_class] = ec_string
        else:
            dict_equiv_class_to_string[equiv_class] = c

    return dict_equiv_class_to_string


def count_frequency_of_letters(string):
    dict_letter_to_frequency = {}

    for s in string:
        if s in dict_letter_to_frequency:
            prev_count = dict_letter_to_frequency[s]
            count = prev_count + 1
            dict_letter_to_frequency[s] = count
        else:
            dict_letter_to_frequency[s] = 1

    return dict_letter_to_frequency


def count_frequencies_of_shift_cipher_strings(letter_to_frequency_dict):
    key_to_frequency_dict = {}
    for key, value in letter_to_frequency_dict.items():
        key_to_frequency_dict[value] = [count_frequency_of_letters(value)]

    return key_to_frequency_dict



def encrypt_vigenere(plain_text, key):
    return map_vigenere(plain_text.lower().replace(' ', ''), key, operator.add)


def decrypt_vigenere(cipher_text, key):
    return map_vigenere(cipher_text.lower().replace(' ', ''), key, operator.sub)


if __name__ == '__main__':
    freq_result = count_frequency_of_letters('KHQWGIZMGKPOYRKHUITDUXLXCWZOTWPAHFOHMGFEVUEJJ')
    print(len('KHQWGIZMGKPOYRKHUITDUXLXCWZOTWPAHFOHMGFEVUEJJ'))
    print(freq_result)
    '''
    result_dict = get_shift_cipher_strings_from_vigenere(4, 'BCRRBCQORHKEPSLSLCWRWXXDESPEZMPYQWCEBCBOSFHCIZHSQWVHCBRWRVLNEGDRCKRRQS')
    print(result_dict)

    frequency_result = count_frequency_of_letters('BBRPLWEZQBSIQCRECQ')
    print(frequency_result)

    key_to_frequency_dict = count_frequencies_of_shift_cipher_strings(result_dict)
    print(key_to_frequency_dict)
    '''

    '''
    letter_to_frequency = {'b': 3, 'r': 2, 'p': 1, 'l': 1, 'w': 1, 'e': 2,
                           'z': 1, 'q': 3, 's': 1, 'i': 1, 'c': 2}

    best_g, best_mg, key, possible_keys, possible_mgs = standard_frequency_analysis(letter_to_frequency, 18)
    print(best_g, best_mg, key, possible_keys, possible_mgs)

    letter_to_frequency_2 = {'c': 4, 'h': 1, 's': 3, 'x': 1, 'm': 1, 'w': 2, 'f': 1, 'z': 1,
                             'b': 1, 'v': 1, 'k': 1, 'g': 1}

    best_g, best_mg, key, possible_keys, possible_mgs = standard_frequency_analysis(letter_to_frequency_2, 18)
    print(best_g, best_mg, key, possible_keys, possible_mgs)

    letter_to_frequency_3 = {'r': 2, 'q': 1, 'k': 1, 'l': 2, 'w': 1, 'x': 1, 'p': 2, 'e': 1, 'b': 1, 'h': 2, 'v': 1}
    best_g, best_mg, key, possible_keys, possible_mgs= standard_frequency_analysis(letter_to_frequency_3, 18)
    print(best_g, best_mg, key, possible_keys, possible_mgs)

    letter_to_frequency_4 = {'r': 4, 'o': 2, 'e': 3, 's': 2, 'd': 1, 'y': 1, 'c': 1, 'h':1, 'w': 1, 'n': 1}
    best_g, best_mg, key, possible_keys, possible_mgs = standard_frequency_analysis(letter_to_frequency_4, 13)
    print(best_g, best_mg, key, possible_keys, possible_mgs)

    print(get_nums_from_sequence('GENMANCMNJWQHF'.lower()))
    print(get_nums_from_sequence('KARLA'.lower()))

    result = decrypt_vigenere('BCRRBCQORHKEPSLSLCWRWXXDESPEZMPYQWCEBCBOSFHCIZHSQWVHCBRWRVLNEGDRCKRRQS', 'okad')
    print(result)
    '''