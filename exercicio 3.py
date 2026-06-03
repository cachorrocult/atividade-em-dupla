#exercicio 3
class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome=nome
        self.amostras=amostras
        self.capacidade_maxima=capacidade_maxima

    def adicionar_amostra(self, amostra):
        if amostra!="" and len(self.amostras)<self.capacidade_maxima:
            self.amostras.append(amostra)
        else:
            print("maximo de amostras coletadas ou espaço vazio")


    def listar_amostras(self):

        for total in range(len(self.amostras)):
            print(self.amostras[total])

    def contar_amostras(self):
        total=len(self.amostras)
        return (total)
    
    def verificar_armazenamento(self):

        if len(self.amostras)==self.capacidade_maxima:
            print("cheio")
        else:
            print("ainda pode coletar")

    def exibir_relatorio(self):

        if len(self.amostras)==self.capacidade_maxima:
            print(f"o robo {self.nome} coletou {len(self.amostras)} tendo capacidade para {self.capacidade_maxima} com o armazenamento estado cheio")
        else:
            print(f"o robo {self.nome} coletou {len(self.amostras)} tendo capacidade para {self.capacidade_maxima} com o armazenamento estado com espaço")

#---------------------principal---------------------------#

robozinho=RoboColetor("robo beta", [], 4)

opcao=0

while opcao!=6:
    print("1-coletar")
    print("2-listar")
    print("3-contar")
    print("4-verificar")
    print("5-relatorio")

    opcao=(int(input("escolhido: ")))
    if opcao==1:
        amostra=(input("amostra coletada: "))
        robozinho.adicionar_amostra(amostra)
    elif opcao==2:
         robozinho.listar_amostras()
    elif opcao==3:
        resultado=robozinho.contar_amostras()
        print(resultado)
    elif opcao==4:
        robozinho.verificar_armazenamento()
    elif opcao==5:
        robozinho.exibir_relatorio()