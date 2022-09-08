# ///////////////////////////////////////////////////////////////
#
# BY: JOAO PEDRO A. OLIVEIRA
#
# ///////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////
# IMPORT / LIBRIRIES
# ///////////////////////////////////////////////////////////////

import requests
import json

# ///////////////////////////////////////////////////////////////
# API CNPJ
# ///////////////////////////////////////////////////////////////


def consulta_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
                   "cnpj": "06990590000123", "plugin": "RF"}
    response = requests.request("GET", url, params=querystring)
    result = json.loads(response.text)
    return result


if __name__ == "__main__":
    try:
        consulta = consulta_cnpj('47193456000189')
        print(consulta['nome'])

        print(consulta)
    except:
        print("Aguarde 1 minuto para tentar novamente.")
