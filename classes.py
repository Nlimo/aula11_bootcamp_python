import pandas as pd

class Processor:
    def __init__(self, arquivo: str):
        self.csv = pd.read_csv(arquivo)
        self.df_filtrado = pd.DataFrame
        self.df = self.csv

    ## receber um str str[]
    def filtrar_por(self, colunas, atributos):
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.filtrar_por(colunas[1:], atributos[1:])
    
    def tratando_nulos(self):
        self.df = self.df.dropna(subset=['cidade', 'custo'], how='all')
        return self.df


        