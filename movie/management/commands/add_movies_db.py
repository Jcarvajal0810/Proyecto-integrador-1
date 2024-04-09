from django.core.management.base import BaseCommand
from movie.models import Movie
import json

class Command(BaseCommand):
    help = "Load movies from titles.json into the Movie model"

    def handle(self, *args, **kwargs):
        json_file_path = r'C:\Users\57304\OneDrive\Escritorio\PI1_2024-1\moviereviewsproject\titles.json'
        with open(json_file_path, 'r') as file:
            movies_data = json.load(file)
            for movie_data in movies_data:
                # Verifica que el objeto de película tenga un título no vacío
                title = movie_data.get('title')
                if title:  # Verifica que title no sea None o una cadena vacía
                    genre = ', '.join(movie_data.get('genres', ['Unknown']))
                    year = movie_data.get('release_year', None)
                    # Intenta crear la película en la base de datos
                    Movie.objects.get_or_create(
                        title=title,
                        defaults={'image': 'movie/images/default.jpg', 'genre': genre, 'year': year}
                    )
                else:
                    # Imprime un mensaje de error para registros sin título
                    print(f'Error: Registro sin título encontrado {movie_data}')
        self.stdout.write(self.style.SUCCESS('Películas agregadas exitosamente a la base de datos'))
