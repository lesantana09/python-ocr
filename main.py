from pdf2docx import Converter

class PDFtoDocx:

    @staticmethod
    def convert(path_pdf_file:str, path_doc_file:str):
        cv = Converter(path_pdf_file)
        cv.convert(path_doc_file)
        cv.close()


if __name__ == '__main__':
    PDFtoDocx.convert(
        path_pdf_file= 'files/ficha-inscricao.pdf',
        path_doc_file= 'files/ficha-incricao.docx',
    )