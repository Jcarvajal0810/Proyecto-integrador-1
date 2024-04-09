import pandas as pd
import json

# Lee el archivo CSV desde la ruta absoluta en la carpeta raíz del proyecto
df = pd.read_csv('titles.csv')  # Cambio de 'movies_initial.csv' a 'titles.csv'

# Guarda el DataFrame como JSON en la carpeta raíz del proyecto, con cada fila como un registro
df.to_json('titles.json', orient ='records')  # Cambio de 'movies.json' a 'titles.json'

# Lee el archivo JSON para verificar que la información se ha guardado correctamente
with open('titles.json', 'r') as file:  # Cambio de 'movies.json' a 'titles.json'
    movies = json.load(file)

# Imprime cada registro del archivo JSON
for movie in movies:
    print(movie)
