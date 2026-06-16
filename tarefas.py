class Tarefas:
    def __init__(self):
        self.lista = []

    def adicionar(self, nome):
        self.lista.append({
            "nome": nome,
            "concluida": False
        })

    def listar(self):
        for i, t in enumerate(self.lista, 1):
            s = "✓" if t["concluida"] else "o"
            print(f"{i}. [{s}] {t['nome']}")