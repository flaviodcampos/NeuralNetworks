import random

entrys = [[0,0],[0,1],[1,0],[1,1]]

intended = [0,1,1,1] #A saída desejada é que define o tipo de porta que o algoritmo procura

alpha = 0.7 #Taxa de aprendizado
w = [] #Vetor de pesos

for x in range(3):
    w.append(random.uniform(0,1))

epocaMax = 10

for epoca in range(epocaMax):
    results = [0, 0, 0, 0]
    erroEpoca = 0

    for i in range(4):
        neuron = w[0] + entrys[i][0] * w[1] + entrys[i][1] * w[2]

        if (neuron < 0):
            results[i] = 0
        else:
            results[i] = 1

        delta = intended[i] - results[i]
        w[0] = w[0] + alpha * delta
        w[1] = w[1] + alpha * entrys[i][0] * delta
        w[2] = w[2] + alpha * entrys[i][1] * delta

        erroEpoca = erroEpoca + abs(delta)

    if (erroEpoca == 0):
        break

if (erroEpoca == 0):
    print("A rede convergiu")
else:
    print("A rede não convergiu")

print("Bias: ", w[0])
print("Pesos: ",w[1],', ',w[2])
print("Valores encontrados: ",results)