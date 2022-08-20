from servidor import Servidor
from usuario import Usuario

ListaServidores = []

servidor1 = Servidor()

arquivo_input = open('input.txt', 'w+')
ttask = input("Digite a quantidade de ticks da tarefa: ")

servidor1.inserir_ttask(int(ttask))

umax = input('Digite a quantidade de usuários: ')

servidor1.inserir_umax(int(umax))


print(servidor1.ttask, servidor1.umax)

arquivo_input.seek(0,0)
print(arquivo_input.read())







