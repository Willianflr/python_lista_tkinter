"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e
listar valores da sua lista
Não permita que o programa quebre com erros de
índices inexistentes na lista 
"""

import os

print('BEM VINDO AO SOFTWARE DO MARCOSW77_')

# Inicia a lista de compras
lista = []

def menu():
    print('OPÇÕES DE MENU ')
    print('1: Adicionar item')
    print('2: Remover item')
    print('3: Ver a lista')
    print('4: Sair')

# Ponto de entrada do programa
if __name__ == "__main__":
    while True:
        menu()  # Exibe o menu
        opcao = input('O que você quer fazer agora? ')

        if opcao == '1':  # Adicionar item
            item = input('Digite o que você quer adicionar: ')
            lista.append(item.upper())  # Adiciona o item e transforma em maiúsculas
            print(f'{item.upper()} ADICIONADO!')

        elif opcao == '2':  # Remover item
            if not lista:  # Verifica se a lista está vazia
                print('A lista tá vazia, não pode remover nada.')
            else:
                item = input('Digite o item que você quer remover: ')
                if item.upper() in lista:
                    lista.remove(item.upper())
                    print(f'{item.upper()} REMOVIDO!')
                else:
                    print(f'{item.upper()} não foi encontrado na lista.')

        elif opcao == '3':  # Ver a lista
            if lista:
                print('Sua lista de compras é essa aqui:')
                for i in lista:
                    print(f' - {i}')
            else:
                print('A lista tá vazia.')

        elif opcao == '4':  # Sair
            print('Saindo...')
            break  # Adiciona um break para sair do loop

        else:  # Opção inválida
            print('Essa opção não é válida, tente de novo.')

