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
\n\n{" Peita Shop ".center(64, '=')}
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
        pass


class Blusa(Produto):
    def __init__(self, codigo, nome, preco, estoque, cor, tamanho):
        super().__init__(codigo, nome, cor, preco, estoque)
        self.cor = cor
        self.tamanho = tamanho

    def descricao(self):
        pass


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
            new = Camiseta(codigo, nome, cor, preco, estoque)
            self.produtos.append(new)
            print("Produto cadastrado!")
        except Exception:
            print(f"Erro ao cadastrar produto: {Exception}")

    def listar_produtos(self):
        for produto in self.produtos:
            pass
            # TODO: Terminar isso aqui


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
    def __init__(self):
        pass

    # TODO: Adicionar funcs de adicionar e remover items no carrinho, listar items no carrinho, finalizar compra.


class Pedidos:
    def __init__(self):
        pass

    # TODO: Adicionar funcs de armazenar pedidos, listar pedidos


# classe sistema que gerencia e acessa as outras classes
class Sistema:
    def __init__(self):
        pass

    # TODO: Fazer um menu, com as opcoes de entrar como vendedor ou cliente, com suas respectivas opcoes ( ou nao )
