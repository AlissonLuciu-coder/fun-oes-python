def calculadora(a, b, operacao):
    if operacao == "+":
        resultado = a + b
        print(resultado)

    elif operacao == "-":
        resultado = a - b
        print(resultado)

    elif operacao == "*":
        resultado = a * b
        print(resultado)

    elif operacao == "/":
        resultado = a / b
        print(resultado)  
             
    else:
        print("Operação inválida")

calculadora(1, 6, "+")        # 7
calculadora(40, 17, "-")      # 23
calculadora(50, 3, "*")       # 150
calculadora(10/2, 5, "/")     # (10/2)=5.0 / 5 = 1.0