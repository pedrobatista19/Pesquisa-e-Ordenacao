import random


class Util:

    @staticmethod
    def popular_lista_aleatoria(lista, tamanho, minimo, maximo):
        for _ in range(tamanho):
            lista.append(random.randint(minimo, maximo))