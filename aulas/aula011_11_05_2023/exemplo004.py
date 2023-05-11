"""
Programa para imprimir uma agenda diária, com
horários de 15 em 15 minutos
EXEMPLO -- for dentro de for --- for aninhados! 
0:0
0:15
0:30
0:45
1:0
1:15
1:30
1:45
2:00
...
23:45
"""
for hora in range(24):
    for minuto in range(0, 60, 15):
        print(f"{hora}:{minuto}")