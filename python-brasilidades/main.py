# from cpf_cnpj import Documento
# from validate_docbr import CNPJ
from TelefoneBr import TelefoneBr
from datetime import datetime, timedelta
from datas_br import DatasBr
import re
import requests
from acesso_cep import BuscaEndereco

cep = 89135000
obj_cep = BuscaEndereco(cep)
print(obj_cep)

bairro, cidade, ufcod  = obj_cep.acessa_via_cep()
#print(r.text)

print(bairro, cidade, ufcod)






#--------------------------------
# hhoje = DatasBr()
# print("Tempo: ", hhoje.tempo_cadastro())
# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1, hours=20)
# print(hoje - amanha)

#----------------------
# cadastro = DatasBr()
# print(cadastro.momento_cadastro)
# print(cadastro.mes_cadastro())
# print(cadastro.dia_semana())
#
#
# hoje = datetime.today()
# hoje_format = hoje.strftime("%d/%m/%Y %H:%M:%S")
# print(hoje_format)

#-----------------------------------------------------
# telefone = "47988567215"
# tel = TelefoneBr(telefone)
# print(tel)


#------------------------------------------
# cnpj = CNPJ()
#
# new_cnpj = cnpj.generate()
# print(new_cnpj)
# print(cnpj.validate(new_cnpj))

# print(cpf)
# print(cpf.valida_cpf())

#----------------------------------
# cnpj = CNPJ()
# new_cnpj = cnpj.generate()
#
# documento = CpfCnpj(new_cnpj, "cnpj")
# print(documento)

#----------------------------------

# documento = Documento.cria_documento(CNPJ().generate())
# print(documento)
#----------------------------------
# regexp_email = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# texto = 'sabd sckl  guilhermelange@siscobra.com.br asihasjk'
#
# resposta = re.search(regexp_email, texto)
# print(resposta.group())


