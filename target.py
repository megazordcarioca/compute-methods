from time import sleep


class Methods:

    def main(self):
        print("Dijkstra")
        sleep(2)
        x = self.Dijkstra(self, "A", "G")
        print(x)
        print("Sistema especialista")
        sleep(2)
        x = self.especialista(self)
        print(x)

    def Dijkstra(self, start, end): 
        #Define nós e grafo
        nodes = ("A", "B", "C", "D", "E", "F", "G")
        graph = {
            "A": {
                "B": 9,
                "C": 5,
                "D": 13
            },
            "B": {
                "A": 9,
                "D": 3,
                "E": 10
            },
            "C": {
                "F": 12,
                "A": 5
            },
            "D": {
                "A": 13,
                "B": 3,
                "E": 6,
                "G": 14
            },
            "E": {
                "B": 10,
                "D": 6,
                "G": 7
            },
            "G": {
                "E": 7,
                "F": 10,
                "D": 14
            },
            "F": {
                "C": 12,
                "G": 10
            },
        }
        unvisited = {n: float("inf") for n in nodes}
        unvisited[start] = 0
        visited = {}
        parents = {}
        while unvisited:
            min_vertex = min(unvisited, key=unvisited.get)
            for neighbour, _ in graph.get(min_vertex, {}).items():
                if neighbour in visited:                        #continua a execusão se o vizinho foi visitado
                    continue
                new_distance = unvisited[min_vertex] + graph[min_vertex].get(
                    neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance         #define a nova distancia 
                    parents[neighbour] = min_vertex             #verifica o menor vertice/parente
            visited[min_vertex] = unvisited[min_vertex]         
            unvisited.pop(min_vertex)                           #remove da pilha
            if min_vertex == end:
                break
        return visited

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


x = Methods
x.main(x)
