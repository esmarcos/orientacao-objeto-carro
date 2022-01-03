class Carro():

    __capacidade_de_combustivel: int
    __velocidade: int
    __combustivel: int
    __status: bool

    def __init__(self, capacidade):
        self.__capacidade_de_combustivel = capacidade
        self.__velocidade = 0
        self.__combustivel = 0
        self.__status = False

    def aumentar_velocidade(self):
        self.__velocidade += 1
    
        
    def diminuir_velocidade(self):
        self.__velocidade -= 1

    def set_capacidade_de_combustivel(self, capacidade_de_combustivel: int):
        self.__capacidade_de_combustivel = capacidade_de_combustivel

    def get_capacidade_combustivel(self):
        return self.__capacidade_de_combustivel
    
    def set_combustivel(self, combustivel:int):
        self.__combustivel = combustivel
    
    def get_combustivel(self):
        return self.__combustivel
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status:bool):
        self.__status = status
    
    
    def set_velocidade(self, velocidade: int):
        self.__velocidade = velocidade

    def get_velocidade(self):
        return self.__velocidade
    
    def __str__(self):
        carro = "status: " + str(self.__status) + "\ncombustivel: " + str(self.__combustivel)
        carro += "\nvelocidade: " + str(self.get_velocidade())
        return carro
        

