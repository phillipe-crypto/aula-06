from flask import Blueprint, render_template, request, redirect, url_for
from controller.tarefa_controller import TarefaController


tarefa_bp = Blueprint("tarefa", __name__)

controller = TarefaController()


@tarefa_bp.route("/")
def index():
    tarefas = controller.listar_tarefas()
    return render_template("index.html", tarefas=tarefas)


@tarefa_bp.route("/adicionar", methods=["POST"])
def adicionar():
    descricao = request.form.get("descricao")

    if descricao:
        controller.adicionar_tarefa(descricao)

    return redirect(url_for("tarefa.index"))


@tarefa_bp.route("/remover/<int:id>", methods=["GET", "POST"])
def remover(id):
    controller.remover_tarefa(id)
    return redirect(url_for("tarefa.index"))


@tarefa_bp.route("/concluir/<int:id>", methods=["GET", "POST"])
def concluir(id):
    controller.concluir_tarefa(id)
    return redirect(url_for("tarefa.index"))