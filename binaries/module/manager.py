# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / MODULES
# ///////////////////////////////////////////////////////////////

from .nfsedata import *
from datetime import datetime

# ///////////////////////////////////////////////////////////////
# MESSAGEBOX
# ///////////////////////////////////////////////////////////////


def on_xml_fail():
    if messagebox.showinfo(f"{program_name} | {error}", "Não foi possível ler o arquivo {i}"):
        pass


def on_final(time):
    if messagebox.showinfo(f"{program_name} | {main_name}", f"Todas as notas foram lançadas em {int(time/60)} minuto(s)!"):
        return


def on_xml_bd_fail():
    if messagebox.showinfo(f"{program_name} | {error}", "Dados não foram gravados no Banco de Dados."):
        pass


def get_user(user):
    teste_login = cursor.execute(
        f"""
            SELECT *
            FROM users
            WHERE user= '{user}' 
            """
    )
    teste_login = cursor.fetchall()[0]
    return teste_login


def get_time(start, filial, nota_num):
    final = t.time()
    final_each = final - start
    print(f"{filial} NF {nota_num} foi lançada em {int(final_each)} segundos!")


def sem_pdf(filial, nota_num):
    print(f"*** {filial} NF {nota_num} foi lançada sem o PDF! ***")
    print("_________________________________________________________\n")


def get_timetot():
    time_tot = cursor.execute(
        f"""
        SELECT SUM(time)
        FROM time    
        """
    )
    time_tot = cursor.fetchall()[0][0]
    return time_tot


def get_filestot():
    files_tot = cursor.execute(
        f"""
        SELECT SUM(files)
        FROM time    
        """
    )
    files_tot = cursor.fetchall()[0][0]
    return files_tot


def get_info():
    info = cursor.execute(
        f"""
        SELECT *
        FROM info    
        """
    )
    info = cursor.fetchall()[0]
    return info


def get_db_data():
    notas_xml = cursor.execute(
        f"""
        SELECT * FROM a_nfse_data
        """
    )
    notas_xml = cursor.fetchall()
    return notas_xml

# ///////////////////////////////////////////////////////////////
# MANAGE THE ROUTINE
# ///////////////////////////////////////////////////////////////


def manager(user):
    cont = 1
    start_init = t.time()
    teste_login = get_user(user)
    slack = teste_login[0]
    nome_solicitante = teste_login[1]
    id_solicitante = teste_login[2]
    pdfs_folder = get_pdfonfolder(folder)
    time_tot = get_timetot()
    files_tot = get_filestot()
    info = get_info()
    est_time = time_tot/files_tot
    notas_xml = get_db_data()
    print(f"""
{path}       XML: {len(notas_xml)}  | PDF: {pdfs_folder}
 
INICIANDO ROTINA... PREVISÃO DE TÉRMINO: {int(est_time*len(notas_xml)/60)} MINUTO(S)

            """)
    print("///////////////////////////////////////////////////////////////")
    print(datetime.today().strftime("%d/%m/%Y - %H:%M:%S"))
