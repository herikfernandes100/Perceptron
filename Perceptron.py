# Perceptron
# Herik Fernandes e Rafael Gonçalves

MAX_EPOCAS = 1000
TAXA_APRENDIZADO = 0.25


import random
import json
import os
import matplotlib.pyplot as plt

class Perceptron:

    def __init__(self):
        self.taxa_aprendizado = TAXA_APRENDIZADO
        self.pesos = [random.uniform(-1, 1) for _ in range(4)]

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

    def plotar_grafico(self, historico, epocas):
        
        plt.figure(figsize=(8,5))
        plt.plot(range(1, epocas+1), historico, marker='o')
        plt.title("Evolução do Erro por Época")
        plt.xlabel("Épocas")
        plt.ylabel("Erro Total")
        plt.grid(True)
        plt.show()

    def prever(self, entradas):
        u = self.calcular_u(entradas)
        return self.ativacao(u)

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

    def carregar_pesos(self, caminho="pesos.json"):
        with open(caminho, "r") as f:
            self.pesos = json.load(f)

    def treinar_completo(self, dados):
        print("Treinando o perceptron...")
        print("\nPesos iniciais:", self.pesos)

        historico, epocas = self.treinar(dados)
        self.salvar_pesos()

        print("\nPesos finais:", self.pesos)
        print("\nHistórico de erro:", historico)
        print("\nTotal de épocas:", epocas)

        return historico, epocas

    def prever_treino(self, dados):
        print("\n=== Testes ===")
        acertos = 0

        for x, esperado in dados:
            previsto = self.prever(x)
            print(f"Entrada: {x} | Esperado: {esperado} | Previsto: {previsto}")

            if previsto == esperado:
                acertos += 1

        print(f"\nAcurácia: {acertos}/{len(dados)} = {acertos/len(dados)*100:.2f}%")

    def prever_completo(self, novos_dados):
        print("\n=== Novos Dados ===")
        for x in novos_dados:
            previsto = self.prever(x)
            print(f"Entrada: {x} | Previsto: {previsto}")