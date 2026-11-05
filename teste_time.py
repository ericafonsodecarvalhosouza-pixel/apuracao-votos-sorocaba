
import time

def medir_tempo(funcao):
    inicio = time.perf_counter()
    resultado = funcao()
    fim = time.perf_counter()
    tempo_total = fim - inicio
    return resultado, tempo_total
    