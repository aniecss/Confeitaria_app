class Controle:
    confetarias = []
    conta_login = []

    def __init__(self, proprietario, loja, cnpj, endereco, status):
        self._proprietario = proprietario
        self._loja = loja
        self._cnpj = cnpj
        self_endereco= endereco
        self._status = False
        Controle.confetarias.append(self)

    def __str__(self):
        return f'Nome da Loja{self._loja} | Edenreço: {self._endereco} {"Ativo" if self._status else "Inativo"}'
    
    @classmethod
    def login(cls):
        tentativas = 3
        for c in range(tentativas):
            login = input('Login: ')
            try:
                senha = int(input('Senha: '))
            except ValueError:
                continue

            for usuario in cls.conta_login:
                if usuario._login == login and usuario._senha == senha:
                    usuario._status = True
                    print(f'\nBem-vindo, {usuario._nome}!')
                    return usuario
                
            print('Login ou senha incorretas. Tente novamente')
        print('Usuario bloqueado')
    
    @classmethod
    def cadastrar_usuario(cls):
        nome = input('Digite seu nome: ')
        login = input('Digite o seu login: ')
        senha = int(input('Digite a senha: '))
        cls(nome, login, senha)
        print(f'Login {login} cadastrado com sucesso')

        
