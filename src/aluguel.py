from datetime import date


class Aluguel:
    """Representa um registro de aluguel de veículo para um cliente."""

    _historico: list["Aluguel"] = []  

    def __init__(self, cliente, veiculo, data_inicio: date, data_fim: date):
        """
        Inicializa um aluguel.

        Args:
            cliente (Cliente): O cliente que está alugando.
            veiculo (Veiculo): O veículo a ser alugado.
            data_inicio (date): Data de início do aluguel.
            data_fim (date): Data prevista de devolução.
        """
        if data_fim <= data_inicio:
            raise ValueError("A data de devolução deve ser posterior à data de início.")

        self.cliente = cliente
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.ativo = True

        Aluguel._historico.append(self)

    @property
    def duracao_dias(self) -> int:
        """Retorna a duração do aluguel em dias."""
        return (self.data_fim - self.data_inicio).days

    @property
    def valor_total(self) -> float:
        """Calcula o valor total com base na diária do veículo."""
        return self.duracao_dias * self.veiculo.diaria

    def finalizar(self) -> None:
        """Marca o aluguel como encerrado e libera o veículo."""
        if not self.ativo:
            print("Este aluguel já foi finalizado.")
            return
        self.ativo = False
        print(f"Aluguel finalizado. Total cobrado: R$ {self.valor_total:.2f}")

    def exibir_dados(self) -> None:
        """Exibe os dados do aluguel de forma formatada."""
        status = "Ativo" if self.ativo else "Finalizado"
        print("=" * 40)
        print(f"  ALUGUEL [{status}]")
        print("=" * 40)
        print(f"  Cliente : {self.cliente.nome}")
        print(f"  Veículo : {self.veiculo.modelo} ({self.veiculo.placa})")
        print(f"  Início  : {self.data_inicio.strftime('%d/%m/%Y')}")
        print(f"  Devolução: {self.data_fim.strftime('%d/%m/%Y')}")
        print(f"  Duração : {self.duracao_dias} dia(s)")
        print(f"  Total   : R$ {self.valor_total:.2f}")
        print("=" * 40)

    @classmethod
    def listar_todos(cls) -> None:
        """Lista todos os aluguéis registrados no sistema."""
        if not cls._historico:
            print("Nenhum aluguel registrado.")
            return
        print(f"\n{'='*40}")
        print(f"  HISTÓRICO DE ALUGUÉIS ({len(cls._historico)} registro(s))")
        print(f"{'='*40}")
        for aluguel in cls._historico:
            aluguel.exibir_dados()

    @classmethod
    def listar_ativos(cls) -> list["Aluguel"]:
        """Retorna uma lista com apenas os aluguéis ativos."""
        ativos = [a for a in cls._historico if a.ativo]
        print(f"\nAluguéis ativos: {len(ativos)}")
        return ativos