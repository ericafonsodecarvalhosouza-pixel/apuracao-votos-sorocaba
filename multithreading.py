
import threading

import threading

from processamento import (
    dividir_dados,
    processar_partes,
    apuracao
)


def executar_thread(df, resultados, indice):
    # Essa função executa o processamento de uma parte dentro de uma thread.
    resultados[indice] = processar_partes(df)


def executar_multithreading():
    # Essa função cria e executa as threads.
    partes = dividir_dados()

    resultados = [None] * len(partes)

    threads = []

    for indice, parte in enumerate(partes):
        thread = threading.Thread(
            target=executar_thread,
            args=(parte, resultados, indice)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    resultado_final = apuracao(resultados)

    return resultado_final
