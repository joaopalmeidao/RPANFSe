# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / MODULES / LIBRIRIES
# ///////////////////////////////////////////////////////////////

from xml.dom import minidom
from datetime import date, timedelta
import unidecode
import os

from .var import *
from .request import *
from .readpdf import Read_pdf

# ///////////////////////////////////////////////////////////////
# READ THE XML FILE
# ///////////////////////////////////////////////////////////////


class Read_xml():
    def __init__(self, directory) -> None:
        self.directory = directory

    def all_files(self):
        return [os.path.join(self.directory, file) for file in os.listdir(self.directory)
                if file.lower().endswith(".xml")]

    def format_valor(self, valor):
        if "." in valor:
            valor = valor.split(".")
            if len(valor[1]) < 2:
                return f"{valor[0]},{valor[1]}0"
            else:
                return f"{valor[0]},{valor[1]}"
        else:
            return f"{valor},00"

    def format_filial(self, descricao):
        str(descricao)
        if "entrega rapida na Dark Store" in descricao:
            init = descricao.find("Dark Store")
            fin = descricao.find(" correspondente")
            return descricao[(init+11):fin]

        elif "SCAPINISUL" in descricao:
            init = descricao.find("LOJA")
            descricao = descricao[init:]
            fin = descricao.find("/")
            return descricao[5:fin]

        elif " - Dark Store Ze" in descricao:
            init = descricao.find("Dark Store Ze")
            return descricao[(init+14):]

        else:
            return ""

    def format_vencimento(self, descricao):
        str(descricao)
        if "CNPJ VENCIMENTO" in descricao:
            init = descricao.find("VENCIMENTO ")
            descricao = descricao[init:]
            fin = descricao.find(".")
            vencimento = descricao[11:fin]
            d = vencimento[0:2]
            m = vencimento[3:5]
            a = vencimento[6:10]
            return f"{a}/{m}/{d}"

        elif "Servicos de entrega rapida na Dark Store" in descricao:
            init = descricao.find("Vencimento: ")
            descricao = descricao[init:]
            vencimento = descricao[12:]
            d = vencimento[0:2]
            m = vencimento[3:5]
            a = vencimento[6:10]
            return f"{a}/{m}/{d}"

        elif "ntermediacao de entregas" in descricao:
            init = descricao.find("Vencimento ")
            descricao = descricao[init:]

            if "-" in descricao:
                fin = descricao.find(" -")

            else:
                fin = descricao.find(" Valor Liquido")

            vencimento = descricao[11:fin]
            d = vencimento[0:2]
            m = vencimento[3:5]
            a = vencimento[6:10]
            return f"{a}/{m}/{d}"
        else:
            return ""

    def format_filename(self, file_name):
        str(file_name)
        return file_name[10:-4]

    def check_none(self, var, row):
        try:
            var = var[row].firstChild.data
            var = unidecode.unidecode(var)
            return var
        except:
            return ""

    def format_valorliq(self, descricao):
        init = descricao.find("Valor Liquido R$ ")
        return descricao[(init+17):]

    def format_valorbox(self, valor):
        if "." in valor:
            result = valor.split(".")
            result = result[0]+result[1]
        else:
            result = valor
        result = result.split(",")
        result = result[0]+result[1]
        real = result[:-2]
        cent = result[-2:]
        return f"{real},{cent}"

    def nfse_data(self, xml):
        data = date.today().strftime("%Y/%m/%d")
        file_name = self.format_filename(xml)
        notas = []
        try:
            xml = minidom.parse(xml)
        except:
            return ""
        teste_cnpj_BM_SC = xml.getElementsByTagName("Cnpj")
        teste_cnpj_BM_SC = str(self.check_none(teste_cnpj_BM_SC, 0))

        teste_cnpj_Box = xml.getElementsByTagName("CNPJ")
        teste_cnpj_Box = str(self.check_none(teste_cnpj_Box, 0))

