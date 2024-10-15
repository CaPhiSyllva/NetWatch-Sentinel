import tkinter as tk
from tkinter import messagebox

class CyberSecurityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NetWatch XDR - Cyber Security")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")  # Cor de fundo

        # Estilo de fonte
        self.font = ("Arial", 12)

        # Cabeçalho
        self.header = tk.Frame(self.root, bg="#0056b3", bd=0, relief="flat")
        self.header.pack(pady=10, fill=tk.X)

        self.title = tk.Label(self.header, text="NetWatch XDR", fg="white", bg="#0056b3", font=("Arial", 18, "bold"))
        self.title.pack(pady=10)

        # Botões
        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        self.add_rule_button = self.create_button("Adicionar Regra", self.add_rule)
        self.remove_rule_button = self.create_button("Remover Regra", self.remove_rule)
        self.list_rules_button = self.create_button("Listar Regras", self.list_rules)

        # Adicionando os botões à interface
        self.add_rule_button.pack(pady=5)
        self.remove_rule_button.pack(pady=5)
        self.list_rules_button.pack(pady=5)

    def create_button(self, text, command):
        button = tk.Button(self.button_frame, text=text, command=command, font=self.font,
                           bg="#007bff", fg="white", bd=0, relief="flat", padx=10, pady=5)
        button.config(borderwidth=2, highlightbackground="#f0f0f0", highlightcolor="#0056b3", highlightthickness=2)
        button.bind("<Enter>", lambda e: button.config(bg="#0056b3"))
        button.bind("<Leave>", lambda e: button.config(bg="#007bff"))
        return button

    def add_rule(self):
        messagebox.showinfo("Adicionar Regra", "Função para adicionar regras ainda não implementada.")

    def remove_rule(self):
        messagebox.showinfo("Remover Regra", "Função para remover regras ainda não implementada.")

    def list_rules(self):
        messagebox.showinfo("Listar Regras", "Função para listar regras ainda não implementada.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberSecurityApp(root)
    root.mainloop()
