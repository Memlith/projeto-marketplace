from abc import ABC, abstractmethod

print(
    f"""
{" Tecnicas de Programacao ".center(64, '=')}
Grupo 5 - Tema 10
Caio Simonassi
Lucas Corrêa

Tema 10 - Plataforma de Marketplace
Permite cadastrar produtos, vendedores e clientes. Os usuários podem listar produtos disponíveis, simular uma compra e 
ver detalhes de pedidos. O sistema pode incluir carrinho e controle de estoque básico.


{" Peita Shop ".center(64, '=')}
"""
)


# classe produto com atributos privados e getters e setters para os atributos necessarios
class Produto(ABC):
    def __init__(self, codigo, nome, preco, estoque):
        self._codigo = codigo
        self._nome = nome
        self._preco = preco
        self._estoque = estoque

    @abstractmethod
    def descricao(self):
        pass


class Camiseta(Produto):
    def __init__(self, codigo, nome, preco, estoque, cor, tamanho):
        super().__init__(codigo, nome, preco, estoque)
        self.cor = cor
        self.tamanho = tamanho

    def descricao(self):
        return f"Camiseta {self._nome} ({self.cor}, {self.tamanho}) - R${self._preco:.2f} (Estoque: {self._estoque})"


class Blusa(Produto):
    def __init__(self, codigo, nome, preco, estoque, cor, tamanho):
        super().__init__(codigo, nome, preco, estoque)
        self.cor = cor
        self.tamanho = tamanho

    def descricao(self):
        return f"Blusa {self._nome} ({self.cor}, {self.tamanho}) - R${self._preco:.2f} (Estoque: {self._estoque})"


# classe usuario
class Usuario(ABC):
    def __init__(self, nome):
        self._nome = nome

    @abstractmethod
    def tipo(self):
        pass


