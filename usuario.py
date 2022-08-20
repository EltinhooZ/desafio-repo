class Usuario():
    def __int__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome