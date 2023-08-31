class ToDoList:
    # Construtor padrão para definir o dicionario e variavel
    def __init__(self):
        # Dicionario onde as tarefas estão armazenads
        self.tarefas = {}
        # Variavel correspondente ao indice
        self.num = 0

    # Metodo para adicionar tarefa
    def adicionar_tarefa(self,descrição):
        # Adicionando 1 ao indice para quando um nova tarefa for adicionada o número aumente
        self.num += 1
        self.descrição = descrição
        # Adicionando a tarefa ao dicionario
        self.tarefas[self.num] = self.descrição

    def excluir_tarefa(self,indice):
        # Excluindo a tarefa do dicionario a partir do indice(chave)
        self.tarefas.pop(indice)
        

    def listar_tarefas(self):
        print("Tarefas:")
        # Percorrendo o dicionario
        for chave, valor in self.tarefas.items():
            print(f"{chave}. {valor} \n")