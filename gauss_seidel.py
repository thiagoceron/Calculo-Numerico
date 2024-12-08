def gauss_seidel(coeficientesMatriz, constanteMatriz, aproximacao, maxIteracoes=100, tolerancia=1e-10):
    n = len(constanteMatriz)
    solucoes = aproximacao.copy()
    
    for iteration in range(maxIteracoes):
        prev_solucoes = solucoes.copy()
        for i in range(n):
            sum1 = sum(coeficientesMatriz[i][j] * solucoes[j] for j in range(i))
            sum2 = sum(coeficientesMatriz[i][j] * prev_solucoes[j] for j in range(i + 1, n))
            solucoes[i] = (constanteMatriz[i] - sum1 - sum2) / coeficientesMatriz[i][i]
        
        if all(abs(solucoes[i] - prev_solucoes[i]) < tolerancia for i in range(n)):
            print(f'Convergência alcançada após {iteration + 1} iterações.')
            return solucoes
    
    print('Número máximo de iterações alcançado.')
    return solucoes

def input_float(text=''):
    while True:
        try:
            return float(input(f'{text}'))
        except ValueError:
            print('Valor inválido. Tente novamente.')

def input_int(text=''):
    while True:
        try:
            return int(input(f'{text}'))
        except ValueError:
            print('Valor inválido. Tente novamente.')

def main():
    print('Programa para resolver sistemas lineares pelo método de Gauss-Seidel\n')

    level = input_int('Qual o grau da matriz? ')
    coeficientesMatriz = []
    constanteMatriz = []

    for i in range(level):
        row = []
        for j in range(level):
            row.append(input_float(f'Insira o elemento a[{i+1}][{j+1}]: '))
        coeficientesMatriz.append(row)
        constanteMatriz.append(input_float(f'Insira o elemento b[{i+1}]: '))

    # Solicitar ao usuário os valores iniciais de aproximação
    aproximacao = []
    for i in range(level):
        aproximacao.append(input_float(f'Insira o valor inicial de aproximação x[{i+1}]: '))

    tolerancia = input_float('Insira a tolerância: ')
    maxIteracoes = input_int('Insira o número máximo de iterações: ')

    solucoes = gauss_seidel(coeficientesMatriz, constanteMatriz, aproximacao, maxIteracoes, tolerancia)

    print('\nSoluções do sistema:')
    for i, solucao in enumerate(solucoes):
        print(f'x[{i + 1}] = {solucao:.10f}')

if __name__ == "__main__":
    main()