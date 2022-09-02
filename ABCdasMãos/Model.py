import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()
        self.db_connection = self.db_connection.conectar()
        self.con = self.db_connection.cursor() #navegação no banco de dados

    def inserir(self, nome , email, senha):
        try:
            sql = "insert into usuario(codigo, nome, email, senha) values('','{}','{}','{}')".format(nome, email, senha)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linhas afetadas".format(self.con.rowcount)
        except Exception as erro:
            return erro

