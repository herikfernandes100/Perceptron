# Perceptron
# Herik Fernandes e Rafael Gonçalves

MAX_EPOCAS = 1000
TAXA_APRENDIZADO = 0.25


import random
import json
import os

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
    
    def atualizar_pesos(self, erro, entradas):
        x = [-1] + entradas
        for i in range(len(self.pesos)):
            self.pesos[i] += self.taxa_aprendizado * erro * x[i]
    
    def ativacao(self, u):
        if u >= 0:
            return 1
        else:
            return -1
        
    def treinar(self, dados):
        epoca = 0
        historico = []

        while epoca < MAX_EPOCAS:
            erro_total = 0

            for entradas, saida_esperada in dados:
                
                u = self.calcular_u(entradas)
                saida_calculada = self.ativacao(u)

                erro = saida_esperada - saida_calculada
                erro_total += abs(erro)

                self.atualizar_pesos(erro, entradas)

            historico.append(erro_total)
            epoca += 1

            if erro_total == 0:
                break

        return historico, epoca

    def prever(self, entradas):
        u = self.calcular_u(entradas)
        return self.ativacao(u)
    
    def carregar(self, caminho="pesos.json"):
        with open(caminho, 'r') as f:
            self.pesos = json.load(f)

    def salvar_pesos(self):
            # Pasta onde o script está
            pasta = os.path.dirname(os.path.abspath(__file__))

            # Nome base
            nome_base = "pesos"
            extensao = ".json"

            # Primeiro arquivo
            caminho = os.path.join(pasta, nome_base + extensao)

            contador = 1
            # Se existir, criar pesos_1.json, pesos_2.json...
            while os.path.exists(caminho):
                novo_nome = f"{nome_base}_{contador}{extensao}"
                caminho = os.path.join(pasta, novo_nome)
                contador += 1

            # Salva os pesos
            with open(caminho, "w") as f:
                json.dump(self.pesos, f, indent=4)

            print(f"Arquivo salvo em: {caminho}")

    def carregar(self, caminho="pesos.json"):
        with open(caminho, "r") as f:
            self.pesos = json.load(f)
