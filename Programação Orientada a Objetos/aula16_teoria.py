from time import sleep

class ClasseQualquer:
    def fazer(self) -> None:
        print('\033[35mEstou fazendo algo...\033[m')
        sleep(1)

class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print('\033[36mEstou preparando algo...\033[m')
        sleep(1)

    def fazer(self) -> None: # duas classes com herança porém com metodos de nomes iguais e que fazem diferentes funções se chama polimorfismo
        print('\033[33mEstou fazendo outra coisa...\033[m')
        sleep(1)

objeto1 = ClasseQualquer()
objeto2 = OutraCoisa()

objeto1.fazer()
objeto2.fazer()
