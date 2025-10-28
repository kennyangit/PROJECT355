import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Gerente:
    def __init__(self, comissao_percentual):
        self.comissao_percentual = comissao_percentual
        self.comissao = 0
        self.valor_liquido = 0
        self.despesas = 0

    def calcular_comissao(self, valor_bruto, despesas):
        """Subtrai as despesas do valor bruto, depois calcula a comissão sobre o valor restante"""
        valor_com_despesas = valor_bruto - despesas  # Subtrai as despesas do valor bruto

        # Se o valor bruto for negativo, comissão é zero, mas as despesas e valor líquido continuam a ser calculados
        if valor_com_despesas < 0:
            self.comissao = 0
        else:
            self.comissao = int(
                valor_com_despesas * (self.comissao_percentual / 100))  # Comissão sobre o valor com despesas

        # Calculando o valor líquido após a comissão (mesmo que a comissão seja zero)
        self.valor_liquido = int(valor_com_despesas - self.comissao)  # Subtrai a comissão do valor com despesas

        self.despesas = int(despesas)  # Arredondar despesas para inteiro

    def exibir_relatorio(self, valor_bruto):
        """Retorna os dados do relatório no formato desejado"""
        if self.valor_liquido < 0:
            if self.comissao == 0:
                return (f"VALOR BRUTO: {int(valor_bruto)}\n"
                 f"DESPESAS: {self.despesas}\n"
                 f"VALOR LÍQUIDO: {self.valor_liquido}\n"
                 f"\n{self.valor_liquido * -1} 🟥 TOTAL DA SEMANA")
            else:
                return (f"VALOR BRUTO: {int(valor_bruto)}\n"
                f"DESPESAS: {self.despesas}\n"
                f"COMISSÃO DO GERENTE: {self.comissao}\n"
                f"VALOR LÍQUIDO: {self.valor_liquido}\n"
                f"\n{self.valor_liquido * -1} 🟥 TOTAL DA SEMANA")
        if self.comissao == 0 and self.valor_liquido > 0:
            return (f"VALOR BRUTO: {int(valor_bruto)}\n"
                f"DESPESAS: {self.despesas}\n"
                f"VALOR LÍQUIDO: {self.valor_liquido}\n"
                f"\n{self.valor_liquido} 🟦 TOTAL DA SEMANA")
        if self.despesas == 0:
                if self.valor_liquido < 0:
                    return (f"VALOR BRUTO: {int(valor_bruto)}\n"
                    f"COMISSÃO DO GERENTE: {self.comissao}\n"
                    f"VALOR LÍQUIDO: {self.valor_liquido}\n"
                    f"\n{self.valor_liquido * -1} 🟥 TOTAL DA SEMANA")
        if self.despesas == 0:
            if self.valor_liquido > 0:
                return (f"VALOR BRUTO: {int(valor_bruto)}\n"
                    f"COMISSÃO DO GERENTE: {self.comissao}\n"
                    f"VALOR LÍQUIDO: {self.valor_liquido}\n"
                    f"\n{self.valor_liquido} 🟦 TOTAL DA SEMANA")
        return (f"VALOR BRUTO: {int(valor_bruto)}\n"
                f"DESPESAS: {self.despesas}\n"
                f"COMISSÃO DO GERENTE: {self.comissao}\n"
                f"VALOR LÍQUIDO: {self.valor_liquido}\n"
                f"\n{self.valor_liquido} 🟦 TOTAL DA SEMANA")


class SistemaDeGerencia:
    def __init__(self):
        self.gerentes = []

    def adicionar_gerente(self, comissao_percentual):
        """Adiciona um gerente ao sistema"""
        gerente = Gerente(comissao_percentual)
        self.gerentes.append(gerente)
        return gerente


def gerar_relatorio():
    try:
        comissao_percentual = float(entry_comissao.get())
        valor_bruto = float(entry_valor_bruto.get())
        despesas = float(entry_despesas.get())

        # Adiciona o gerente e gera o relatório
        gerente = sistema.adicionar_gerente(comissao_percentual)
        gerente.calcular_comissao(valor_bruto, despesas)

        # Exibe o relatório na área de texto
        resultado = gerente.exibir_relatorio(valor_bruto)
        text_resultado.config(state=tk.NORMAL)  # Permite editar o texto
        text_resultado.delete(1.0, tk.END)  # Limpa a área de texto
        text_resultado.insert(tk.END, resultado)  # Insere o novo relatório
        text_resultado.config(state=tk.DISABLED)  # Desabilita a edição
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para comissão, valor bruto e despesas.")


# Criação da janela principal
root = tk.Tk()
root.title("Gerenciamento de Comissões")

# Instanciando o sistema de gerentes
sistema = SistemaDeGerencia()

# Criando o Notebook (abas)
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill="both", expand=True)

# Criando a aba para inserção dos dados
aba_entrada = tk.Frame(notebook)
notebook.add(aba_entrada, text="BET355")

# Layout da interface na aba de entrada
frame_entrada = tk.Frame(aba_entrada)
frame_entrada.pack(padx=10, pady=10)

# Campo para Comissão Percentual
tk.Label(frame_entrada, text="Comissão Percentual:").grid(row=0, column=0, padx=5, pady=5)
entry_comissao = tk.Entry(frame_entrada, width=30)
entry_comissao.grid(row=0, column=1, padx=5, pady=5)

# Campo para Valor Bruto
tk.Label(frame_entrada, text="Valor Bruto:").grid(row=1, column=0, padx=5, pady=5)
entry_valor_bruto = tk.Entry(frame_entrada, width=30)
entry_valor_bruto.grid(row=1, column=1, padx=5, pady=5)

# Campo para Despesas
tk.Label(frame_entrada, text="Despesas:").grid(row=2, column=0, padx=5, pady=5)
entry_despesas = tk.Entry(frame_entrada, width=30)
entry_despesas.grid(row=2, column=1, padx=5, pady=5)

# Botão para Gerar Relatório
btn_gerar = tk.Button(aba_entrada, text="Gerar Relatório", command=gerar_relatorio)
btn_gerar.pack(pady=10)

# Área de texto para exibir o relatório
text_resultado = tk.Text(root, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED)
text_resultado.pack(padx=10, pady=10)

# Rodando a interface
root.mainloop()