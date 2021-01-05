import re

class TelefoneBr:
    def __init__(self, tel):
        if self.valida_telefone(tel):
            self.numero = tel
        else:
            raise ValueError("Número Inválido!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)

        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resp = re.search(padrao,self.numero)
        numero_formatado = "+{} ({}) {}-{}".format(resp.group(1),resp.group(2),resp.group(3),resp.group(4))
        return numero_formatado