# ///////////////////////////////////////////////////////////////
# LOOP INIT
# ///////////////////////////////////////////////////////////////
    for nota_xml in notas_xml:
        start = t.time()
        try:
            if OPEN_BROWSER == True:
                init_routine()
                getwindow(cont)
            else:
                pass
            nota_num = nota_xml[0]
            uf = nota_xml[1]
            filial = nota_xml[2]
            razao_social = nota_xml[3]
            grupo_conta1 = info[2]
            grupo_conta2 = info[3]
            descricao = nota_xml[4]
            frequencia = info[0]
            vencimento = nota_xml[5]
            valor = nota_xml[6]
            metodo_pagto = nota_xml[7]
            data = nota_xml[8]
            cod_barras = nota_xml[9]
            info_adicionais = info[1]
            file_name = nota_xml[10]
            print(
                f"\n________________________ Nota {cont} _________________________")
            print(f"{filial} NF {nota_num}")
            if DO_ROUTINE == True:
                routine(
                    nome_solicitante,
                    id_solicitante,
                    slack,
                    uf,
                    filial,
                    razao_social,
                    grupo_conta1,
                    grupo_conta2,
                    descricao,
                    frequencia,
                    vencimento,
                    valor,
                    metodo_pagto,
                    data,
                    cod_barras,
                    info_adicionais
                )
            else:
                pass
            try:
                teste_filename = f"{file_name}.pdf"
                teste_BrasilModal = f"NF BRASIL MODAL {nota_num}.pdf"
                notanum_scapini = nota_num % 100000000000
                teste_SCAPINISUL = f"NF SCAPINISUL {notanum_scapini}.pdf"
                teste_Box = f"NF BOX DELIVERY {nota_num}.pdf"
                teste_Box_boleto = f"BOLETO BOX DELIVERY {nota_num}.pdf"
                pdfs_folder = [os.path.join(file) for file in os.listdir(
                    folder) if file.lower().endswith(".pdf")]

                if teste_filename == teste_BrasilModal or teste_filename == teste_SCAPINISUL:
                    if teste_filename in pdfs_folder:
                        file_select = path + teste_filename
                        print(f"O PDF {filial} NF {nota_num} foi encontrado!")
                        if SELECT_PDF == True:
                            open_file(file_select)
                        else:
                            pass
                        get_time(start, filial, nota_num)
                        print(
                            "_________________________________________________________\n")
                        if SEND_FILES == True:
                            send_file()
                        else:
                            pass
                    else:
                        get_time(start, filial, nota_num)
                        sem_pdf(filial, nota_num)

                elif teste_filename == teste_Box:
                    if teste_filename in pdfs_folder:
                        file_select = path + teste_filename
                        print(f"O PDF {filial} NF {nota_num} foi encontrado!")
                        if SELECT_PDF == True:
                            open_file(file_select)
                            if SEND_FILES == True:
                                send_file()
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                    if teste_Box_boleto in pdfs_folder:
                        file_select = path + teste_Box_boleto
                        print(
                            f"O BOLETO {filial} NF {nota_num} foi encontrado!")
                        if SELECT_PDF == True:
                            open_file(file_select)
                        else:
                            pass
                        get_time(start, filial, nota_num)
                        print(
                            "_________________________________________________________\n")
                        if SEND_FILES == True:
                            send_file()
                        else:
                            pass
                    else:
                        get_time(start, filial, nota_num)
                        print(
                            "_________________________________________________________\n")
            except:
                get_time(start, filial, nota_num)
                print(f"""///////////////////////////////////////////////////////////////  
Erro ao procurar PDF {filial} {nota_num}
///////////////////////////////////////////////////////////////""")
            if REMOVE_FILES == True:
                try:
                    os.remove(f"arquivos\{teste_Box_boleto}")
                except:
                    pass
                try:
                    os.remove(f"arquivos\{file_name}.xml")
                except:
                    pass
                try:
                    os.remove(f"arquivos\{file_name}.pdf")
                except:
                    pass
            else:
                pass
            cont += 1
# ///////////////////////////////////////////////////////////////
# LOOP END
# ///////////////////////////////////////////////////////////////
        except:
            print(f"""///////////////////////////////////////////////////////////////  
Erro ao lançar dados: {nota_xml} 
///////////////////////////////////////////////////////////////""")
            pass
    rest_files()
    if cont != 1:
        final_fin = t.time()
        time_spend = final_fin - start_init
        if SAVE_TIME == True:
            try:
                cursor.execute(
                    f"""
                    INSERT INTO time VALUES(
                    '{time_spend}',
                    '{len(notas_xml)}'
                    )
                    """
                )
                db.commit()
            except:
                pass
        else:
            pass
        print("\n")
        print(datetime.today().strftime("%d/%m/%Y - %H:%M:%S"))
        print("///////////////////////////////////////////////////////////////")
        if DELETE_DATA == True:
            cursor.execute(
                f"""
            DELETE FROM a_nfse_data
            """
            )
            db.commit()
        else:
            pass
    return time_spend
