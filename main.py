import requests
from acesso_cep import BuscaEndereco

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)

cep = "02461000"
objeto_cep = BuscaEndereco(cep)
#print(objeto_cep)
objeto_cep.acessa_via_cep()