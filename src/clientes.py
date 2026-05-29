class Cliente:
    def __init__(self, nome=None, cpf=None, telefone=None, endereco=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.ativo = True

    def __str__(self):
        status_texto = "Ativo" if self.ativo else "Bloqueado"
        return f"CLIENTE: {self.nome} | CPF: {self.cpf} | Status: {status_texto}"

    def cadastrar(self):
        print("\n--- Cadastro de Cliente ---")
        self.nome = input("Nome: ")
        self.cpf = input("CPF: ")
        self.telefone = input("Telefone: ")
        self.endereco = input("Endereço: ")
        print("Dados registrados!")
