from Classe import *

def main():
    # Instanciando um objeto
    lista1 = ToDoList()

    while True:
        # Tratamento de erro
        try:
            print("Bem vindo a sua To do list! O que você gostaria de fazer?")
            print("[1] Adicionar tarefa")
            print("[2] Excluir tarefa")
            print("[3] Listar suas tarefas")
            print("[4] Sair")
            op = int(input("- "))

            match op:
                case 1:
                    descrição = input("Qual tarefa você quer adicionar? \n - ")
                    # Chamendo o método e colocando a variavel do input como parametro
                    lista1.adicionar_tarefa(descrição)

                case 2:
                    print("Aqui estão suas tarefas")
                    # Chamando o método de listar
                    lista1.listar_tarefas()
                    indice = int(input("Qual você deseja excluir? \n - "))
                    # Chamendo o método e colocando a variavel do input como parametro
                    lista1.excluir_tarefa(indice)
                    print("Agora sua lista está assim:")
                    lista1.listar_tarefas()

                case 3:
                    print("Essas são suas tarefas")
                    # Chamando o método de listar
                    lista1.listar_tarefas()

                case 4:
                    # Para sair do software
                    break

                case _:
                    print("Opção invalida")

        # Tratamento de erro
        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)