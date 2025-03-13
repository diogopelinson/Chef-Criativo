print("""

░█████╗░██╗░░██╗███████╗███████╗  ░█████╗░██████╗░██╗░█████╗░████████╗██╗██╗░░░██╗░█████╗░
██╔══██╗██║░░██║██╔════╝██╔════╝  ██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██║██║░░░██║██╔══██╗
██║░░╚═╝███████║█████╗░░█████╗░░  ██║░░╚═╝██████╔╝██║███████║░░░██║░░░██║╚██╗░██╔╝██║░░██║
██║░░██╗██╔══██║██╔══╝░░██╔══╝░░  ██║░░██╗██╔══██╗██║██╔══██║░░░██║░░░██║░╚████╔╝░██║░░██║
╚█████╔╝██║░░██║███████╗██║░░░░░  ╚█████╔╝██║░░██║██║██║░░██║░░░██║░░░██║░░╚██╔╝░░╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░  ░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░░╚════╝░"
""")

print('1. Cadastrar restaurante')
print('2. Listagem restaurante')
print('3. Ativar restaurante') # Não aparece no app direto
print('4. Sair\n')


opcao_escolhida = int(input('Escolha uma opção: '))
# opcao_escolhida = int(opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar restaurantes')
    # Todo cod de cadastro do restaurante
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    print('Encerrando o programa')
    


