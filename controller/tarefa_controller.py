from model.tarefa import Tarefa


class TarefaController:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def adicionar_tarefa(self, descricao):
        tarefa = Tarefa(self.proximo_id, descricao)
        self.tarefas.append(tarefa)
        self.proximo_id += 1

    def listar_tarefas(self):
        return self.tarefas

    def remover_tarefa(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                self.tarefas.remove(tarefa)
                return True
        return False

    def concluir_tarefa(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                tarefa.concluir()
                return True
        return False