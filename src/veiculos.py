class Veiculo:
    def __init__(self, placa, modelo, tipo, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.tipo = tipo  # "carro", "moto", "caminhao"
        self.valor_diaria = valor_diaria
        self.disponivel = True

    def alugar(self):
        if not self.disponivel:
            print(f"Veículo {self.modelo} já está alugado.")
            return False
        self.disponivel = False
        print(f"Veículo {self.modelo} alugado com sucesso.")
        return True

    def devolver(self):
        self.disponivel = True
        print(f"Veículo {self.modelo} devolvido com sucesso.")

    def exibir_dados(self):
        status = "Disponível" if self.disponivel else "Alugado"
        print(f"[{self.tipo.upper()}] {self.modelo} | Placa: {self.placa} | Diária: R${self.valor_diaria:.2f} | Status: {status}")