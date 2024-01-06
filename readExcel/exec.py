import pandas as pd

excel_file = 'readExcel/test.xlsx'

df = pd.read_excel(excel_file)

for indice, fila in df.iterrows():
    nombre = fila["nombre"]
    pareja = "Soltero"
    if(fila["relacion"]):
        for indice2, fila2 in df.iterrows():
            if(fila["relacion"] - fila2["id"] == 0):
                pareja = fila2["nombre"]
    print("--------------------------")
    print(nombre + " Pareja: " + pareja)
