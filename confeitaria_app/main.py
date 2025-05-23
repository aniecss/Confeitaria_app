

def main():
    while True:
        print('\n==== CONFEITARIA RIO ====')
        print('-' * 30)
        print('\n==== MENU PRINCIPAL ====')
        print('''
              1. Login
              2. Cadastrar Usuário
              3. Cadastrar Loja
              4. Fazer Pedido
              5. Sair''') 
        
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            return 'Fazer login'
        elif opcao == 2:
            return 'Cadastrar usuario'
        elif opcao == 3:
            return 'Cadastrar loja'
        elif opcao == 4:
            return 'Fazer pedido'
        elif opcao == 5:
            print('Volte sempre')
            break
        else:
            print('Opção invalida, tente novamente')

            
if __name__ == "__main__":
    main()