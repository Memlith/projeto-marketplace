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


class ListagemProdutosErro(Exception):
    pass


class FaltaEstoqueErro(Exception):
    pass


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
    def __init__(self, codigo, nome, cor, tamanho, preco, estoque):
        super().__init__(codigo, nome, preco, estoque)
        self.cor = cor
        self.tamanho = tamanho

    def descricao(self):
        pass


class Blusa(Produto):
    def __init__(self, codigo, nome, cor, tamanho, preco, estoque):
        super().__init__(codigo, nome, preco, estoque)
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

    def cadastrar_camiseta(self, codigo, nome, cor, tamanho, preco, estoque):
        print("Cadastrando camiseta...")
        try:
            new = Camiseta(codigo, nome, cor, tamanho, preco, estoque)
            self.produtos.append(new)
            print(" Produto cadastrado! ".center(64, "="))
        except Exception as erro:
            print(f"Erro ao cadastrar produto: {erro}")
        print("\n")

    def cadastrar_blusa(self, codigo, nome, cor, tamanho, preco, estoque):
        print("Cadastrando blusa...")
        try:
            new = Blusa(codigo, nome, cor, tamanho, preco, estoque)
            self.produtos.append(new)
            print(" Produto cadastrado! ".center(64, "="))
        except Exception as erro:
            print(f"Erro ao cadastrar produto: {erro}")
        print("\n")

    def listar_produtos(self):
        for produto in self.produtos:
            if isinstance(produto, Camiseta):
                print(" Camisetas ".center(64, "="))
                print(f"Código: {produto._codigo}")
                print(
                    f"\tNome: {produto._nome}\n\tCor: {produto.cor}\n\tTamanho: {produto.tamanho}\n\tPreço: {produto._preco}\n\tEstoque: {produto._estoque}\n\n"
                )
            elif isinstance(produto, Blusa):
                print(" Blusas ".center(64, "="))
                print(f"Código: {produto._codigo}")
                print(
                    f"\tNome: {produto._nome}\n\tCor: {produto.cor}\n\tTamanho: {produto.tamanho}\n\tPreço: {produto._preco}\n\tEstoque: {produto._estoque}\n\n"
                )
            else:
                raise ListagemProdutosErro("Erro ao listar os produtos do vendedor")
        print("\n")


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


# teste de vendedor
vendedor = Vendedor(1, "Caio")

vendedor.cadastrar_camiseta(1, "Camiseta Rock", "Preto", "M", 109.99, 8)
vendedor.cadastrar_blusa(1, "Blusa Rock", "Preto", "M", 109.99, 8)

vendedor.listar_produtos()
