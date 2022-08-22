from servidor import Servidor
import numpy as np

ticks = 0
servidor = Servidor()
listaServidores = []

# Forma 1 como havia tinha pensado, porém decidi realizar a leitura do arquivo input.txt
# A ideia era que ficasse dinamica a solicitação dos dados.


while True:
    time_task = input("Digite a quantidade de ticks da tarefa: ")

    user_max = input("Digite a quantidade de usuários maximos no servidor: ")

    opcao = int(input('1. Alocar usuarios\n2. Encerrar\n--> '))

    if opcao == 1:
        qtdUsuarios = int(input("Quantos usuarios deseja adicionar no servidor?"))


        servidor.inserir_umax(int(user_max))
        servidor.inserir_ttask(int(time_task))

        for i in range(qtdUsuarios):
        servidor.inserir_usuario(qtdUsuarios)


        listaServidores.append(servidor)
        print(servidor.umax)

        print(qtdUsuarios)
        if qtdUsuarios > servidor.umax:
            print("Não é possivel adicionar mais usuários nesse servidor")
            listaServidores.append(servidor)
        else:
            for i in range(qtdUsuarios):
                nome = str(input("Digite o nome do novo usuário: "))
                usuario = Usuario()
                usuario.inserirNome(nome)
                servidor.inserir_usuario(usuario)

                if servidor.inserir_usuario(usuario):
                    print("criar um novo servidor")
                    servidor = Servidor()
                    servidor.inserir_umax(user_max)
                    servidor.inserir_ttask(time_task)

    else:
        break  # sai do loop
    print('\n')







