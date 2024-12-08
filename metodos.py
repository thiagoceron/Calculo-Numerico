import math


# Dicionário que mapeia nomes de funções para operações matemáticas correspondentes
func_map = {
    'sen': 'math.sin',
    'cos': 'math.cos',
    'tg': 'math.tan',
    'sec': '1 / math.cos',
    'cosec': '1 / math.sin',
    'tang': 'math.tan',
    'e': 'math.e',
    'raiz': 'x ** 0.5',
    'log': 'math.log',
    'ln': 'math.log'
}


def bisseccao(a, b, n, k, precisao, func, decimal_places):
    while abs(b - a) > precisao and k < n:
        k += 1
        y = (a + b) / 2
        z = func(y)
        if func(a) * z < 0:
            b = y
        else:
            a = y
        print("Número de iterações:", k)
        print("Raiz:", round(y, decimal_places))


def secante(x0, x1, precisao, max_iter, func, decimal_places):
    k = 1
    while k <= max_iter:
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(func(x2)) < precisao or abs(x2 - x1) < precisao:
            return round(x2, decimal_places), k
        x0, x1 = x1, x2
        k += 1
    print("Número máximo de iterações atingido. Última aproximação:", round(x2, decimal_places))
    return x2, k


def MIL(x0, precisao, func, decimal_places, max_iter):
    k = 1
    x1 = func(x0)
   
    while abs(func(x1)) > precisao and abs(x1 - x0) > precisao and k < max_iter:
        x0 = x1
        x1 = func(x0)
        k += 1
   
    print("Número de iterações:", k)
    print("Raiz:", round(x1, decimal_places))



def newton(x0, precisao, n, iteracao_max, func, derivada, decimal_places):
    # Condições de parada
    if abs(func(x0)) <= precisao or n >= iteracao_max:
        print("Raiz aproximada:", round(x0, decimal_places))
        print("Número de iterações:", n)
        return x0
    
    # Cálculo da próxima aproximação
    x1 = x0 - (func(x0) / derivada(x0))
    
    # Chamada recursiva
    return newton(x1, precisao, n + 1, iteracao_max, func, derivada, decimal_places)





def regula_falsi(a, b, delta1, maxIter, func, decimal_places):
    if func(a) * func(b) >= 0:
        print("A condição f(a) * f(b) < 0 não é satisfeita. Saindo.")
        return


    k = 0
    x_prev = a


    while k < maxIter:
        x = (a * func(b) - b * func(a)) / (func(b) - func(a))


        if abs(func(x)) < delta1:
            print(f"Raiz aproximada encontrada: {round(x, decimal_places)}")
            print(f"Número total de iterações: {k + 1}")
            return


        if func(a) * func(x) < 0:
            b = x
        else:
            a = x


        if abs(func(x)) < delta1:
            print(f"Raiz aproximada encontrada: {round(x, decimal_places)}")
            print(f"Número total de iterações: {k + 1}")
            return


        k += 1


    print("Número máximo de iterações atingido sem encontrar a raiz com a precisão desejada.")


def main():
    print("Digite a função (ex: x**2 - 2):")
    func_str = input()
   
    # Substitui os nomes das funções pelo seu equivalente em Python
    for key, value in func_map.items():
        func_str = func_str.replace(key, value)


    func_str = func_str.replace('^', '**')


    func = eval("lambda x: " + func_str)


    print("Escolha o método:")
    print("1. Bissecção")
    print("2. Secante")
    print("3. MIL")
    print("4. Newton")
    print("5. Regula Falsi")
    escolha = int(input("Digite a opção: "))
    decimal_places = int(input("Digite o número de casas decimais: "))


    if escolha == 1:
        a = float(input("Digite o intervalo a: "))
        b = float(input("Digite o intervalo b: "))
        precisao = float(input("Digite a precisão: "))
        bisseccao(a, b, 50, 0, precisao, func, decimal_places)
    elif escolha == 2:
        x0 = float(input("Digite x0: "))
        x1 = float(input("Digite x1: "))
        precisao = float(input("Digite a precisão: "))
        max_iter = int(input("Digite o número máximo de iterações: "))
        raiz, k = secante(x0, x1, precisao, max_iter, func, decimal_places)
        print("Raiz encontrada:", raiz)
        print("Número de Interações:", k)
    elif escolha == 3:
        x0 = float(input("Digite x0: "))
        precisao = float(input("Digite a precisão: "))
        max_iter = int(input("Digite o número máximo de iterações: "))
        MIL(x0, precisao, func, decimal_places, max_iter)
    elif escolha == 4:
        x0 = float(input("Digite x0: "))
        precisao = float(input("Digite a precisão: "))
       
        # Substitui os nomes das funções na derivada
        derivada_str = input("Digite a derivada da função: ")
        for key, value in func_map.items():
            derivada_str = derivada_str.replace(key, value)
        derivada_str = derivada_str.replace('^', '**')
       
        derivada = eval("lambda x: " + derivada_str)
       
        newton(x0, precisao, 0, 100, func, derivada, decimal_places)
    elif escolha == 5:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        delta1 = float(input("Digite a precisão delta1: "))
        regula_falsi(a, b, delta1, 100, func, decimal_places)
    else:
        print("Opção inválida. Saindo.")


if __name__ == "__main__":
    main()