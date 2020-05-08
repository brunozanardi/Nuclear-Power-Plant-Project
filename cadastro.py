class Cadastro:
    def __init__(self):
        self.nome= None
        self.login= None
        self.idade= None
        self.email= None
        self.senha= None

    def InserirNome(self):
        if self.nome == None: 
            self.nome =  str(input("Nome completo: "))
        else:
            return 'Nome já preenchido'

    def InserirLogin(self):
        if self.login == None:
            self.login = str(input("Cadastrar Login: "))
        else:
            return 'Login já preenchido'

    def InserirIdade(self):
         if self.idade == None:
            self.idade = int(input("Idade: "))
         else:
            return 'Idade já preenchida'  

    def InserirEmail(self):
        if self.email == None:
            self.email = str(input("Email: "))
        else:
            return 'Email já preenchido'
        
    def InserirSenha(self):
        if self.senha == None:
            self.senha = str(input("Senha a ser cadastrada: "))
        else:
            i = input('Senha já cadastrada, deseja alterá-la? (s/n)')
            if input == 's':
                pass
            else:
                return None
        
    def ConsultarNome(self):
        return self.nome

    def ConsultarLogin(self):
        return self.login

    def ConsultarIdade(self):
        return self.idade

    def ConsultarEmail(self):
        return self.email
    
    def ConsultarSenha(self):
        return self.senha
    
    def ConsultarTudo(self):
        print("Nome cadastrado: {}\nLogin cadastrado: {}\nIdade cadastrada:{}\Email cadastrado: {}".format(self.nome, self.login,self.idade,self.email))
    
