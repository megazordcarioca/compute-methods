def especialista(self):
        print(
        "Ola, iremos verificar os sintomas para saber se eh supeito de covid ou nao:"
        )
        print("Deseja iniciar o questionario? [s/n]")
        valor = input()
        if (valor == 's'):
            vetor = self.perguntas(self)
            if (vetor == None):
                print("Sem suspeita de covid-19;")
                return
            resultado = self.calculaSuspeito(self,vetor)
            if (resultado < 2):
                print("Sem suspeita de covid-19;")
                return
            else:
                print("Paciente com suspeita de covid-19.")
                return

        else:
            print("Obrigado por utilizar o software")
            return


def perguntas(self):
    soma = 0
    print("Apresenta um ou mais desses casos? [s/n]")
    print("Tosse; OU")
    print("Dor de garganta; OU")
    print("Coriza (nariz escorrendo);")
    simNao = input()
    if (simNao == 's'):
        soma = soma + 1
        vetor = [1]
    elif (simNao == 'n'):
        print("Nao se classifica como suspeito para covid-19.")
        return
    else:
        print("Resposta incorreta.")
        self.perguntas()

    print("Resposta computada.")
    print(
        "Responda se apresenta esses sintomas em conjunto com os anteriores.")
    print("Dificuldade respiratoria? [s/n]")
    if (input() == 's'):
        soma = soma + 1
        vetor.append(1)
    else:
        return
    return vetor


def calculaSuspeito(self,vetor):
    matriz = [
            [0, 0], 
            [1, 0], 
            [1, 1], 
            [0, 1]]
    i = 0
    while i < 2:
        if ((matriz[i][0] == vetor[0]) and (matriz[i][1] == vetor[1])):
            soma = matriz[i][0] + matriz[i][1]
        i = i + 1
    return soma