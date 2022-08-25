# main para tentar uma nova lógica
with open('input.txt', 'r') as arquivo_input:
    input = [int(item) for item in arquivo_input.readlines()]

tick = 0
ttask = 0
umax = 0
listaServidores = []
controle = True

if input[0] <= 0 or input[0] > 10:
    print("Não foi")
else:
    ttask = input[0]

if input[1] <= 0 or input[1] > 10:
    print("Não foi")
else:
    umax = input[1]

c = 0

while controle:
    c += 1
    if not len(listaServidores):

        if input[tick + 2] < umax:
            listaServidores.insert(tick, 1)

        elif listaServidores[tick] > 0:
            user = listaServidores[tick]
            listaServidores.insert(tick, user + 1)

        else:
            listaServidores.insert(tick, 1)
        tick += 1

    elif c == 10:
        controle = False
    print(listaServidores)
