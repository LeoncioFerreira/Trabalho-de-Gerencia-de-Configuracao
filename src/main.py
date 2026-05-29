from datetime import date

from clientes import Cliente
from veiculos import Veiculo
from aluguel import Aluguel


veiculos = [
    Veiculo("ABC-1234", "Civic", "carro", 150),
    Veiculo("XYZ-9090", "CG 160", "moto", 80),
    Veiculo("JKL-7777", "Volvo FH", "caminhao", 450)
]

clientes = []
alugueis = []


def cadastrar_cliente():
    cliente = Cliente()
    cliente.cadastrar()
    clientes.append(cliente)
    print("\nCliente cadastrado com sucesso!")


def listar_clientes():
    if not clientes:
        print("\nNenhum cliente cadastrado.")
        return

    print("\n=== CLIENTES ===")
    for i, cliente in enumerate(clientes):
        print(f"{i + 1}. {cliente}")


def listar_veiculos():
    print("\n=== VEÍCULOS DISPONÍVEIS ===")

    for i, veiculo in enumerate(veiculos):
        print(f"{i + 1}. ", end="")
        veiculo.exibir_dados()


def realizar_aluguel():
    if not clientes:
        print("\nCadastre um cliente primeiro.")
        return

    listar_clientes()
    cliente_index = int(input("\nEscolha o cliente: ")) - 1

    listar_veiculos()
    veiculo_index = int(input("\nEscolha o veículo: ")) - 1

    cliente = clientes[cliente_index]
    veiculo = veiculos[veiculo_index]

    if not veiculo.disponivel:
        print("\nVeículo indisponível.")
        return

    dias = int(input("Quantidade de dias do aluguel: "))

    data_inicio = date.today()
    data_fim = date.fromordinal(data_inicio.toordinal() + dias)

    veiculo.alugar()

    aluguel = Aluguel(
        cliente,
        veiculo,
        data_inicio,
        data_fim
    )

    alugueis.append(aluguel)

    print("\nAluguel realizado com sucesso!")
    aluguel.exibir_dados()


def devolver_veiculo():
    ativos = [a for a in alugueis if a.ativo]

    if not ativos:
        print("\nNenhum aluguel ativo.")
        return

    print("\n=== ALUGUÉIS ATIVOS ===")

    for i, aluguel in enumerate(ativos):
        print(
            f"{i + 1}. "
            f"{aluguel.cliente.nome} -> "
            f"{aluguel.veiculo.modelo}"
        )

    escolha = int(input("\nEscolha o aluguel: ")) - 1

    aluguel = ativos[escolha]

    aluguel.finalizar()
    aluguel.veiculo.devolver()


def menu():
    while True:
        print("\n" + "=" * 40)
        print(" SISTEMA DE ALUGUEL DE VEÍCULOS ")
        print("=" * 40)

        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Listar veículos")
        print("4. Realizar aluguel")
        print("5. Devolver veículo")
        print("6. Histórico de aluguéis")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_cliente()

            case "2":
                listar_clientes()

            case "3":
                listar_veiculos()

            case "4":
                realizar_aluguel()

            case "5":
                devolver_veiculo()

            case "6":
                Aluguel.listar_todos()

            case "0":
                print("\nEncerrando sistema...")
                break

            case _:
                print("\nOpção inválida.")


if __name__ == "__main__":
    menu()