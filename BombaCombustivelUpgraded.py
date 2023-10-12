class BombaCombustivel:
    def __init__(self, valor_litro, quantidade_disponivel):
        self.valor_litro = valor_litro
        self.quantidade_disponivel = quantidade_disponivel
    
    @property
    def valor_litro(self):
        return self._valor_litro

    @valor_litro.setter
    def valor_litro(self, valor_litro):
        if valor_litro < 0:
            raise ValueError("O valor do litro não pode ser negativo")
        self._valor_litro = valor_litro

    @property
    def quantidade_disponivel(self):
        return self._quantidade_disponivel

    @quantidade_disponivel.setter
    def quantidade_disponivel(self, quantidade_disponivel):
        if quantidade_disponivel < 0:
            raise ValueError("A quantidade disponível não pode ser negativa")
        self._quantidade_disponivel = quantidade_disponivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        if litros > self.quantidade_disponivel:
            raise ValueError("A quantidade solicitada é maior que a quantidade disponível")
        self.quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro(self, litros):
        valor = litros * self.valor_litro
        if litros > self.quantidade_disponivel:
            raise ValueError("A quantidade solicitada é maior que a quantidade disponível")
        self.quantidade_disponivel -= litros
        return valor
#Acima foi a construção da classe BombaCombustivel e seus métodos

class Gasolina(BombaCombustivel):  
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)
        self.tipo_combustivel = "Gasolina"

class Etanol(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)
        self.tipo_combustivel = "Etanol"

def exibir_menu():
    print("Escolha a ação desejada:")
    print("1. Abastecer por quantidade de litros")
    print("2. Abastecer por valor em reais")
    print("3. Sair")

#função para o código ser utilizado apenas no fonte principal("main code")
def main():
    gasolina = Gasolina(5, 1000)
    etanol = Etanol(4, 800)

    while True:
        exibir_menu()
        escolha = input("Digite o número correspondente à ação desejada: ")

        if escolha == '1':
            tipo_combustivel = input("Digite o tipo de combustível (1 para Gasolina, 2 para Etanol): ")
            quantidade_litros = float(input("Digite a quantidade de litros desejada: "))
            if tipo_combustivel == '1':
                try:
                    valor_a_pagar = gasolina.abastecer_por_litro(quantidade_litros)
                    print(f"Abasteceram {quantidade_litros:.2f} litros de gasolina. Valor a pagar: R$ {valor_a_pagar:.2f}")
                except ValueError as e:
                    print(e)
            elif tipo_combustivel == '2':
                try:
                    valor_a_pagar = etanol.abastecer_por_litro(quantidade_litros)
                    print(f"Abasteceram {quantidade_litros:.2f} litros de etanol. Valor a pagar: R$ {valor_a_pagar:.2f}")
                except ValueError as e:
                    print(e)
            else:
                print(f"Opção inválida. Escolha 1 para Gasolina ou 2 para Etanol.")
        elif escolha == '2':
            tipo_combustivel = input(f"Digite o tipo de combustível (1 para Gasolina, 2 para Etanol): ")
            valor_pago = float(input(f"Digite o valor em reais a ser abastecido: "))
            if tipo_combustivel == '1':
                try:
                    litros_abastecidos = gasolina.abastecer_por_valor(valor_pago)
                    print(f"Abasteceram {litros_abastecidos:.2f} litros de gasolina com R$ {valor_pago:.2f}")
                except ValueError as e:
                    print(e)
            elif tipo_combustivel == '2':
                try:
                    litros_abastecidos = etanol.abastecer_por_valor(valor_pago)
                    print(f"Abasteceram {litros_abastecidos:.2f} litros de etanol com R$ {valor_pago:.2f}")
                except ValueError as e:
                    print(e)
            else:
                print(f"Opção inválida. Escolha 1 para Gasolina ou 2 para Etanol.")
        elif escolha == '3':
            print(f"Obrigado por abastecer no posto FJJPS!")
            break
        else:
            print(f"Opção inválida. Escolha um número válido do menu.")

#faz com que o código não seja executado quando importado em forma de biblioteca(Import ... from ... ) 
if __name__ == "__main__":
    main()