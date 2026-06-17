class Tarefas:
    def __init__(self):
        self.lista = []
<<<<<<< HEAD

    def adicionar(self, nome, prioridade="normal"):
        self.lista.append({
            "nome": nome,
            "prioridade": prioridade,
            "concluida": False
        })

    def listar(self):
        if not self.lista:
            print("Nenhuma tarefa cadastrada.")
            return
        for i, t in enumerate(self.lista, 1):
            s = "✓" if t["concluida"] else "o"
            p = t.get("prioridade", "normal")
            print(f"{i}. [{s}] {t['nome']} ({p})")
 
    def listar(self):
        if not self.lista:
            print("Nenhuma tarefa cadastrada.")
            return
        for i, t in enumerate(self.lista, 1):
            s = "✓" if t["concluida"] else "○"
            print(f"{i}. [{s}] {t['nome']}")
 
    def concluir(self, indice):
        if 0 <= indice < len(self.lista):
            self.lista[indice]["concluida"] = True
            print("✓ Tarefa concluída!")
        else:
            print("Tarefa não encontrada.")
>>>>>>> 01646c6 (maneiro)
