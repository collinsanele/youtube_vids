#The code link would be in the video description
#pip install PyPDF2

from PyPDF2 import PdfFileReader, PdfFileWriter

def encrypt_pdf(password, path_to_dir, dest_path):
    #dest_path is the path to the encrypted pdf file
    with open(path_to_dir, "rb") as in_file:
        input_pdf = PdfFileReader(in_file)
        output_pdf = PdfFileWriter()
        output_pdf.appendPagesFromReader(input_pdf)
        output_pdf.encrypt(password)

        with open(dest_path, "wb") as out_file:
            output_pdf.write(out_file)

#run script in the terminal 'encrypt_pdf.py'

if __name__ == "__main__":
    encrypt_pdf(password="cool", path_to_dir="./input_pdfs/The_Origin_of_Man.pdf", dest_path="./output_pdfs/The_Origin_of_Man.pdf")
