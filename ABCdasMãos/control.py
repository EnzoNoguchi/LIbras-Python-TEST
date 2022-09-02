from Model import model

class control:

    def __init__(self):
        self.opcao = -1
        self.modelo = model()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("Escolha uma das opções abaixo: \n"      +
              "0.Sair\n"                               +
              "1.Cadastrar\n"                          +
              "2.Entrar como administrador\n"            +
              "3.Entrar")
        self.setOpcao(int(input()))

    def operacoes(self):

        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("OBRIGADA!")
            elif self.getOpcao() == 1:
                self.cadastrar()


            else:
                print("Opcão escolhida não é valida! Tente novamente!")




    def cadastrar(self):
        print("Informe seu nome: ")
        nome = input()
        print("Informe seu email: ")
        email = input()
        print("Crie um senha: ")
        senha = input()
        print(self.modelo.inserir(nome, email, senha))
