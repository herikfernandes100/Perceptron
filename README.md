# 🧠 Perceptron - Implementação do Zero

Este projeto consiste na implementação de um Perceptron, um dos algoritmos mais fundamentais de Machine Learning, desenvolvido do zero em Python com o objetivo de compreender profundamente seu funcionamento interno.

O Perceptron é um algoritmo de aprendizado supervisionado utilizado para classificação binária. Neste projeto, toda a lógica foi implementada manualmente, sem uso de bibliotecas de Machine Learning como scikit-learn, permitindo um entendimento completo de cada etapa do processo de aprendizado.

Entre as principais funcionalidades implementadas estão a inicialização dos pesos (incluindo o bias), o cálculo da saída por meio de uma função de ativação do tipo degrau, o ajuste dos pesos com base no erro, além do treinamento iterativo utilizando conjuntos de dados personalizados.

O funcionamento do modelo segue uma sequência simples e eficiente: as entradas são multiplicadas pelos seus respectivos pesos, somadas ao bias, e o resultado passa por uma função de ativação, onde a saída é definida como 1 caso o valor seja maior ou igual a zero, e 0 caso contrário. Em seguida, é calculado o erro com base no valor esperado, e os pesos são ajustados utilizando a taxa de aprendizado.

A estrutura do projeto é organizada de forma simples, contendo um arquivo principal responsável pela execução (Main.py), a implementação do algoritmo (Perceptron.py) e um arquivo de dados para treinamento (dados.txt).

Para executar o projeto, basta clonar o repositório, acessar a pasta e rodar o arquivo principal utilizando Python:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd Perceptron
python Main.py
