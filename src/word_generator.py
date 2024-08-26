import hashlib

from .helper import get_day_isoformat
from .consts import ENCRYPT_KEY

words = None


def load_words():
    global words
    if words is None:
        words_library = "static/ru_words.txt"
        with open(words_library) as file:
            words = file.read().split()

    return words


def get_code_word():
    words = load_words()
    hash_string = (ENCRYPT_KEY + get_day_isoformat()).encode()
    hash_value = hashlib.md5(hash_string).hexdigest()
    code_word_index = int(hash_value, 16) % len(words)
    return words[code_word_index]
