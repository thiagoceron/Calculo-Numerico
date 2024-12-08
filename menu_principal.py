def menu():
    while True:
        print("\nMenu Principal:")
        print("1. Métodos")
        print("2. Gauss-Seidel")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("\nVocê escolheu Métodos.")
            from metodos import main as metodos_main
            metodos_main()
        elif escolha == "2":
            print("\nVocê escolheu Gauss-Seidel.")
            
            from gauss_seidel import main as gauss_seidel_main
            gauss_seidel_main()
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()