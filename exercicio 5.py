#exercicio 5

class CofreDoDragao:
    def __init__(self, nome_dragao, tesouros):
        self.nome_dragao=nome_dragao
        self.tesouros=tesouros
    
    def adicionar_item(self, nome, valor):
        if nome!="" and valor>0:
            novo_tesouro = {
                "nome":nome,
                "valor":valor
            }

            self.tesouros.append(novo_tesouro)

    def listar_itens(self):
        for total in self.tesouros:
            print(f"tesouro-{total['nome']}-{total['valor']}")

    def calcular_total(self):
        total=0
        for somar in self.tesouros:
            total=total+somar['valor']
        return(total)
    
    def encontrar_item_mais_valioso(self):
        final=1['valor']
        for somar in self.tesouros:
            if somar['valor']>final:
                final=somar['valor']