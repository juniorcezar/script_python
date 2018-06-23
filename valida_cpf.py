'''
Autor: Junior Cezar dos Santos
Data: 23/06/2018
Versão do Python: 3.6.5
Algoritmo utilizado: https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
Gerador de cpf: https://www.4devs.com.br/gerador_de_cpf
Lembrem-se este algoritmo serve apenas para estudo!!!
'''
# Pedir para o usuário digitar um cpf, contendo apenas numeros

entra_cpf = input("Digite somente numeros: ")

# Transformando esse cpf em uma lista com list comprehensions

cpf = [int(x) for x in entra_cpf]

# 1º parte, calcular o primeiro digito verificador do cpf
'''
Validação do primeiro dígito
Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente de números de 10 à 2 e soma os resultados.
'''
seq_um = [10,9,8,7,6,5,4,3,2]
soma_um = 0
for x in range(len(cpf[0:9])):
    soma_um = (cpf[x] * seq_um[x]) + soma_um

resultado_um = soma_um * 10 % 11

if resultado_um == 10:
    resultado_um = 0
    
# print(resultado_um)

# 2º parte, calcular o segundo digito verificador do cpf
'''
A validação do segundo dígito é semelhante à primeira, porém vamos considerar os 9 primeiros dígitos,
mais o primeiro dígito verificador, e vamos multiplicar esses 10 números pela sequencia decrescente de 11 a 2.
'''
seq_dois = [11,10,9,8,7,6,5,4,3,2]
soma_dois = 0
for x in range(len(cpf[0:10])):
    soma_dois = (cpf[x] * seq_dois[x]) + soma_dois

resultado_dois = soma_dois * 10 % 11

# Printa na tela se o cpf é valido
if cpf[-2] == resultado_um and cpf[-1] == resultado_dois:
    print("O cpf é valido")
