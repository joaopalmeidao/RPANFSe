# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / MODULES
# ///////////////////////////////////////////////////////////////

from .database import *
from .utils import *
from .sys import *
from .readxml import *

# ///////////////////////////////////////////////////////////////
# GET NFSE DATA
# ///////////////////////////////////////////////////////////////


def nfse_data():
    try:
        cursor.execute(
            f"""
            DELETE FROM a_nfse_data
            """
        )
        db.commit()
        print(f"""\n///////////////////////////////////////////////////////////////
GRAVANDO DADOS DE TODAS AS NFSE EM
{path}
NA TABELA a_nfse_data DO BANCO DE DADOS C:\\RPA NFSe\\{DataBase}.bd
///////////////////////////////////////////////////////////////
                """)
    except:
        on_db_fail()
    xml = Read_xml(folder)
    notas_xml = xml.all_files()
    start = t.time()
    cont = 0
    for i in notas_xml:
        # try:
        print(i)
        nota_xml = xml.nfse_data(i)
        nota_xml = nota_xml[0]
        nota_num = int(nota_xml[7])
        uf = nota_xml[4]
        filial = nota_xml[1]
        razao_social = nota_xml[16]
        descricao = nota_xml[6]
        vencimento = nota_xml[3]
        valor = nota_xml[5]
        metodo_pagto = nota_xml[23]
        data = nota_xml[2]
        cod_barras = nota_xml[24]
        file_name = nota_xml[8]
        cursor.execute(
            f"""
                INSERT INTO a_nfse_data VALUES(
                '{nota_num}',   
                '{uf}',
                '{filial}',
                '{razao_social}',
                '{descricao}',
                '{vencimento}',
                '{valor}',
                '{metodo_pagto}',
                '{data}',
                '{cod_barras}',
                '{file_name}'
                )
                """
        )
        db.commit()
        final_each = t.time()
        cont += 1
        time = int(final_each - start)

#         except:
#             print(f"""///////////////////////////////////////////////////////////////
# Erro ao ler {i}
# ///////////////////////////////////////////////////////////////""")
#         if SAVE_NFSE_DB == True:
#             try:
#                 cursor.execute(
#                     f"""
#                     INSERT INTO xml_nfse VALUES(
#                     '{nota_xml[0]}',
#                     '{nota_xml[1]}',
#                     '{nota_xml[2]}',
#                     '{nota_xml[3]}',
#                     '{nota_xml[4]}',
#                     '{nota_xml[5]}',
#                     '{nota_xml[6]}',
#                     '{nota_xml[7]}',
#                     '{nota_xml[8]}',
#                     '{nota_xml[9]}',
#                     '{nota_xml[10]}',
#                     '{nota_xml[11]}',
#                     '{nota_xml[12]}',
#                     '{nota_xml[13]}',
#                     '{nota_xml[14]}',
#                     '{nota_xml[15]}',
#                     '{nota_xml[16]}',
#                     '{nota_xml[17]}',
#                     '{nota_xml[18]}',
#                     '{nota_xml[19]}',
#                     '{nota_xml[20]}',
#                     '{nota_xml[21]}',
#                     '{nota_xml[22]}',
#                     '{nota_xml[23]}',
#                     '{nota_xml[24]}'
#                     )
#                     """
#                 )
#                 db.commit()
#             except:
#                 pass
#         else:
#             pass
#     db.commit()
#     print(f"""\n///////////////////////////////////////////////////////////////
# {cont} NOTA(S) COLETADAS
# # ///////////////////////////////////////////////////////////////""")
