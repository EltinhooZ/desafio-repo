
# class Servidor():
#     def __int__(self):
#         self.__usuarios = []
#         self.__ttask = 0
#         self.__umax = 0
#
#     def inserir_ttask(self, valor):
#         if valor <= 0 or valor > 10:
#             print("Valor inválido")
#         else:
#             self.__ttask = valor
#
#     def inserir_umax(self, valor):
#         if valor <= 0 or valor > 10:
#             print("Valor inválido")
#         else:
#             self.__umax = valor
#
#     def inserir_usuario(self, usuario):
#         if len(self.__usuarios) >= self.__umax:
#             return False
#         else:
#             self.__usuarios.append(usuario)
#
#     def remover_usuario(self, usuario):
#         if usuario in self.__usuarios:
#             self.__usuarios.remove(usuario)
#         else:
#             print("Usuario não existe no servidor")
#
#     def encerrarServidor(self):
#         if self.__ativo == True:
#             if len(self.__usuarios) == 0:
#                 self.__ativo = False
#                 print("Servidor desligado")
#         else:
#             print("Servidor já está desligado")
#
#
#     @property
#     def nome_servidor(self):
#         return self.__nome_servidor
#
#     @property
#     def usuarios(self):
#         return len(self.__usuarios)
#
#     @property
#     def ttask(self):
#         return self.__ttask
#
#     @property
#     def umax(self):
#         return self.__umax
#
#     @property
#     def ativo(self):
#         return self.__ativo
#

