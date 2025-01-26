# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis sobre ele

texto = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(texto)))
print('Contém só espaços? {}'.format(texto.isspace()))
print('É numérico? {}'. format(texto.isnumeric()))
print('É alfabético? {}'.format(texto.isalpha()))
print('É alfanumérico? {}'.format(texto.isalnum()))
print('Está todo em maiúsculas? {}'.format(texto.isupper()))
print('Está todo em minúsculas? {}'.format(texto.islower()))
print('Está capitalizado? {}'.format(texto.istitle()))
