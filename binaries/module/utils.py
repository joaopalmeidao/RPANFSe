# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / LIBRIRIES
# ///////////////////////////////////////////////////////////////

import webbrowser as wbb
import pyautogui as pa
import pygetwindow as pw
import time as t

# ///////////////////////////////////////////////////////////////
# GLOBAL VARIABLES
# ///////////////////////////////////////////////////////////////

icon_folder = r"binaries\\icon\\"

help = "help"
whatsapp = "https://api.whatsapp.com/send?phone=5531993702136"
LinkedIn = "https://www.linkedin.com/in/jo%C3%A3o-pedro-a-oliveira-a51551237/"
atlassian = "https://zedelivery.atlassian.net/servicedesk/customer/portal/5/group/18"

# ///////////////////////////////////////////////////////////////
# OPEN THE BROWSER ATLASSIAN
# ///////////////////////////////////////////////////////////////


def init_routine():
    wbb.open_new(atlassian)

# ///////////////////////////////////////////////////////////////
# PYAUTOGUI
# ///////////////////////////////////////////////////////////////


def getwindow(cont):
    if cont == 1:
        t.sleep(5)
        window = pw.getActiveWindow()
        window.maximize()
    else:
        pass
    t.sleep(3)
    open_pagamentos()


def press(button, presses):
    t.sleep(0.1)
    while presses != 0:
        pa.press(button)
        t.sleep(0.1)
        presses -= 1


def open_pagamentos():
    press("tab", 8)
    pa.press("enter")
    t.sleep(1)
    press("tab", 2)


def open_file(file_select):
    pa.press("enter")
    t.sleep(10)
    pa.write(file_select)
    t.sleep(0.2)
    pa.press("enter")
    t.sleep(10)


def send_file():
    t.sleep(3)
    press("tab", 2)
    t.sleep(0.1)
    press("enter")


def routine(
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
):
    t.sleep(0.1)
    pa.write(nome_solicitante)
    pa.press("tab")
    t.sleep(0.1)
    pa.write(id_solicitante)
    pa.press("tab")
    t.sleep(0.1)
    pa.write(slack)
    pa.press("tab")
    t.sleep(0.1)
    pa.write(uf)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.2)
    pa.write(filial)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.2)
    pa.write(razao_social)
    t.sleep(0.5)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.1)
    pa.write(grupo_conta1)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.2)
    pa.write(grupo_conta2)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.2)
    pa.write(descricao)
    pa.press("tab")
    t.sleep(0.1)
    pa.write(frequencia)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.1)
    pa.write(vencimento)
    t.sleep(0.5)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.1)
    pa.write(valor)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.1)
    pa.write(metodo_pagto)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.1)
    pa.write(data)
    t.sleep(0.5)
    pa.press("enter")
    pa.press("tab")
    t.sleep(0.1)
    pa.write(cod_barras)
    pa.press("tab")
    t.sleep(0.1)
    pa.write(info_adicionais)
    t.sleep(0.1)
    pa.press("tab")
    pa.press("tab")
