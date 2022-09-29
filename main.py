import requests
from acesso_cep import BuscaEndereco

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)

cep = "02461000"
objeto_cep = BuscaEndereco(cep)
#print(objeto_cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(f'bairro: {bairro}, cidade: {cidade}, uf: {uf}')