# ///////////////////////////////////////////////////////////////
# NFSE BRASIL MODAL E SCAPINISUL
# ///////////////////////////////////////////////////////////////

        if teste_cnpj_BM_SC == cnpj_BM or teste_cnpj_BM_SC == cnpj_SC or teste_cnpj_BM_SC == cnpj_JP:

            razaoSocial_filial = xml.getElementsByTagName("RazaoSocial")
            razaoSocial_filial = self.check_none(razaoSocial_filial, 1)

            descricao = xml.getElementsByTagName("Discriminacao")
            descricao = self.check_none(descricao, 0)

            numero = xml.getElementsByTagName("Numero")
            numero = self.check_none(numero, 0)

            dataEmissao = xml.getElementsByTagName("DataEmissao")
            dataEmissao = self.check_none(dataEmissao, 0)

            valor = xml.getElementsByTagName("ValorLiquidoNfse")
            valor = self.check_none(valor, 0)

            uf = xml.getElementsByTagName("Uf")
            uf = self.check_none(uf, 1)

            endereco_filial = xml.getElementsByTagName("Endereco")
            endereco_filial = self.check_none(endereco_filial, 3)

            nmr_filial = xml.getElementsByTagName("Numero")
            nmr_filial = self.check_none(nmr_filial, 2)

            bairro_filial = xml.getElementsByTagName("Bairro")
            bairro_filial = self.check_none(bairro_filial, 1)

            cep_filial = xml.getElementsByTagName("Cep")
            cep_filial = self.check_none(cep_filial, 1)

            cnpj_filial = xml.getElementsByTagName("Cnpj")
            cnpj_filial = self.check_none(cnpj_filial, 1)

            cnpj_forn = xml.getElementsByTagName("Cnpj")
            cnpj_forn = self.check_none(cnpj_forn, 0)

            razaoSocial_forn = xml.getElementsByTagName("RazaoSocial")
            razaoSocial_forn = self.check_none(razaoSocial_forn, 0)

            nomeFantasia_forn = xml.getElementsByTagName("NomeFantasia")
            nomeFantasia_forn = self.check_none(nomeFantasia_forn, 0)

            endereco_forn = xml.getElementsByTagName("Endereco")
            endereco_forn = self.check_none(endereco_forn, 1)

            numero_forn = xml.getElementsByTagName("Numero")
            numero_forn = self.check_none(numero_forn, 1)

            uf_forn = xml.getElementsByTagName("Uf")
            uf_forn = self.check_none(uf_forn, 0)

            cep_forn = xml.getElementsByTagName("Cep")
            cep_forn = self.check_none(cep_forn, 0)

            bairro_forn = xml.getElementsByTagName("Bairro")
            bairro_forn = self.check_none(bairro_forn, 0)

            vencimento = date.today() + timedelta(days=2)
            vencimento = vencimento.strftime("%Y/%m/%d")

            filial = descricao
            filial = self.format_filial(filial)

            valor = self.format_valor(valor)

            if filial == Jabaquara:
                filial = "Jabaquara"
            elif filial == santa_luzia:
                filial = "Santa Luzia"
            else:
                pass

            metodo_pagto = "transferencia"

            cod_barras = "."

