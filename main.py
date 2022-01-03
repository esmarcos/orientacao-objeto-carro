from carro_service import Carro_service
from carro import Carro

if __name__ == "__main__":
    
    carro = Carro(10)
    carro_service = Carro_service()
    carro_service.abastecer(carro, 10)
    carro_service.ligar(carro)
    print(carro)
    print("----------------")
    carro_service.acelerar(carro)
    carro_service.acelerar(carro)
    carro_service.acelerar(carro)
    carro_service.acelerar(carro)
    print(carro)
    print("----------------") 
    carro_service.freiar(carro)
    print(carro)
    print("----------------")
    carro_service.parar(carro)
    print(carro)
    print("---------------")
    carro_service.marcha_re(carro)
    carro_service.marcha_re(carro)
    carro_service.marcha_re(carro)
    print(carro)