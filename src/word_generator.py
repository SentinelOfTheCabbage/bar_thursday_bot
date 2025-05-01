import hashlib
import qrcode
from .helper import get_current_time
from .consts import ENCRYPT_KEY

words = None


def load_words():
    global words
    if words is None:
        words_library = "static/ru_words_latinized.txt"
        with open(words_library) as file:
            words = file.read().split()

    return words


def get_code_word():
    words = load_words()
    hash_string = (ENCRYPT_KEY).encode()
    hash_value = hashlib.md5(hash_string).hexdigest()
    code_word_index = int(hash_value, 16) % len(words)
    return words[code_word_index]


def generate_qr_code(code_word: str) -> str:
    output_file = "./static/qrcode.png"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    url_template = 'https://t.me/bar_thursday_bot?start={code_word}'
    qr.add_data(url_template.format(code_word=code_word))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

    return output_file
