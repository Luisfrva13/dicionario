# Crie um dicionário em Python com os seguintes dados de uma pessoa:
# - Nome
# - CPF
# - RG
# - Data de Nascimento
# - Gênero
# - E-mail
# - Telefone
# - Tipo sanguíneo
# - Profissão
# - Empresa

# O programa deverá exibir os dados da pessoa no console.

# Obs: o usuário deverá informar os dados da pessoa.

import os

pessoas = {'Nome':input('Informe o nome do usuário:'),
         'CPF':input('Informe o CPF do usuário:'),
         'RG':input('Informe o RG do usuário:'),
         'Data de Nascimento':input('Informe a data de nascimento do usuário:'),
         'Gênero':input('Informe o gênero do usuário:'),
         'E-mail':input('Informe o E-mail do usuário:'),
         'Telefone':input('Informe o telefone do usuário:'),
         'Tipo Sanguíneo':input('Informe o tipo sanguíneo do usuário:'),
         'Profissão':input('Informe a profissão do usuário:'),
         'Empresa':input('Informe a empresa do usuário:')}

os.system('cls')

for chave in pessoas:
    print(f'{chave}: {pessoas.get(chave)}')
