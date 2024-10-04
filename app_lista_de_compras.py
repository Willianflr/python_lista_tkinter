import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

class ListaComprasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Compras")
        self.root.configure(bg="#f0f0f0")
        self.root.geometry("500x350")

        self.lista = []

        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(pady=10)

        self.label = tk.Label(self.frame, text="Adicione um item:", bg="#f0f0f0", fg="#333", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, padx=10)

        self.entry = tk.Entry(self.frame, font=("Helvetica", 10), width=20)
        self.entry.grid(row=0, column=1, padx=10)

        self.add_button = tk.Button(self.frame, text="Adicionar", command=self.adicionar_item, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=20, pady=10)
        self.add_button.grid(row=1, column=0, pady=15)

        self.remove_button = tk.Button(self.frame, text="Remover", command=self.remover_item, bg="#F44336", fg="white", font=("Helvetica", 12), padx=20, pady=10)
        self.remove_button.grid(row=1, column=1, pady=5)

        self.view_button = tk.Button(self.frame, text="Ver Lista", command=self.ver_lista, bg="#2196F3", fg="white", font=("Helvetica", 12), padx=20, pady=10)
        self.view_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.save_button = tk.Button(self.frame, text="Salvar PDF", command=self.salvar_pdf, bg="#ff9932", fg="white", font=("Helvetica", 12), padx=20, pady=10)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.exit_button = tk.Button(self.frame, text="Sair", command=root.quit, bg="#9E9E9E", fg="white", font=("Helvetica", 12), padx=20, pady=10)
        self.exit_button.grid(row=4, column=0, columnspan=2, pady=10)


    def adicionar_item(self):
        item = self.entry.get().strip()
        if item:
            self.lista.append(item.upper())
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Sucesso", f'{item.upper()} ADICIONADO!')
        else:
            messagebox.showwarning("Atenção", "Digite um item para adicionar.")

    def remover_item(self):
        item = self.entry.get().strip()
        if item.upper() in self.lista:
            self.lista.remove(item.upper())
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Sucesso", f'{item.upper()} REMOVIDO!')
        else:
            messagebox.showwarning("Atenção", f'{item.upper()} não encontrado na lista.')

    def ver_lista(self):
        if self.lista:
            lista_str = "\n".join(self.lista)
            messagebox.showinfo("Lista de Compras", f'Sua lista:\n{lista_str}')
        else:
            messagebox.showwarning("Atenção", "A lista está vazia.")

    def salvar_pdf(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        pdf_path = os.path.join(desktop, "lista_de_compras.pdf")

        
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawString(50, 150, "Lista de Compras:")
        
        for i, item in enumerate(self.lista, start=1):
            c.drawString(100, 750 - (i * 20), f"{i}. {item}")

        c.save()
        messagebox.showinfo("Sucesso", f"Lista salva como {pdf_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaComprasApp(root)
    root.mainloop()
