from validate_docbr import CPF
from validate_docbr import CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Doc_Cpf(documento)
        elif len(documento) == 14:
            return Doc_Cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta.")

class Doc_Cpf:
    def __init__(self, documento):
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!")

    def valida_cpf(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format()

class Doc_Cnpj:

    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!")

    def valida_cnpj(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format()