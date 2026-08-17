from view.view import OrdenacaoView
from controller.controller import OrdenacaoController

TAMANHO = 100000
MINIMO = 1000
MAXIMO = 20000


def main():
    view = OrdenacaoView()
    controller = OrdenacaoController()

    view.limpar_tela()

    lista = controller.gerar_lista_teste(TAMANHO, MINIMO, MAXIMO)

    resultados = controller.executar_todos(lista)

    for resultado in resultados:
        view.exibir_resultado(resultado)

    view.exibir_comparativo(resultados)


if __name__ == "__main__":
    main()