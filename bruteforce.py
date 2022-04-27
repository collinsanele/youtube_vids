#A python script that uses naive brute force to decrypt pdf files.
#it tries all possible combinations of lowercases and numbers.
#The max_pwd_length is 9 characters but you can always increase it or decrease it.
#The longer the password, the more time it would take.
#The script runs faster if show_attempt=False
#The code link would be in the description below.
#Like and subscribe :)

import itertools
import string
from PyPDF2 import PdfFileReader
from PyPDF2.errors import PdfReadError

def decrypt_pdf(path_to_pdf, password):
    with open(path_to_pdf, "rb") as in_file:
        input_pdf = PdfFileReader(in_file)
        try:
            input_pdf.decrypt(password=password)
            input_pdf.getNumPages()
            return 1

        except PdfReadError:
            "Do nothing"

        return 0


def crack_pdf(show_attempt=False, max_pwd_length=9):
    chars = f"{string.ascii_lowercase} + {string.digits}"
    attempts = 0
    for password_length in range(1, max_pwd_length):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            is_decrypted = decrypt_pdf(path_to_pdf="./output_pdfs/The_Origin_of_Man.pdf", password=guess)
            if is_decrypted:
                print(f'password is {guess}. found in {attempts} guesses.')
                return f'password is {guess}. found in {attempts} guesses.'
            if show_attempt:
                print(guess)


if __name__ == "__main__":
    crack_pdf(show_attempt=True)
