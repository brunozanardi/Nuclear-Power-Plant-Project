import pymysql
from cadastro import Cadastro

def Novo_Cadastro():
    conexao = pymysql.connect(db='DB_CPU', user='root', passwd='brunico2807') 
    cursor = conexao.cursor()
    
    print("CADASTRO DE NOVO USUÁRIO")
    cadastro = Cadastro()

    cadastro.InserirNome()
    nome = cadastro.ConsultarNome()
    #print("O nome colocado foi: {}".format(nome))

    cadastro.InserirLogin()
    login = cadastro.ConsultarLogin()
    #print("O login colocado foi: {}".format(login))

    cadastro.InserirIdade()
    idade = cadastro.ConsultarIdade()
    #print("A idade colocada foi: {}".format(idade))

    cadastro.InserirEmail()
    email = cadastro.ConsultarEmail()
    #print("O email colocado foi: {}".format(email))

    cadastro.InserirSenha()
    senha = cadastro.ConsultarSenha()
    
    code = "INSERT INTO cadastro (NOME, LOGIN, SENHA, EMAIL, IDADE) VALUES (%s,%s,%s,%s,%s)"
    val = [nome,login,senha,email,idade] 
    cursor.execute(code,val)
    conexao.commit()
    conexao.close()

