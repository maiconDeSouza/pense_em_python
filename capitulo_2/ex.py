import math
# n =42
# 42 = n erro proposital

x = y = 1
print(x, y)

var_teste_ponto_virgula = 23; #pelo jeito o python aceita tbm ponto e virgula no final da instrução
print(var_teste_ponto_virgula)

# print(xy)
# z = xy não é possivel

print('\n Exercício 2.2')
print(f'\n{1:-^11}')
raio = 5

volume = ((4 / 3)* math.pi) * (raio ** 3)
print(f'{volume:.1f}')

print(f'\n{2:-^11}')

preco_livre = 24.95
desconto = 40 / 100
primeiro_livro = 3
demais_livros = 0.75
compra = 60
total_compra = 0
inteirar = 1

while inteirar <= compra:
    if inteirar == 1:
        total_compra += (preco_livre - (preco_livre * desconto)) + primeiro_livro
    else:
        total_compra += (preco_livre - (preco_livre * desconto)) + demais_livros
    
    inteirar += 1

print(f'Total da compra de livros -> R${total_compra:.2f}')

print(f'\n{3:-^11}')
# sair de casa 6:52
hora_de_saida = 6
minutos_de_saida = 52
minutos_total_de_saida = (hora_de_saida * 60) + 52
segundos_total_de_saida = minutos_total_de_saida * 60

dois_km_minutos = 8
dois_km_segundos = 15
dois_km_total_segundos = ((dois_km_minutos * 60) + dois_km_segundos) * 2

tres_km_minutos = 7
tres_km_segundos = 12
tres_km_total_segundos = ((tres_km_minutos * 60) + tres_km_segundos) * 3

total = segundos_total_de_saida + dois_km_total_segundos + tres_km_total_segundos

horas = total // 3600
minutos = (total % 3600) // 60
segundos = total % 60

print(f'Chehou as {horas}:{minutos}:{segundos}')