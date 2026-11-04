from processamento import dividir_dados, exibir_resultados
from multiprocessos import executar_processos
from time import perf_counter



def main():
    partes = dividir_dados()

    if not partes:
        print("Arquivo vazio.")
        return

    inicio = perf_counter()
    resultado_processos = executar_processos(partes)
    tempo_processos = perf_counter() - inicio
    
    exibir_resultados("PROCESSO", resultado_processos)
    print(f"Tempo de processamento {tempo_processos:.2f}")
    
    
    
    ''''
    print("\n===== COMPARAÇÃO DE DESEMPENHO =====")

        print(f"Tempo com processos: {tempo_processos:.4f} segundos")
        print(f"Tempo com threads: {tempo_threads:.4f} segundos")

        if tempo_processos < tempo_threads:
            print("Melhor desempenho: MULTIPROCESSING")
        elif tempo_threads < tempo_processos:
            print("Melhor desempenho: MULTITHREADING")
        else:
            print("As duas abordagens tiveram o mesmo tempo.")
'''
    

if __name__ == "__main__":
    main()
    