"""Programa para gerar a tabela de jogos de um campeonato que tem 5 times (times jogam em casa e na casa do adversário)"""

for time1 in ("SPF", "ATL", "VAS", "GRE", "PAR"):
    for time2 in ("SPF", "ATL", "VAS", "GRE", "PAR"):
        if time1 != time2:
            print(f"{time1} X {time2}")