# ///////////////////////////////////////////////////////////////
# NFSE BOX
# ///////////////////////////////////////////////////////////////

        elif teste_cnpj_Box == cnpj_box:

            razaoSocial_filial = xml.getElementsByTagName("RazaoSocialTomador")
            razaoSocial_filial = self.check_none(razaoSocial_filial, 0)

            descricao = xml.getElementsByTagName("Discriminacao")
            descricao = self.check_none(descricao, 0)

            numero = xml.getElementsByTagName("NumeroNFe")
            numero = self.check_none(numero, 0)

            if numero == "":
                try:
                    numero = file_name.split(" ")
                    numero = numero[3]
                except:
                    numero = ""

            dataEmissao = xml.getElementsByTagName("DataEmissaoNFe")
            dataEmissao = self.check_none(dataEmissao, 1)

            try:
                if "Valor Liquido" in descricao:
                    valor = descricao
                    valor = self.format_valorliq(valor)
                    valor = self.format_valorbox(valor)

                else:
                    valor = xml.getElementsByTagName("ValorServicos")
                    valor = self.check_none(valor, 0)
                    valor = self.format_valor(valor)
            except:
                valor = ""

            uf = xml.getElementsByTagName("UF")
            uf = self.check_none(uf, 1)

            if uf == "":
                try:
                    uf = xml.getElementsByTagName("UF")
                    uf = self.check_none(uf, 0)
                except:
                    uf = ""

            endereco_filial = xml.getElementsByTagName("Logradouro")
            endereco_filial = self.check_none(endereco_filial, 1)

            nmr_filial = xml.getElementsByTagName("NumeroEndereco")
            nmr_filial = self.check_none(nmr_filial, 1)

            bairro_filial = xml.getElementsByTagName("Bairro")
            bairro_filial = self.check_none(bairro_filial, 1)

            cep_filial = xml.getElementsByTagName("CEP")
            cep_filial = self.check_none(cep_filial, 1)

            cnpj_filial = xml.getElementsByTagName("CNPJ")
            cnpj_filial = self.check_none(cnpj_filial, 1)

            cnpj_forn = xml.getElementsByTagName("CNPJ")
            cnpj_forn = self.check_none(cnpj_forn, 0)

            razaoSocial_forn = xml.getElementsByTagName("RazaoSocialPrestador")
            razaoSocial_forn = self.check_none(razaoSocial_forn, 0)

            if razaoSocial_forn == "":
                razaoSocial_forn = ""

            endereco_forn = xml.getElementsByTagName("Logradouro")
            endereco_forn = self.check_none(endereco_forn, 0)

            numero_forn = xml.getElementsByTagName("NumeroEndereco")
            numero_forn = self.check_none(numero_forn, 0)

            uf_forn = xml.getElementsByTagName("UF")
            uf_forn = self.check_none(uf_forn, 0)

            cep_forn = xml.getElementsByTagName("CEP")
            cep_forn = self.check_none(cep_forn, 0)

            bairro_forn = xml.getElementsByTagName("Bairro")
            bairro_forn = self.check_none(bairro_forn, 0)

            vencimento = descricao
            vencimento = self.format_vencimento(vencimento)

            try:
                file = f"BOLETO BOX DELIVERY {numero}.pdf"
                pdf = Read_pdf(self.directory)
                try:
                    pdf_text = pdf.pdf_data(file)
                    try:
                        pdf_text = pdf_text[0]
                        cod_barras = pdf_text[1]
                    except:
                        print(
                            "///////////////////////////////////////////////////////////////")
                        print(
                            f"Erro ao ler {self.directory+file} VERIFICAR PDF")
                        print(
                            "///////////////////////////////////////////////////////////////")
                        cod_barras = ""
                except:
                    print(
                        "///////////////////////////////////////////////////////////////")
                    print(f"Não encontrei {self.directory+file}")
                    print(
                        "///////////////////////////////////////////////////////////////")
                    cod_barras = ""
            except:
                cod_barras = ""

            filial = descricao

            if "Dark Store Ze" in filial:
                try:
                    filial = self.format_filial(filial)
                    if filial == cdd_centro:
                        filial = "Cdd Centro"
                    else:
                        pass
                except:
                    filial = ""

            elif "Intermediacao de entregas Ze" in filial:
                try:
                    fin = filial.find(".")
                    ini = filial.find("Ze ")
                    filial = filial[ini+3:fin]
                except:
                    filial = ""

            else:
                if bairro_filial == garcia:
                    filial = "Garcia"
                elif bairro_filial == ciddade_nova:
                    filial = "Cidade Nova"
                elif bairro_filial == betim:
                    filial = "Betim"
                elif bairro_filial == savassi:
                    filial = "Savassi"
                elif bairro_filial == barreiro:
                    filial = "Barreiro"
                elif bairro_filial == sao_cristovao:
                    filial = "Sao Cristovao"
                elif bairro_filial == trindade:
                    filial = "Trindade"
                elif bairro_filial == sulacap:
                    filial = "Sulacap"
                elif bairro_filial == vila_prudente:
                    filial = "Vila Prudente"
                elif bairro_filial == freguesia:
                    filial = "Freguesia"
                elif bairro_filial == jardim_celeste:
                    filial = "Jardim Celeste"
                elif bairro_filial == jardim_stella:
                    filial = "Jardim Stella"
                elif bairro_filial == itaquera:
                    filial = "Itaquera"
                elif bairro_filial == jk:
                    filial = "JK"
                elif bairro_filial == embu:
                    filial = "Embu"
                elif bairro_filial == gonzaga:
                    filial = "Gonzaga"
                elif bairro_filial == cipava:
                    filial = "Cipava"
                elif bairro_filial == maria_estela:
                    filial = "Maria Estela"
                elif bairro_filial == sao_mateus:
                    filial = "Sao Mateus"
                elif bairro_filial == jardim_satelite:
                    filial = "Jardim Satelite"
                else:
                    filial = bairro_filial

            nomeFantasia_forn = ""
            metodo_pagto = "boleto"

        else:
            try:
                dadosforn = consulta_cnpj(str(teste_cnpj_BM_SC))
                razaoSocial_forn = dadosforn["nome"]
                print(f"Fornecedor {razaoSocial_forn} não Cadastrado!")
            except:
                try:
                    dadosforn = consulta_cnpj(str(teste_cnpj_Box))
                    razaoSocial_forn = dadosforn["nome"]
                    print(f"Fornecedor {razaoSocial_forn} não Cadastrado!")
                except:
                    print(f"Fornecedor não Cadastrado!")
            pass

        dados = (
            razaoSocial_filial,  # 0
            filial,  # 1
            data,  # 2
            vencimento,  # 3
            uf,  # 4
            valor,  # 5
            descricao,  # 6
            numero,  # 7
            file_name,  # 8
            dataEmissao,  # 9
            endereco_filial,  # 10
            nmr_filial,  # 11
            bairro_filial,  # 12
            cep_filial,  # 13
            cnpj_filial,  # 14
            cnpj_forn,  # 15
            razaoSocial_forn,  # 16
            nomeFantasia_forn,  # 17
            endereco_forn,  # 18
            numero_forn,  # 19
            bairro_forn,  # 20
            uf_forn,  # 21
            cep_forn,  # 22
            metodo_pagto,  # 23
            cod_barras  # 24
        )
        notas.append(dados)
        return notas


if __name__ == "__main__":
    xml = Read_xml(r"arquivos\\")
    all = xml.all_files()
    for i in all:
        result = xml.nfse_data(i)
        print(result)
