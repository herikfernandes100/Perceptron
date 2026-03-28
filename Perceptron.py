# Perceptron
# Herik Fernandes e Rafael Gonçalves

MAX_EPOCAS = 1000
TAXA_APRENDIZADO = 0.25


import random
import json

class Perceptron:

    def __init__(self):
        self.taxa_aprendizado = TAXA_APRENDIZADO
        self.pesos = [random.random() for _ in range(4)]

    def calcular_u(self, entradas):
        x = [-1] + entradas
        soma = 0
        for i in range(len(self.pesos)):
            soma += self.pesos[i] * x[i]
        return soma
    
    def ativacao(self, u):
        if u >= 0:
            return 1
        else:
            return 0
        
    def treinar(self, dados, ):
        epoca = 0

        while epoca < MAX_EPOCAS:
            erro_total = 0

            for x, saida_esperada in dados:

                u = self.calcular_u(x)
                saida_calculada = self.ativacao(u)

                erro = saida_esperada - saida_calculada
                erro_total += abs(erro)

                # Atualiza os pesos com base no erro e na taxa de aprendizado
                for i in range(len(self.pesos)):
                    # Wi = Wi + n * (Dk - Yk) * X[i]
                    self.pesos[i] += self.taxa_aprendizado * erro * x[i] # Atualiza cada peso com base no erro e na entrada correspondente

            epoca += 1

            if erro_total == 0:
                break

    def prever(self, entradas):
        u = self.calcular_u(entradas)
        return self.ativacao(u)
    
    def salvar(self, caminho = "pesos.json"):
        with open(caminho, 'w') as f:
            json.dump(self.pesos, f)

    def carregar(self, caminho = "pesos.json"):
        with open(caminho, 'r') as f:
            self.pesos = json.load(f)
