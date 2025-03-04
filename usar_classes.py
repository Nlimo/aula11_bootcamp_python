from classes import Processor


path = "./custo.csv"

df_path = Processor(path)
print(df_path.df)
print("################")
print(df_path.filtrar_por('custo', 10))
