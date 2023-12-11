
def textFunction():
    string = str (input("Insira o texto: \n"))
    i = 0
    vogals = 'aeiou'
    textVogals = 0
    for i in string.lower():
        if i in vogals:
            textVogals+=1
    print("A quantidade de vogais no texto é {}".format(textVogals))


textFunction()