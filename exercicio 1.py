#exercicio 1
class CapsulaDoTempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor=autor
        self.mensagem=mensagem
        self.ano_abertura=ano_abertura
        self.ano_atual=ano_atual

    def pode_abrir(self):
            
        if self.ano_atual<self.ano_abertura:
            return ("nao pode abrir")
        else:
            return ("pode ser aberta")

    def calcular_espera(self):

        espera=self.ano_abertura-self.ano_atual

        if espera<0:
            espera=0

        return espera

    def classificar_espera(self):
        
        espera=self.calcular_espera()
        
        if espera==0:
            print("pode abrir agora.")
        elif espera>=1 and espera<=3:
            print(" espera curta.")
        else:
            print("espera longa.")

    def exibir_resumo(self):
        if self.ano_atual < self.ano_abertura:
            print(f"o autor {self.autor} eve abrir a capsula em {self.ano_abertura} por isso ela esta fechada e a mensagem é {self.mensagem}")
        else:
            print(f"o autor {self.autor} eve abrir a capsula em {self.ano_abertura} por isso ela esta aberta e mostrando a mensagem {self.mensagem}")
#----------------------principal---------------------#

nome=(input("nome: "))
texto=(input("mensagem: "))
ano1=int(input("ano: "))
ano_atual=int(input("ano "))
minha_capsula=CapsulaDoTempo(nome,texto,ano1,ano_atual)
           
minha_capsula.calcular_espera()
minha_capsula.pode_abrir()
minha_capsula.classificar_espera()




