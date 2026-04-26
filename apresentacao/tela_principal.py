import tkinter as tk
from tkinter import ttk, messagebox

class TelaPrincipal:
    def __init__(self, root, casos_de_uso):
        self.root = root
        self.root.title("Sistema Bancário - Clean Architecture")
        self.root.geometry("450x350")
        
        self.casos_de_uso = casos_de_uso 

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill="both")

        self.aba_cadastro = ttk.Frame(self.notebook)
        self.aba_operacoes = ttk.Frame(self.notebook)
        self.aba_historico = ttk.Frame(self.notebook)

        self.notebook.add(self.aba_cadastro, text="Criar Conta")
        self.notebook.add(self.aba_operacoes, text="Depósito / Saque")
        self.notebook.add(self.aba_historico, text="Histórico")

        self._setup_aba_cadastro()
        self._setup_aba_operacoes()
        self._setup_aba_historico()

    def _setup_aba_cadastro(self):
        tk.Label(self.aba_cadastro, text="Nome:").pack(pady=2)
        self.entry_nome = tk.Entry(self.aba_cadastro, width=30)
        self.entry_nome.pack(pady=2)

        tk.Label(self.aba_cadastro, text="CPF:").pack(pady=2)
        self.entry_cpf = tk.Entry(self.aba_cadastro, width=30)
        self.entry_cpf.pack(pady=2)

        tk.Label(self.aba_cadastro, text="Saldo Inicial:").pack(pady=2)
        self.entry_saldo = tk.Entry(self.aba_cadastro, width=30)
        self.entry_saldo.pack(pady=2)

        tk.Button(self.aba_cadastro, text="Criar Conta", command=self.criar_conta, bg="lightblue").pack(pady=15)

    def _setup_aba_operacoes(self):
        tk.Label(self.aba_operacoes, text="Nº da Conta:").pack(pady=2)
        self.entry_num_conta_op = tk.Entry(self.aba_operacoes, width=20)
        self.entry_num_conta_op.pack(pady=2)

        tk.Label(self.aba_operacoes, text="Valor (R$):").pack(pady=2)
        self.entry_valor_op = tk.Entry(self.aba_operacoes, width=20)
        self.entry_valor_op.pack(pady=2)

        frame_botoes = tk.Frame(self.aba_operacoes)
        frame_botoes.pack(pady=15)
        
        tk.Button(frame_botoes, text="Depositar", command=self.depositar, bg="lightgreen", width=10).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Sacar", command=self.sacar, bg="lightcoral", width=10).pack(side="right", padx=5)

    def _setup_aba_historico(self):
        tk.Label(self.aba_historico, text="Nº da Conta:").pack(pady=2)
        self.entry_num_conta_hist = tk.Entry(self.aba_historico, width=20)
        self.entry_num_conta_hist.pack(pady=2)

        tk.Button(self.aba_historico, text="Buscar Histórico", command=self.buscar_historico).pack(pady=5)

        self.texto_historico = tk.Text(self.aba_historico, height=10, width=50)
        self.texto_historico.pack(pady=5)


    def criar_conta(self):
        try:
            saldo = float(self.entry_saldo.get()) if self.entry_saldo.get() else 0.0
            
            conta = self.casos_de_uso["criar_conta"].executar(
                self.entry_nome.get(), 
                self.entry_cpf.get(), 
                saldo
            )
            
            messagebox.showinfo("Sucesso", f"Conta criada!\nNúmero: {conta.numero}")
            self.entry_nome.delete(0, tk.END)
            self.entry_cpf.delete(0, tk.END)
            self.entry_saldo.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro de Regra de Negócio", str(e))

    def depositar(self):
        try:
            valor = float(self.entry_valor_op.get())
            numero = self.entry_num_conta_op.get()
            
            conta = self.casos_de_uso["depositar"].executar(numero, valor)
            
            messagebox.showinfo("Sucesso", f"Depósito efetuado!\nNovo saldo: R$ {conta.saldo:.2f}")
            self.entry_valor_op.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def sacar(self):
        try:
            valor = float(self.entry_valor_op.get())
            numero = self.entry_num_conta_op.get()
            
            conta = self.casos_de_uso["sacar"].executar(numero, valor)
            
            messagebox.showinfo("Sucesso", f"Saque efetuado!\nNovo saldo: R$ {conta.saldo:.2f}")
            self.entry_valor_op.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def buscar_historico(self):
        try:
            numero = self.entry_num_conta_hist.get()
            
            conta, transacoes = self.casos_de_uso["historico"].executar(numero)
            
            self.texto_historico.delete(1.0, tk.END)
            self.texto_historico.insert(tk.END, f"Cliente: {conta.cliente.nome} | Saldo: R$ {conta.saldo:.2f}\n")
            self.texto_historico.insert(tk.END, "-"*40 + "\n")
            for t in transacoes:
                self.texto_historico.insert(tk.END, f"{t['data']} | {t['tipo']} | R$ {t['valor']:.2f}\n")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))


