def calculadora(a, b, operacao):
    if operacao  == "+":
        soma = a + b
        print (soma)

    elif operacao == "-":
        sub = a - b
        print(sub)

    elif operacao == "*":
        mult = a * b
        print(mult)

    elif operacao == "/":
        div = a / b 
        print(div)

    else:
        print("Operação inválida")


calculadora(1,6,"+")

calculadora(40,17,"-")

calculadora(50,3,"*")

calculadora(25,5,"/")

calculadora(1,2,"qualquer coisa entre aspas")