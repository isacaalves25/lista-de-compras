"""APAGAR DEPOIS:
- função os para todos os sistemas
- verificar se a lista esta vazia antes de mostrar
- verificar se o usuario digitou alguma coisa antes de adicionar a lista
- verificar se o item ja existe
- usar dois excepts oara indice invalido e indice fora do alcance
"""
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


lista_compras = []

while True:

    print('---LISTA DE COMPRAS---')
    indice_escolhido = input(
        '1- Adicionar item | \n'
        '2 - Remover item |\n'
        '3 - Mostrar lista |\n'
        '4 - Sair |\n')

    if indice_escolhido == '1':
        limpar_tela()
        item = input('Digite o item que deseja adicionar: ').lower()

        if item:
            if item not in lista_compras:
                lista_compras.append(item)
                print(f'✅ {item} foi adicionado à lista.')
            else:
                print(f'⚠️ {item} já está na lista.')
        else:
            print('⚠️ Por favor, digite um item válido.')

    elif indice_escolhido == '2':
        limpar_tela()

        if len(lista_compras) == 0:
            print('⚠️ A lista está vazia. Não há itens para remoção.')
        else:
            item = input('Digite o item a ser removido: ').lower()

            if item in lista_compras:
                lista_compras.remove(item)
                print(f'✅ {item} foi removido da lista.')
            else:
                print(f'⚠️ {item} não encontrado na lista.')

    elif indice_escolhido == '3':
        limpar_tela()

        if len(lista_compras) == 0:
            print('⚠️ A lista está vazia.')
        else:
            print('---LISTA DE COMPRAS---')
            for item in lista_compras:
                print(f'- {item}')

    elif indice_escolhido == '4':
        print("Saindo ...")
        break

    else:
        limpar_tela()
        print('❌ Opção inválida! Selecione uma opção válida.')
