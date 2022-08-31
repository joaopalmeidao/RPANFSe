# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / LIBRIRIES
# ///////////////////////////////////////////////////////////////

import os

from .config import *

# ///////////////////////////////////////////////////////////////
# DONT CHANGE
# ///////////////////////////////////////////////////////////////

folder = r"arquivos\\"
path = f"C:\\RPA NFSe\\arquivos\\"

# ///////////////////////////////////////////////////////////////
# OUTRAS FUNCOES
# ///////////////////////////////////////////////////////////////


def del_otherfiles():
    for file in os.listdir(folder):
        if file.lower().endswith(".xml") or file.lower().endswith(".pdf"):
            pass
        else:
            os.remove(file)


def rest_files():
    arqfolder = os.listdir(folder)
    if len(arqfolder) != 0:
        print("""///////////////////////////////////////////////////////////////
Os arquivos abaixo continuam na pasta "arquivos":
""")
        for file in arqfolder:
            print(f"{file}")


def get_xmlonfolder(folder):
    xmls_onfolder = [os.path.join(file) for file in os.listdir(
        folder) if file.lower().endswith(".xml")]
    return len(xmls_onfolder)


def get_pdfonfolder(folder):
    pdfs_onfolder = [os.path.join(file) for file in os.listdir(
        folder) if file.lower().endswith(".pdf")]
    return len(pdfs_onfolder)

# ///////////////////////////////////////////////////////////////
# TREAT XML
# ///////////////////////////////////////////////////////////////


def rename_file():
    for file in os.listdir(folder):

        if file.lower().endswith(".xml"):
            if "NFSe_E_" in file:
                try:
                    if " " in file:
                        file.replace(" ", "")
                    else:
                        pass
                    old_name = folder + file
                    new_file = file.split("_")
                    fin = new_file[3]
                    fin = fin[0:-4]
                    try:
                        fin = int(fin)
                    except:
                        pass
                    try:
                        fin = fin.split(" ")
                        fin = fin[0]
                        fin = int(fin)
                    except:
                        pass
                    file_name = f"NF BRASIL MODAL {fin}.xml"
                    new_name = folder + file_name
                    try:
                        os.rename(old_name, new_name)
                    except:
                        if REMOVE_REPEATED == True:
                            os.remove(old_name)
                            print(
                                f"O arquivo {file} foi removido da pasta, arquivo repetido.")
                            pass
                        else:
                            pass
                except:
                    pass
            elif "nfse_20" in file:
                try:
                    if " " in file:
                        file.replace(" ", "")
                    else:
                        pass
                    old_name = folder + file
                    new_file = file.split("_")
                    fin = new_file[1]
                    fin = fin[0:-4]
                    fin = int(fin) % 100000000000
                    file_name = f"NF SCAPINISUL {fin}.xml"
                    new_name = folder + file_name
                    try:
                        os.rename(old_name, new_name)
                    except:
                        if REMOVE_REPEATED == True:
                            os.remove(old_name)
                            print(
                                f"O arquivo {file} foi removido da pasta, arquivo repetido.")
                            pass
                        else:
                            pass
                except:
                    pass
            elif "nfse_resposta" in file or "enviar_rps_solicitacao":
                try:
                    if " " in file:
                        file.replace(" ", "")
                    else:
                        pass
                    old_name = folder + file
                    new_file = file.split("_")
                    fin = new_file[1]
                    fin = int(fin)
                    file_name = f"NF BOX DELIVERY {fin}.xml"
                    new_name = folder + file_name
                    try:
                        os.rename(old_name, new_name)
                    except:
                        if REMOVE_REPEATED == True:
                            os.remove(old_name)
                            print(
                                f"O arquivo {file} foi removido da pasta, arquivo repetido.")
                            pass
                        else:
                            pass
                except:
                    pass
            else:
                pass

# ///////////////////////////////////////////////////////////////
# TREAT PDF
# ///////////////////////////////////////////////////////////////

        elif file.lower().endswith(".pdf"):
            if "Zé Delivery" in file:
                try:
                    old_name = folder + file
                    nr_nota = file.split(" ")
                    fin = nr_nota[1]
                    file_name = f"NF BRASIL MODAL {fin}.pdf"
                    new_name = folder + file_name
                    try:
                        os.rename(old_name, new_name)
                    except:
                        if REMOVE_REPEATED == True:
                            os.remove(old_name)
                            print(
                                f"O arquivo {file} foi removido da pasta, arquivo repetido.")
                            pass
                        else:
                            pass
                except:
                    pass
            elif "NFSE" in file:
                try:
                    old_name = folder + file
                    nr_nota = file.split(" ")
                    fin = nr_nota[1]
                    file_name = f"NF SCAPINISUL {fin}.pdf"
                    new_name = folder + file_name
                    try:
                        os.rename(old_name, new_name)
                    except:
                        if REMOVE_REPEATED == True:
                            os.remove(old_name)
                            print(
                                f"O arquivo {file} foi removido da pasta, arquivo repetido.")
                            pass
                        else:
                            pass
                except:
                    pass
            elif "boleto" in file.lower():
                try:
                    if " " in file:
                        file.replace(" ", "")
                    else:
                        pass
                    old_name = folder + file
                    nr_nota = file.split("-")
                    fin = nr_nota[1]
                    fin = int(fin)
                    file_name = f"BOLETO BOX DELIVERY {fin}.pdf"
                    new_name = folder + file_name
                    try:
                        os.rename(old_name, new_name)
                    except:
                        if REMOVE_REPEATED == True:
                            os.remove(old_name)
                            print(
                                f"O arquivo {file} foi removido da pasta, arquivo repetido.")
                            pass
                        else:
                            pass
                except:
                    pass
            elif "NFS " in file:
                try:
                    if " " in file:
                        file.replace(" ", "")
                    else:
                        pass
                    old_name = folder + file
                    nr_nota = file.split("-")
                    fin = nr_nota[1]
                    fin = int(fin)
                    file_name = f"NF BOX DELIVERY {fin}.pdf"
                    new_name = folder + file_name
                    try:
                        os.rename(old_name, new_name)
                    except:
                        if REMOVE_REPEATED == True:
                            os.remove(old_name)
                            print(
                                f"O arquivo {file} foi removido da pasta, arquivo repetido.")
                            pass
                        else:
                            pass
                except:
                    pass
            else:
                pass
    print()
