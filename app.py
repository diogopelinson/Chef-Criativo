import os

def exibir_nome_do_programa():
    print("""

░█████╗░██╗░░██╗███████╗███████╗  ░█████╗░██████╗░██╗░█████╗░████████╗██╗██╗░░░██╗░█████╗░
██╔══██╗██║░░██║██╔════╝██╔════╝  ██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██║██║░░░██║██╔══██╗
██║░░╚═╝███████║█████╗░░█████╗░░  ██║░░╚═╝██████╔╝██║███████║░░░██║░░░██║╚██╗░██╔╝██║░░██║
██║░░██╗██╔══██║██╔══╝░░██╔══╝░░  ██║░░██╗██╔══██╗██║██╔══██║░░░██║░░░██║░╚████╔╝░██║░░██║
╚█████╔╝██║░░██║███████╗██║░░░░░  ╚█████╔╝██║░░██║██║██║░░██║░░░██║░░░██║░░╚██╔╝░░╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░  ░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░╚════╝░"
""")

def exibir_opções():
    print('1. Cadastrar restaurante')
    print('2. Listagem restaurante')
    print('3. Ativar restaurante') # Não aparece no app direto
    print('4. Sair\n')

# Bloco de codigo para finalizar o App
def Finalizar_app(): 
    os.system('cls')
    print('Finalizando o app\n')
    print()

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()


# Opção 1
def cadastrar_novo_restaurante():
    pass




def escolher_opção():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)


        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            Finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# Ordem de Saida
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opção()

if __name__ == '__main__':
    main()
    


