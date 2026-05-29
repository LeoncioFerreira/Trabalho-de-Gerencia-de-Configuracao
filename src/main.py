from clientes import Cliente


def main():
    print("=== Sistema de Aluguel de Veículos ===")
    cliente_1 = Cliente()
    cliente_1.cadastrar()
    print("\nResumo do Cadastro:")
    print(cliente_1)


if __name__ == "__main__":
    main()
