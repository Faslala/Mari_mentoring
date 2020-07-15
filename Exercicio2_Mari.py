#-- coding: utf-8 --
'''
2. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: até 20 litros, desconto de 3% por litro acima de 20 litros, desconto de 5% por litro
Gasolina:até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina).
Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é 
R$ 1,90.'''

# duvida: como colocar o utf-8

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

alcool = 1.90
gasolina = 2.50

litros = float(input("Quantos litros de combustivel foi colocado no automovel? "))
combustivel = input("Foi utilizado A-alcool ou G-gasolina? ")

if combustivel == "A":

    if litros <= 20:
        valor1 = (litros * alcool) - (litros * alcool) * 3 / 100
        print("O valor a pagar eh " + locale.currency(valor1, grouping=True) + ", ja incluso o desconto de 3%.")

    elif litros > 20:
        valor2 = (litros * alcool) - (litros * alcool) * 5 / 100
        print("O valor a pagar eh " + locale.currency(valor2, grouping=True) + ", ja incluso o desconto de 5%.")

elif combustivel == "G":
    if litros <= 20:
        valor3 = (litros * gasolina) - (litros * gasolina) * 4 / 100
        print("O valor a pagar eh " + locale.currency(valor3, grouping=True) + ", ja incluso o desconto de 4%.")

    elif litros > 20:
        valor4 = (litros * gasolina) - (litros * gasolina) * 6 / 100
        print("O valor a pagar eh " + locale.currency(valor4, grouping=True) + ", ja incluso o desconto de 6%.")

else:
    print('\033[0;31mError: Inserir A para alcool ou G para gasolina!\033[m')
