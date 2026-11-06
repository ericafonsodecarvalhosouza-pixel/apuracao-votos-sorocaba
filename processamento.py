import pandas as pd

caminho = r"*ADICIONE SEU CAMINHO*"

COLUNA_VOTOS = "QT_VOTOS_NOMINAIS_VALIDOS"
SIGLA_COLUNA_PARTIDO = "SG_PARTIDO"
COLUNA_CARGO = "DS_CARGO"

def dividir_dados():
    leitor = pd.read_csv(
        caminho,
        sep=";",
        encoding="latin1",
        chunksize=3_000
    )
    
    return list(leitor)

def processar_partes(df):
    df[COLUNA_VOTOS] = pd.to_numeric(
        df[COLUNA_VOTOS],
        errors="coerce"
    )
    
    df = df.dropna(subset=[COLUNA_VOTOS])
    
    soma = df[COLUNA_VOTOS].sum()
    quantidade = len(df)
    
    partidos = df.groupby(SIGLA_COLUNA_PARTIDO)[COLUNA_VOTOS].agg(["sum", "count"])
    
    cargos = df.groupby(COLUNA_CARGO)[COLUNA_VOTOS].agg(["sum", "count"])
    
    return soma, quantidade, partidos, cargos

def apuracao(resultados):
    
    soma_total = 0
    quantidade_total = 0
    
    partidos_total = {}
    cargos_total = {}
    
    for soma, quantidade, partidos, cargos in resultados:
        soma_total += soma
        quantidade_total += quantidade
        
        for nome, linha in partidos.iterrows():
            
            if nome not in partidos_total:
                partidos_total[nome] = [0, 0]
                
            partidos_total[nome][0] += linha["sum"]
            partidos_total[nome][1] += linha["count"]
        
        for nome, linha in cargos.iterrows():

            if nome not in cargos_total:
                cargos_total[nome] = [0, 0]

            cargos_total[nome][0] += linha["sum"]
            cargos_total[nome][1] += linha["count"]
    
    media_geral = (
        soma_total / quantidade_total
        if quantidade_total else 0
    )
    
    media_partidos = {
        nome: soma / quantidade
        for nome, (soma, quantidade) in partidos_total.items()
    }
    
    media_cargos = {
        nome: soma / quantidade
        for nome, (soma, quantidade) in cargos_total.items()
    }
    
    partido_melhor_media = max(media_partidos, key=media_partidos.get)
    
    cargo_melhor_media = max(media_cargos, key=media_cargos.get)
    
    return{
        "media_geral": media_geral,
        "partido_maior_media": partido_melhor_media,
        "media_partido_vencedor": media_partidos.get(partido_melhor_media, 0),
        "cargo_maior_media": cargo_melhor_media,
        "media_cargo_vencedor": media_cargos.get(cargo_melhor_media, 0)
    }

def exibir_resultados(titulo, resultado):

    print(f"\n===== {titulo} =====")

    print(f"Média geral: {resultado['media_geral']:.2f}")

    print(f"Partido vencedor: {resultado['partido_maior_media']}")
    print(f"Média: {resultado['media_partido_vencedor']:.2f}")

    print(f"Cargo vencedor: {resultado['cargo_maior_media']}")
    print(f"Média: {resultado['media_cargo_vencedor']:.2f}")        
