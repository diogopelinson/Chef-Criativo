import os

restaurantes = [{'Nome':'Divino', 'Categoria':'Brasileira', 'Ativo':False}, 
                {'Nome':'Planet Pizzas', 'Categoria':'Italiana','Ativo': True},
                {'Nome':'Mak Burger', 'Categoria':'Hamburgueria', 'Ativo':False}]

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
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
     os.system('cls')
     print(texto)
     print()


# Opção 1 - Cadasto
def cadastrar_novo_restaurante():
   exibir_subtitulo('Cadastro de novos restaurantes')
   nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
   categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
   dados_do_restaurante = {'Nome': nome_do_restaurante, 'Categoria': categoria, 'Ativo':False}
   restaurantes.append(dados_do_restaurante)
   print(f'O resaurante {nome_do_restaurante} foi cadastrado com êxito!')
   voltar_ao_menu_principal()


# Opção 2 - Lista
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    # Para cada restaurante na lista [restaurantes]: nome
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = restaurante["Ativo"]
        print(f'- {nome_restaurante} | {categoria} | {ativo}')
    voltar_ao_menu_principal()






def escolher_opção():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)


        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
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
    


