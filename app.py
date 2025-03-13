import os
'''Biblioteca para importar a o.systems('cls) dentro das funcoes, para limpar o terminal '''

restaurantes = [{'Nome': 'Divino', 'Categoria': 'Brasileira', 'Ativo': False},
                {'Nome': 'Planet Pizzas', 'Categoria': 'Italiana', 'Ativo': True},
                {'Nome': 'Mak Burger', 'Categoria': 'Hamburgueria', 'Ativo': False}]


def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""

░█████╗░██╗░░██╗███████╗███████╗  ░█████╗░██████╗░██╗░█████╗░████████╗██╗██╗░░░██╗░█████╗░
██╔══██╗██║░░██║██╔════╝██╔════╝  ██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██║██║░░░██║██╔══██╗
██║░░╚═╝███████║█████╗░░█████╗░░  ██║░░╚═╝██████╔╝██║███████║░░░██║░░░██║╚██╗░██╔╝██║░░██║
██║░░██╗██╔══██║██╔══╝░░██╔══╝░░  ██║░░██╗██╔══██╗██║██╔══██║░░░██║░░░██║░╚████╔╝░██║░░██║
╚█████╔╝██║░░██║███████╗██║░░░░░  ╚█████╔╝██║░░██║██║██║░░██║░░░██║░░░██║░░╚██╔╝░░╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░  ░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░╚════╝░"
""")


def exibir_opções():
    '''Exibe as opcoes disponiveis no app'''
    print('1. Cadastrar restaurante')
    print('2. Listagem restaurante')
    print('3. Alternar estado do restaurante') 
    print('4. Sair\n') 

# Bloco de codigo para finalizar o App


def Finalizar_app():
    ''' Funcao definida para exibir mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizar app')


def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
''' Exibe mensagem de opção inválida e retorna ao menu principal !
    
    Outputs:
    - Retorna ao menu principal
    '''
    


def exibir_subtitulo(texto):
    '''Exibe um subtitulo especial na tela
    
    Inputs:
    -texto: str - o texto especial
    '''
    os.system('cls')
    linha ='*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


# Opção 1 - Cadasto
def cadastrar_novo_restaurante():
    ''' Essa funcao e responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Output:
    -Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(
        f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'Nome': nome_do_restaurante,
                            'Categoria': categoria, 'Ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O resaurante {nome_do_restaurante} foi cadastrado com êxito!')
    voltar_ao_menu_principal()


# Opção 2 - Lista
def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando restaurantes')
    # Para cada restaurante na lista [restaurantes]: nome
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativado' if restaurante["Ativo"] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado dos restaurantes cadastrados
    
    Outputs:
    - Exibe mensagem indicando o sucesso da alteracao
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante[
                'Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


# Opção 3 - Ativar


def escolher_opção():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            Finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# Ordem de Saida


def main():
    '''Funcao princiapl que inicaliza o prrograma e define a logica do mesmo'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opção()


if __name__ == '__main__':
    main()
