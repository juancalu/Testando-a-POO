class Cad:
    def __init__(self, nome , idade):
      self.nome = nome
      self.idade = idade
    def display(self):
        print(self.nome)
        print(self.idade)
    def verificacao(self):
        if self.idade <18:
            print('Menor de idade')
        else:
            print('Maior de idade')
