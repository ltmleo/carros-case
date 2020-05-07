import re
class Carros:
    def __init__(self, cor, placa, ano, modelo):
        self.cor = cor.lower().strip()
        self.placa = placa.lower().strip()
        self.ano = int(ano)
        self.modelo = modelo.lower().strip()
        if not self._valida():
            raise ValueError("valores inválidos") 

    def _valida(self):
        if re.search(r"[a-z]{3}[-][0-9]{4}", self.placa):
            return True
        else:
            return False
        
#test = Carros("branco", "ggf2600", 1997, "hb20")



        