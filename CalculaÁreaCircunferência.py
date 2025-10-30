'''ENUNCIADO: Calcular a área de uma circunferência, sendo
informado o valor do raio.
DICAS - Fórmula da Área da circunferência: Pi * R2 (ao quadrado)
AUTORA: Sâmara Tinoco
DATA: 23/10/2025
FONTE: ER_Prg13Pag50.py
'''
print("\nInicio!")
# importação das bibliotecas
from math import pi
# lendo e convertendo para o tipo de dado "FLOAT"
vlrRaio = float(input("\nDigite informando o raio da área: "))
print(type(vlrRaio))
vlrArea = pi * vlrRaio ** 2
print(f"A área calculada é = {vlrArea: .2f}.") # f = função de formatação de string.

print("\nFim!")
