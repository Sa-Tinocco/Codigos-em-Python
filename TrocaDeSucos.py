'''ENUNCIADO: Efetue a troca completa, dos sucos,
sem misturar ou perder
AUTORA: Sâmara Tinoco
DATA: 23/10/2025
FONTE: EP_Exer10Pag53.py
'''
print("\nInicio!")
txtCopo1 = "suco de laranja"
txtCopo2 = "suco de acerola"
print("\nAntes da troca, Copo1 = ", txtCopo1)
print("\nAntes da troca, Copo2 = ", txtCopo2)
print("\nFazendo as trocas!")

##colocando Acerola no Copo1
##txtCopo1 = "suco de acerola"
##txtCopo1 = txtCopo2

txtCopoAuxiliar3 = txtCopo2 #-->Salvei o suco de acerola no copo 3

##Copo2 está SECO.
##então posso colocar o conteúdo do copó1

txtCopo2 = txtCopo1
##Copo1 está SECO.
##então posso colocar o conteúdo do Copo3.

txtCopo1 = txtCopoAuxiliar3
print("\nApós as trocas, Copo1 = ", txtCopo1)
print("\nApós as trocas, Copo2 = ", txtCopo2)
print("\nFim!")
