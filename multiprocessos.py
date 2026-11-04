from processamento import processar_partes, apuracao, dividir_dados
from multiprocessing import Pool, cpu_count

numero_processos = cpu_count()


def executar_processos(partes):
    
    with Pool(processes=min(numero_processos, len(partes))) as pool:
        
        resultados = pool.map(processar_partes, partes)
    
    return apuracao(resultados)
