"""
Programa para imprimir uma agenda diária, com
horários de 15 em 15 minutos
EXEMPLO -- for dentro de for --- for aninhados! 
00:00
00:15
00:30
00:45
1:00
1:15
1:30
1:45
2:00
...
23:45
"""
for hora in range(24):
    if hora == 0:
            hora = "00"
    for minuto in range(0, 60, 15):
        if minuto == 0:
            minuto = "00"
        print(f"{hora}:{minuto}")