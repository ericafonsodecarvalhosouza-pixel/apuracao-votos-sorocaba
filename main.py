from processamento import (
    dividir_dados,
    processar_partes,
    apuracao,
    exibir_resultados
)

from multiprocessos import executar_multiprocessing
from multithreading import executar_multithreading
from teste_time import medir_tempo


def executar_sequencial():
    # Essa função executa o processamento de forma sequencial.
    partes = dividir_dados()

    resultados = []

    for parte in partes:
        resultado = processar_partes(parte)
        resultados.append(resultado)

    return apuracao(resultados)

def main():

    #PROCESSAMENTO SEQUENCIAL
    
    resultado_sequencial, tempo_sequencial = medir_tempo(
        executar_sequencial
    )

    # MULTIPROCESSAMENTO
    resultado_processos, tempo_processos = medir_tempo(
        executar_multiprocessing
    )

    # MULTITHREADING
    resultado_threads, tempo_threads = medir_tempo(
        executar_multithreading
    )

    #EXIBIÇÃO DOS RESULTADOS
    #exibir_resultados("PROCESSAMENTO SEQUENCIAL", resultado_sequencial)

    exibir_resultados("MULTIPROCESSAMENTO", resultado_processos)
    exibir_resultados("MULTITHREADING", resultado_threads)


    # EXIBIÇÃO DOS TEMPOS
    print("\n===== TEMPO DE EXECUÇÃO =====")
    print(f"Multiprocessamento: {tempo_processos:.4f} segundos")
    print(f"Multithreading: {tempo_threads:.4f} segundos")
    
    if tempo_processos < tempo_threads:
        print("Melhor desempenho: MULTIPROCESSING")
    elif tempo_threads < tempo_processos:
        print("Melhor desempenho: MULTITHREADING")
    else:
        print("As duas abordagens tiveram o mesmo tempo.")


if __name__ == "__main__":
    main()