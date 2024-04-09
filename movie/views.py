from django.shortcuts import render
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64
from movie.models import Movie




def home(request):
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.filter(title__icontains=searchTerm) if searchTerm else Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})

def about(request):
    # Aquí se ha corregido para no incluir un contexto si no se pasa nada
    return render(request, 'movie/about.html')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


def news(request):
    # Lógica para la vista de noticias
    return render(request, 'news.html')


def statistics_view(request):
    matplotlib.use('Agg')
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')  # Obtener todos los años de las películas
    movie_counts_by_year = {}  # Crear un diccionario para almacenar la cantidad de películas por año 
    for year in years:  # Contar la cantidad de películas por año
        if year:
            movies_in_year = Movie.objects.filter(year=year)
        else:
            movies_in_year = Movie.objects.filter(year__isnull=True)
            year = "None"
        movie_counts_by_year[str(year)] = movies_in_year.count()  # Convertir year a string para evitar problemas en la gráfica

    # Ordenar el diccionario por año para asegurar que las barras estén en orden cronológico
    movie_counts_by_year = dict(sorted(movie_counts_by_year.items()))

    # Ajustar el tamaño de la figura para que sea más ancho
    plt.figure(figsize=(18, 6))  # Ancho, alto en pulgadas

    # Crear la gráfica de barras
    plt.bar(list(movie_counts_by_year.keys()), list(movie_counts_by_year.values()), align='center')

    # Personalizar la gráfica
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    
    # Configurar las etiquetas del eje X para que solo muestren ciertos años y evitar la superposición
    plt.xticks(rotation=90)
    every_nth = 10  # Ajusta este número según la cantidad de años y el espacio disponible
    for n, label in enumerate(plt.gca().xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)

    # Ajustar los márgenes y la disposición
    plt.tight_layout()

    # Guardar la gráfica en un objeto BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()
    
    # Convertir la gráfica a base64
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    # Renderizar la plantilla statistics.html con la gráfica
    return render(request, 'statistics.html', {'graphic': graphic})