# classe vendedor que herda de Usuario
class Vendedor(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(nome)
        self._codigo = codigo
        self.produtos = []

    def tipo(self):
        return "Vendedor"

    def cadastrar_produto(self, codigo, nome, cor, preco, estoque):
        try:
            new = Camiseta(codigo, nome, preco, estoque, cor, "M") # Tamanho fixo para exemplo, pode ser melhorado
            self.produtos.append(new)
            print("Produto cadastrado!")
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        print("--- Seus Produtos ---")
        for produto in self.produtos:
            print(produto.descricao())


# classe cliente que Herda de usuario tambem, e tem o carrinho e os pedidos feitos pelo usuario
class Cliente(Usuario):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self._cpf = cpf
        self.carrinho = Carrinho(self)
        self.pedidos = []

    def tipo(self):
        return "Cliente"


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        if produto._estoque >= quantidade:
            self.itens.append({"produto": produto, "quantidade": quantidade})
            produto._estoque -= quantidade
            print(f"{quantidade}x {produto._nome} adicionado ao carrinho.")
        else:
            print(f"Estoque insuficiente para {produto._nome}. Disponível: {produto._estoque}")

    def remover_item(self, produto):
        for item in self.itens:
            if item["produto"] == produto:
                produto._estoque += item["quantidade"]
                self.itens.remove(item)
                print(f"{produto._nome} removido do carrinho.")
                return
        print(f"{produto._nome} não encontrado no carrinho.")

    def listar_itens(self):
        if not self.itens:
            print("Carrinho vazio.")
            return
        print("--- Itens no Carrinho ---")
        total = 0
        for item in self.itens:
            produto = item["produto"]
            quantidade = item["quantidade"]
            subtotal = produto._preco * quantidade
            print(f"{quantidade}x {produto._nome} - R${subtotal:.2f}")
            total += subtotal
        print(f"Total: R${total:.2f}")

    def finalizar_compra(self):
        if not self.itens:
            print("Carrinho vazio. Não é possível finalizar a compra.")
            return
        pedido = Pedidos(self.cliente, self.itens)
        self.cliente.pedidos.append(pedido)
        self.itens = [] # Limpa o carrinho após a compra
        print("Compra finalizada com sucesso!")


class Pedidos:
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self.status = "Pendente"

    def armazenar_pedidos(self):
        # Este método é mais para simular o armazenamento, pois já estamos adicionando na lista de pedidos do cliente
        print(f"Pedido do cliente {self.cliente._nome} armazenado. Status: {self.status}")

    def listar_pedidos(self):
        if not self.cliente.pedidos:
            print("Nenhum pedido realizado.")
            return
        print(f"--- Pedidos de {self.cliente._nome} ---")
        for i, pedido in enumerate(self.cliente.pedidos):
            print(f"Pedido {i+1} (Status: {pedido.status}):")
            for item in pedido.itens:
                produto = item["produto"]
                quantidade = item["quantidade"]
                print(f"  {quantidade}x {produto._nome} - R${produto._preco:.2f}")


# classe sistema que gerencia e acessa as outras classes
class Sistema:
    def __init__(self):
        self.vendedores = []
        self.clientes = []
        self.produtos_disponiveis = [] # Todos os produtos cadastrados por vendedores

    def _menu_vendedor(self, vendedor):
        while True:
            print("\n--- Menu do Vendedor ---")
            print("1. Cadastrar Produto")
            print("2. Listar Meus Produtos")
            print("3. Voltar ao Menu Principal")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                codigo = input("Código do produto: ")
                nome = input("Nome do produto: ")
                preco = float(input("Preço: "))
                estoque = int(input("Estoque: "))
                cor = input("Cor: ")
                tamanho = input("Tamanho: ") # Adicionado para Camiseta/Blusa
                # Simplificado para cadastrar apenas Camiseta por enquanto
                novo_produto = Camiseta(codigo, nome, preco, estoque, cor, tamanho)
                vendedor.produtos.append(novo_produto)
                self.produtos_disponiveis.append(novo_produto)
                print("Produto cadastrado com sucesso!")
            elif opcao == "2":
                vendedor.listar_produtos()
            elif opcao == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def _menu_cliente(self, cliente):
        while True:
            print("\n--- Menu do Cliente ---")
            print("1. Listar Produtos Disponíveis")
            print("2. Adicionar Produto ao Carrinho")
            print("3. Ver Carrinho")
            print("4. Finalizar Compra")
            print("5. Ver Meus Pedidos")
            print("6. Voltar ao Menu Principal")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                if not self.produtos_disponiveis:
                    print("Nenhum produto disponível no momento.")
                    continue
                print("--- Produtos Disponíveis ---")
                for i, produto in enumerate(self.produtos_disponiveis):
                    print(f"{i+1}. {produto.descricao()}")
            elif opcao == "2":
                self._adicionar_ao_carrinho(cliente)
            elif opcao == "3":
                cliente.carrinho.listar_itens()
            elif opcao == "4":
                cliente.carrinho.finalizar_compra()
            elif opcao == "5":
                cliente.pedidos[0].listar_pedidos() if cliente.pedidos else print("Nenhum pedido realizado.") # Acessa o primeiro pedido para listar todos
            elif opcao == "6":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def _adicionar_ao_carrinho(self, cliente):
        if not self.produtos_disponiveis:
            print("Nenhum produto disponível para adicionar ao carrinho.")
            return
        print("--- Produtos Disponíveis ---")
        for i, produto in enumerate(self.produtos_disponiveis):
            print(f"{i+1}. {produto.descricao()}")
        try:
            escolha = int(input("Digite o número do produto para adicionar ao carrinho: ")) - 1
            if 0 <= escolha < len(self.produtos_disponiveis):
                produto_selecionado = self.produtos_disponiveis[escolha]
                quantidade = int(input(f"Quantas unidades de {produto_selecionado._nome} deseja adicionar? "))
                cliente.carrinho.adicionar_item(produto_selecionado, quantidade)
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    def run(self):
        while True:
            print("\n--- Bem-vindo ao Peita Shop! ---")
            print("1. Entrar como Vendedor")
            print("2. Entrar como Cliente")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome_vendedor = input("Nome do Vendedor: ")
                vendedor_encontrado = next((v for v in self.vendedores if v._nome == nome_vendedor), None)
                if not vendedor_encontrado:
                    codigo_vendedor = len(self.vendedores) + 1
                    vendedor_encontrado = Vendedor(codigo_vendedor, nome_vendedor)
                    self.vendedores.append(vendedor_encontrado)
                    print(f"Vendedor {nome_vendedor} cadastrado com sucesso!")
                self._menu_vendedor(vendedor_encontrado)
            elif opcao == "2":
                nome_cliente = input("Nome do Cliente: ")
                cliente_encontrado = next((c for c in self.clientes if c._nome == nome_cliente), None)
                if not cliente_encontrado:
                    cpf_cliente = input("CPF do Cliente: ")
                    cliente_encontrado = Cliente(nome_cliente, cpf_cliente)
                    self.clientes.append(cliente_encontrado)
                    print(f"Cliente {nome_cliente} cadastrado com sucesso!")
                self._menu_cliente(cliente_encontrado)
            elif opcao == "3":
                print("Obrigado por usar o Peita Shop!")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema = Sistema()
    sistema.run()