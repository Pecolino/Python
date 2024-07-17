import customtkinter as ctk
from back import Calculadora

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("400x600")

        self.calc = Calculadora()

        self.display = ctk.CTkLabel(master, text="", width=392, height=120, fg_color="#333")
        self.display.place(x=5, y=15)

        self.criar_botoes()

    def atualizar_display(self):
        self.display.configure(text=self.calc.valor_atual)

    def adicionar_valor(self, valor):
        self.calc.adicionar_valor(valor)
        self.atualizar_display()

    def limpar(self):
        self.calc.limpar()
        self.atualizar_display()

    def calcular(self):
        self.calc.calcular()
        self.atualizar_display()

    def criar_botoes(self):
        botoes = [
            ('1', 10, 170), ('2', 110, 170), ('3', 210, 170),
            ('4', 10, 280), ('5', 110, 280), ('6', 210, 280),
            ('7', 10, 390), ('8', 110, 390), ('9', 210, 390),
            ('0', 110, 500), ('+', 310, 170), ('-', 310, 280),
            ('*', 310, 390), ('/', 310, 500), ('C', 10, 500),
            ('=', 210, 500)
        ]

        for (text, x, y) in botoes:
            if text == 'C':
                cmd = self.limpar
            elif text == '=':
                cmd = self.calcular
            else:
                cmd = lambda t=text: self.adicionar_valor(t)
            
            btn = ctk.CTkButton(self.master, text=text, command=cmd, width=75, height=50, fg_color="grey")
            btn.place(x=x, y=y)

if __name__ == "__main__":
    root = ctk.CTk()
    app = CalculadoraApp(root)
    root.mainloop()
