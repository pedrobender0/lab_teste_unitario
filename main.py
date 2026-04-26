import tkinter as tk
from infraestrutura.arquivo_conta_repository import ArquivoContaRepository
from aplicacao.casos_de_uso import CriarContaUseCase, RealizarDepositoUseCase, ObterHistoricoUseCase
from aplicacao.realizar_saque_use_case import RealizarSaqueUseCase
from apresentacao.tela_principal import TelaPrincipal

if __name__ == "__main__":
   
    repositorio = ArquivoContaRepository()

    casos_de_uso = {
        "criar_conta": CriarContaUseCase(repositorio),
        "depositar": RealizarDepositoUseCase(repositorio),
        "sacar": RealizarSaqueUseCase(repositorio),
        "historico": ObterHistoricoUseCase(repositorio)
    }

   
    root = tk.Tk()
    
    app = TelaPrincipal(root, casos_de_uso) 
    
    root.mainloop()


