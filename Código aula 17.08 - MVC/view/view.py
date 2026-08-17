import os


class OrdenacaoView:

    def limpar_tela(self):
        os.system('cls')

    def exibir_titulo(self, texto):
        print(f"\n===== {texto} =====")

    def exibir_resultado(self, resultado):
        comp = resultado["comparacoes"] if resultado["comparacoes"] is not None else "N/A"
        troc = resultado["trocas"] if resultado["trocas"] is not None else "N/A"
        print(f"\nTempo da rotina ordenar por {resultado['nome_algoritmo']}: {resultado['tempo']} s")
        print(f"Comparacoes: {comp}")
        print(f"Trocas: {troc}")

    def exibir_comparativo(self, resultados):
        self.exibir_titulo("COMPARATIVO")
        print(f"{'Algoritmo':<15}{'Comparações':<15}{'Trocas':<12}{'Tempo (s)':<15}")
        for r in resultados:
            comp = r["comparacoes"] if r["comparacoes"] is not None else "N/A"
            troc = r["trocas"] if r["trocas"] is not None else "N/A"
            print(f"{r['nome_algoritmo']:<15}{str(comp):<15}{str(troc):<12}{r['tempo']:<15.8f}")