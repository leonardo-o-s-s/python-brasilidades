from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ


# cpf_um = Cpf("15316264754")
# print(cpf_um)

exemplo_cnpj = "10360842000108"
exemplo_cpf = "47913825871"
# cnpj = CNPJ()
# print(cnpj.validate((exemplo_cnpj)))
documento = CpfCnpj(exemplo_cnpj, "cnpj")
print(documento)
documento2 = CpfCnpj(exemplo_cpf, "cpf")
print(documento2)