# 🧠 Perceptron em Python

Implementação de um **Perceptron** (modelo básico de rede neural) desenvolvido em **Python**, com foco em aprendizado supervisionado, ajuste de pesos e visualização da evolução do erro.

Projeto desenvolvido por **Hérik Fernandes** e **Rafael Gonçalves**.

---

## 🚀 Funcionalidades

* 🧠 Implementação do algoritmo Perceptron
* ⚖️ Atualização de pesos com regra de aprendizado
* 🔁 Treinamento por épocas
* 📉 Registro do erro ao longo do treinamento
* 📊 Plotagem do gráfico de erro
* 💾 Salvamento automático dos pesos em `.json`
* 📂 Carregamento de pesos salvos
* 🔍 Previsão de novos dados
* 📈 Cálculo de acurácia

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 📊 Matplotlib
* 📁 JSON
* 🎲 Random

---

## 📂 Estrutura do Projeto

* `Perceptron` → Classe principal do modelo
* `pesos` → Lista de pesos do modelo
* `treinar()` → Método de treinamento
* `prever()` → Método de previsão
* `plotar_grafico()` → Visualização do erro
* `salvar_pesos()` → Persistência dos pesos
* `carregar_pesos()` → Leitura dos pesos salvos

---

## 🧠 Como funciona o Perceptron

O modelo:

1. Recebe entradas
2. Calcula a soma ponderada (u)
3. Aplica função de ativação:

* Se `u >= 0` → saída = 1
* Se `u < 0` → saída = -1

4. Ajusta os pesos com base no erro:

```text
peso = peso + taxa_aprendizado * erro * entrada
```

---

## ▶️ Como executar

1. Instale as dependências:

```bash id="x1d9pw"
pip install matplotlib
```

2. Execute seu script Python normalmente:

```bash id="9m1y9o"
python main.py
```

---

## 📊 Exemplo de uso

```python id="0v1g52"
dados = [
    ([0, 0, 0], -1),
    ([0, 1, 0], -1),
    ([1, 0, 1], 1),
    ([1, 1, 1], 1)
]

p = Perceptron()
historico, epocas = p.treinar_completo(dados)
p.plotar_grafico(historico, epocas)
p.prever_treino(dados)
```

---

## 📈 Saídas do sistema

* 📉 Gráfico mostrando evolução do erro por época
* 📄 Arquivo `.json` com pesos salvos automaticamente
* 🧪 Testes com acurácia do modelo
* 🔍 Previsões para novos dados

---

## 💡 Conceitos aplicados

* Inteligência Artificial
* Machine Learning básico
* Aprendizado supervisionado
* Função de ativação
* Ajuste de pesos (regra delta)
* Visualização de dados

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para:

* Entender o funcionamento de redes neurais básicas
* Implementar um modelo de classificação do zero
* Praticar Python aplicado à IA

---

## 📌 Melhorias futuras

* Suporte a múltiplas camadas (MLP)
* Interface gráfica
* Dataset real para treinamento
* Normalização de dados
* Exportação de gráficos

---

## 👨‍💻 Autores

* [Hérik Fernandes](https://github.com/herikfernandes100)
* Rafael Gonçalves

---

⭐ Se curtiu o projeto, deixa uma estrela!
