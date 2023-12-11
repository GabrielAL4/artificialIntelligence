

def function_1():
    number = int(input("Insira o numero de numeros a serem inseridos: "))

    lista = []
    i = 0
    
    while i < number:
        i += 1
        value = float(input("Insira o valor na casa " + str(i) + ": "))
        lista.append(value)
        
    print("1 - Os valores digitados (originais)\n")
    print("2 - Os valores originais em índices pares\n")
    print("3 - Os valores originais em índices ímpares\n")
    print("4 - Cada valor da lista arredondado para 1 casa decimal\n")
    print("5 - O somatório de valores contidos na lista original arredondado para 2 casas decimais\n")
    print("6 - Cada valor da lista arredondado para inteiro\n")
    print("7 - Do inteiro de cada valor, mostrar no sistema binário\n")
    print("8 - Do inteiro de cada valor, mostrar no sistema octal\n")
    print("9 - Do inteiro de cada valor, mostrar no sistema hexadecimal.\n")

    op = 1
    
    while(op>0 and op<10):
     
        op = int(input('Insira a opção desejada: '))
        
        if op == 1:
            print(lista)
        elif op == 2:
            i = 0
            listPar = []
            while i < number:
                if(i%2==0):
                    listPar.append(lista[i])
            print(listPar)
        elif op == 3:
            for i in number:
                if(i%2!=0):
                    print(value)
        elif op == 4:
            for i in number:
                print("%.1f" % round(value, 1))
        elif op == 5:
            for i in number:
                sum += value

            print("%.2f" % round(sum, 2))
        elif op == 6:
            for i in number:
                print(round(value))
        elif op == 7:
            for i in number:
                print(bin(value))
        elif op == 8:
            for i in number:
                print(oct(value))
        elif op == 9:
            for i in number:
                print(hex(value))

function_1()