# Created on 9/13/2020 by Anuradha Lal
# This program decrypts a message using the exhaustive key search algorithm utilizing the following functions


def cipher(code, shift_key, function):
    """
    Shifts a given alphabetical code shift_key number of letters in the alphabet. The alphabetical code is
    shifted right or left based on the given function.

    str :param code:
        The code to be mapped to an output
    int :param shift_key:
        The number of letters in the alphabet we are shifting the given code
    function :param function:
        The function that will decide whether to shift the letters in the code right or left.
    str :return:
        The code shifted according to the shift key and the function.
    """

    alphabet = []
    shifted_alphabet = []

    for i in range(0, 26):
        ascii_num = ord('a') + i
        alphabet.append(chr(ascii_num))

        shifted_i = (i + shift_key) % 26
        shifted_ascii_num = ord('a') + shifted_i
        shifted_alphabet.append(chr(shifted_ascii_num))

    alphabet_cipher_dict = function(alphabet, shifted_alphabet)
    final_string = []

    for c in code:
        final_string.append(alphabet_cipher_dict[c])

    return ''.join(final_string)


def dict_a_to_b(a, b):
    return dict(zip(a, b))


def dict_b_to_a(a, b): return dict(zip(b, a))


def encrypt(plain_text, shift_key):
    """
    Encrypts the plain_text using a shift cipher and the given shift_key
    str :param plain_text:
        A lowercase alphabetical string to be encrypted
    int :param shift_key:
        The number of letters in the alphabet we will shift our plain_text by
    str :return:
    The encrypted code for the given plain_text
    """
    return cipher(plain_text, shift_key % 26, dict_a_to_b)


def decrypt(encrypted_text, shift_key):
    """
    Decrypts the encrypted_text using a shift cipher and the given shift_key
    str :param encrypted_text:
        A lowercase alphabetical string to be decrypted
    int :param shift_key:
        The number of letters in the alphabet we will shift our encrypted_text by
    str :return:
    The decrypted message for the given encrypted_text
    """
    return cipher(encrypted_text, shift_key % 26, dict_b_to_a)


def exhaustive_key_search(encrypted_text):
    """
    Decrypts the given text using the shift cipher by attempting all possible keys (i.e. integers from 0-25)
    on the given text.
    str :param encrypted_text:
        A lowercase alphabetical string to be decrypted
    dict, dict :return:
    A dictionary mapping a key to the message produced using that key for decryption.
    """
    key_to_code = {}

    for i in range(0, 26):
        message = decrypt(encrypted_text, i)
        key_to_code[i] = message

    return key_to_code


if __name__ == '__main__':
    print(exhaustive_key_search('BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD'.lower()))
