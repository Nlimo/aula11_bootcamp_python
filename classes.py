import pandas as pd

class Processor:
    def __init__(self, arquivo: str):
        self.csv = pd.read_csv(arquivo)
        self.df_filtrado = pd.DataFrame
        self.df = self.csv

    def filtrar_por(self, atributo: str, valor: str):
        self.df_filtrado = self.df[self.df[atributo] == valor]
        return self.df_filtrado



        