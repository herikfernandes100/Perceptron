# Perceptron
# Herik Fernandes e Rafael Gonçalves


import random

class Perceptron:

    def __init__(self, taxa_aprendizado):
        self.n = taxa_aprendizado
        # 4 pesos: pesos = [limiar, x1, x2, x3]
        self.w = [random.random() for _ in range(4)] # Inicializa os pesos com valores aleatórios entre 0 e 1


    # Função de soma ponderada de u
    def calcular_u(self, entradas):
        x = [-1] + entradas # Adiciona o termo (limiar) como a primeira entrada

        #u = (Somatorio)wi*xi + (-1)*w0
        soma = 0
        for i in range(len(self.w)):
            soma += self.w[i] * x[i] # Calcula a soma ponderada dos pesos e entradas
        return soma
    
    # Função de ativação
    def ativacao(self, u):
        if u >= 0:
            return 1
        else:
            return 0
        
    # Função de treinamento
    # dados no formato: [([x1, x2, x3], d), ...]
    def treinar(self, dados):
        epoca = 0

        while True:
            erro_total = 0

            for x, d in dados:
                x = [-1] + x # Adiciona o termo que multiplica o limiar como a primeira entrada

                u = self.calcular_u(x) # Calcula a soma ponderada das entradas
                y = self.ativacao(u) # Aplica a função de ativação para obter a saída

                erro = d - y # Calcula o erro entre a saída esperada e a obtida
                erro_total += abs(erro) # Acumula o erro total

                # Atualiza os pesos com base no erro e na taxa de aprendizado
                for i in range(len(self.w)):
                    # wi = wi + n * (d - y) * x[i]
                    self.w[i] += self.n * erro * x[i] # Atualiza cada peso com base no erro e na entrada correspondente

            epoca += 1

            if erro_total == 0: # Se não houver mais erros, o treinamento é concluído
                break