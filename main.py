from cadastro import Cad
def cad():
    name = input('Digite seu nome \n')
    age = int(input('Digite a sua idade \n'))
    cadastro = Cad(name,age)
    print('--------------------------------------------------')
    cadastro.display()
    cadastro.verificacao()
cad()

