# crie um porgrama que:
# inserir pessoa na lista
# liste o nome de todas as pessoas cadastradas
# pesquise pelo nome de uma pessoa
# ordenar em ordem alfabética
# atualizar nomes
# deletar nome da lista
# sair do programa
import os

lista_nomes = []

while True:
    print('1 - Inserir nome.')
    print('2 - Listar nomes.')
    print('3 - Pesquisar por um nome.')
    print('4 - Ordenar os nomes em ordem alfabética.')
    print('5 - Atualizar um nome.')
    print('6 - Deletar um nome da lista.')
    print('0 - Encerrar o programa.')

    opcao = int(input('Informe a opção desejada:'))

    match opcao:
        case 1:
            novo_nome = input('Novo nome:')
            lista_nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso.\n')
            continue
        case 2:
            for i in range(len(novo_nome)):
                print(f'ID: {i + 1} - {lista_nomes[i]}')
            print('')
            continue
        case 3:
            pesquisa_nome = input('Pesquisar nome: ')
            quantidade = lista_nomes.count(pesquisa_nome)
            try:
                print(f'Encontrado {quantidade} vezes: {pesquisa_nome}\n')
            except:
                print(f'{pesquisa_nome} não encontrado.\n')
                continue
            
        case 4:
            lista_nomes.sort()
            print('Ordenação feita com sucesso.\n')
            continue
        
        case 5:
            id_nome = int(input('Informe o ID do nome a ser alterado: '))
            if id_nome > 0 and id_nome < len(lista_nomes):
                id_nome -= 1
            else:
                print(f'{id_nome} inválido.\n')
                continue
            lista_nomes[id_nome] = input('Informe o novo nome: ')
            print(f'Nome do ID {id_nome + 1} alterado com sucesso.\n')
            continue
        case 6:
            id_nome = int(input('Informe o ID do nome a ser excluído: '))
            if id_nome > 0 and id_nome < len(lista_nomes):
                id_nome -= 1
            else:
                print(f'{id_nome} inválido.\n')
                continue
            del(lista_nomes[id_nome])
            print(f'Nome deletado com sucesso.\n')
            continue
        case 0:
            break

        case _:
            print('Opção inválida.')
            continue

            
        
        
            

