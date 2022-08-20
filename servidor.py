from usuario import Usuario



class Servidor():
    def __int__(self):
        self.__usuarios = []
        self.__ttask = 0
        self.__umax = 0
        self.__ativo = False

    def inserir_ttask(self, valor):
        if valor <= 0 or valor > 10:
            print("Valor inválido")
        else:
            self.__ttask = valor

    def inserir_umax(self, valor):
        if valor <= 0 or valor > 10:
            print("Valor inválido")
        else:
            self.__umax = valor

    def inserir_usuario(self, usuario):
        if len(self.__usuarios) > self.__umax:
            return False
        else:
            self.__usuarios.append(usuario)

    def remover_usuario(self, usuario):
        if usuario in self.__usuarios:
            self.__usuarios.remove(usuario)
        else:
            print("Usuario não existe no servidor")



    def desativar_servidor(self):
        if self.__ativo == True:
            self.__ativo = False
            print("Servidor desativado")
        else:
            print("Servidor já está desativado")


    @property
    def usuarios(self):
        return self.__usuarios

    @property
    def ttask(self):
        return self.__ttask

    @property
    def umax(self):
        return self.__umax

    @property
    def ativo(self):
        return self.__ativo


