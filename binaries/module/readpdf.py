# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / MODULES / LIBRIRIES
# ///////////////////////////////////////////////////////////////

import os
import pdfplumber

# ///////////////////////////////////////////////////////////////
# READ THE PDF FILE
# ///////////////////////////////////////////////////////////////


class Read_pdf():
    def __init__(self, directory) -> None:
        self.directory = directory

    def all_files(self):
        return [os.path.join(self.directory, file) for file in os.listdir(self.directory)
                if file.lower().endswith('.pdf')]

    def format_codbarras(self, page):
        str(page)
        if 'Recibo do Pagador' in page:
            init = page.find('Recibo do Pagador')
            fin = page.find('Beneficiário')
            cod_barras = page[(init+23):fin]
            cod_barras = cod_barras.replace("\n", "").replace(" ", "")
            cod_barras = cod_barras.replace(".", "")
            return cod_barras
        else:
            return ""

    def format_filename(self, file_name):
        str(file_name)
        return file_name[10:]

    def pdf_data(self, pdf):
        file_name = self.format_filename(pdf)
        page = []
        open_pdf = pdfplumber.open(self.directory+pdf)
        pdf_text = open_pdf.pages[0].extract_text()
        cod_barras = self.format_codbarras(pdf_text)

        dados = (
            file_name,
            cod_barras
        )
        page.append(dados)
        return page


if __name__ == "__main__":
    pdf = Read_pdf(r"arquivos\\")
    all = pdf.all_files()
    for i in all:
        result = pdf.pdf_data(i)
        print(result)
