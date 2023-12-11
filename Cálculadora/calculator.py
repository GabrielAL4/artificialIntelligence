#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:37:26 2023

> Criar um projeto de Calculadora Python, prevendo:

- Funções definidas para soma, subtração, multiplicação, divisão, potência, raiz: dois números N1 e N2 passados como parâmetros e 
retorno da referida operação. Estas funções deverão estar em um arquivo calculadora.py (back end) e importados em um main.py 
(front end) para testes via menu em loop, permitindo ao usuário escolher o uso das funções disponíveis. Documente seu código 
e funções desenvolvidas segundo o padrão "Python Docstring".

@author: gabriel
"""

import math as mt

"""Função voltada para realizar a soma de dois números inteiros"""
def sum():
    number1 = int(input("Insira o primeiro valor: "))
    number2 = int(input("Insira o segundo valor: "))
    result = number1 + number2
    print("A soma é: ", result)
    
"""Função que tem como objetivo fazer a subtração de dois números inteiros, sendo o 1º menos o 2º"""
def sub():
    number1 = input("Insira o primeiro valor: ")
    number2 = input("Insira o segundo valor: ")
    result = number1 - number2
    print("A subtração é: ", result)
    
"""Função na qual objetiva a multiplicação de dois números inteiros"""
def mult():
    number1 = input("Insira o primeiro valor: ")
    number2 = input("Insira o segundo valor: ")
    result = number1 * number2
    print("O resultado da multiplicação é: ", result)
    
"""Função que realiza a divisão de dois números inteiros de modo em que o 1º é o dividendo e o segundo o 2º"""
def div():
    number1 = input("Insira o primeiro valor: ")
    number2 = input("Insira o segundo valor: ")
    result = number1 / number2
    print("O resultado da divisão é: ", result)
    
"""Função que realiza a divisão de dois números inteiros, sendo o 1º a base e o 2º a potência"""
def pot():
    number1 = input("Insira o primeiro valor: ")
    number2 = input("Insira o segundo valor: ")
    result = pow(number1, number2)
    print("O resultado da divisão é: ", result)
    
"""Função que realiza a radiciação de dois números sendo o 1º o radicando e o 2º o índice"""
def rad():
    number1 = input("Insira o primeiro valor: ")
    number2 = input("Insira o segundo valor: ")
    number2 = 1/number2
    result =  mt.pow(number1, number2)
    print("O resultado da radiciação é: ", result)
    
