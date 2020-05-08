import pymysql
from cadastro import Cadastro

def Valida_Usuario():
    
    conexao = pymysql.connect(db='DB_CPU', user='root', passwd='brunico2807')
    cursor = conexao.cursor()
    tentativas=3
    while (tentativas>0):
        login = str(input("Digite o seu login: "))
        senha = str(input("Digite a sua senha: "))
        code = "SELECT SENHA FROM cadastro WHERE LOGIN = '%s'"%(login)
        cursor.execute(code)
        resultado = cursor.fetchone()
        for row in resultado:
            print(row)
            if row != senha:
                tentativas-=1
                print ("Senha incorreta. Você tem mais %i tentativas"%(tentativas))
            else:
                print("Você acertou sua senha")
    conexao.close()
 
