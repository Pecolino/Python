class Calculadora:
    def __init__(self):
        self.valor_atual = ""
        self.resultado = 0

    def adicionar_valor(self, valor):
        self.valor_atual += str(valor)
        return self.valor_atual

    def limpar(self):
        self.valor_atual = ""
        self.resultado = 0
        return self.valor_atual

    def calcular(self):
        try:
            self.resultado = eval(self.valor_atual)
            self.valor_atual = str(self.resultado)
        except Exception as e:
            self.valor_atual = "Erro"
        return self.valor_atual
