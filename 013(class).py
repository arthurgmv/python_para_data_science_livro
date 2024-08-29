class Pessoa:
#construtor
   def __init__(self, Nome, Idade):
       self.Nome = Nome
       self.Idade = Idade

   def Boas_vindas(self):
       print("Olá, seja bem-vindo! ", self.Nome)

   def Recusado(self):
       print("Seu acesso foi negado.")
#função
   def Maior_de_idade(self):
        if self.Idade >= 18:
            print("Usuário é maior de idade")
            self.Boas_vindas()
        else:
            print("Usurário é menor de idade")
            self.Recusado()

João = Pessoa("João", 20)
João.Maior_de_idade()
print(" ")
Pedro = Pessoa("Pedro", 5)
Pedro.Maior_de_idade()
