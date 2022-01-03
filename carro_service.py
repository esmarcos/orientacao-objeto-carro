from carro import Carro


class Carro_service() :
    
    
    
    def ligar(self, carro:Carro):
        if not carro.get_status() :
            carro.set_status(True)
    
    def desligar(self, carro:Carro):
        if carro.get_status():
            carro.set_status(False)
    
    def acelerar(self, carro:Carro):
        combustivel = carro.get_combustivel()
        if carro.get_status():
            if combustivel > 0:
                combustivel -= 1
                carro.set_combustivel(combustivel)
                carro.aumentar_velocidade()
            else:
                self.parar(carro)
                self.desligar(carro)
                
    def freiar(self, carro:Carro):
        if carro.get_status() and carro.get_velocidade() > 0 :
            carro.diminuir_velocidade()
        else:
            self.parar(carro)
    
    def marcha_re(self, carro:Carro):
        combustivel = carro.get_combustivel()
        if carro.get_status() and carro.get_velocidade() <= 0:
            if combustivel > 0 :
                combustivel -= 1
                carro.set_combustivel(combustivel)
                carro.diminuir_velocidade()
            else:
                self.desligar(carro)
            
        
            
            
    def parar(self, carro:Carro):
        if carro.get_status() and carro.get_velocidade() != 0:
            carro.set_velocidade(0)
    
    def abastecer(self, carro:Carro, combustivel):
        if not carro.get_status() and carro.get_velocidade() == 0:
            combustivel_novo = carro.get_combustivel() + combustivel
            if combustivel_novo < carro.get_capacidade_combustivel():
                carro.set_combustivel(combustivel_novo)
            else:
                carro.set_combustivel(carro.get_capacidade_combustivel())
    
           
                
            
            
            
        

    

    
        


