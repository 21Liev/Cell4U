import pandas as pd
df = pd.read_csv("src\components\movilebd.csv")
df.to_json("celulares.json", orient="records", indent=4)
print("Archivo JSON creado con éxito.")
print(df.head)