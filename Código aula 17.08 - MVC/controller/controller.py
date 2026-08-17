import time
from model.ordenacao import Ordenacao
from model.resultado import criar_resultado
from controller.util import Util


class OrdenacaoController:

    ALGORITMOS = {
        "1": ("Quick", Ordenacao.quicksort_completo),
        "2": ("Pente", Ordenacao.pente),
        "3": ("Bolha", Ordenacao.bolha),
        "4": ("Seleção", Ordenacao.selecao),
        "5": ("Inserção", Ordenacao.insercao),
        "6": ("Agitação", Ordenacao.agitacao),
    }

    def gerar_lista_teste(self, tamanho, minimo, maximo):
        lista = []
        Util.popular_lista_aleatoria(lista, tamanho, minimo, maximo)
        return lista

    def executar_algoritmo(self, opcao, lista_original):
        nome, funcao = self.ALGORITMOS[opcao]
        vetor = lista_original.copy()

        inicio = time.perf_counter()
        comparacoes, trocas = funcao(vetor)
        tempo = time.perf_counter() - inicio

        return criar_resultado(nome, vetor, comparacoes, trocas, tempo)

    def executar_todos(self, lista_original):
        resultados = []
        for opcao in self.ALGORITMOS:
            resultados.append(self.executar_algoritmo(opcao, lista_original))
        return resultados