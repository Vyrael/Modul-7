import random

class library:
   
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        # Variables
        self.view_count = 0 

    def play(self, step = 1):
        self.view_count += step
    
class movie(library):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.release_year})'
   
class series(library):
   
    def __init__(self,episode_no,season_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_no = episode_no
        self.season_no = season_no
      
    def __str__(self):
        if self.episode_no < 10 and self.season_no < 10:
            return f'{self.title} S0{self.episode_no}E0{self.season_no}'
        elif self.episode_no < 10:
            return f'{self.title} S0{self.episode_no}E{self.season_no}'
        elif self.season_no < 10:
            return f'{self.title} S{self.episode_no}E0{self.season_no}'
        else:
            return f'{self.title} S{self.episode_no}E{self.season_no}'
    
movie1 = movie(title = "Matrix", release_year=1999, genre="scifi")
movie2 = movie(title = "Fight Club", release_year=1999, genre="drama")
movie3 = movie(title="Inception", release_year=2010, genre="Sci-Fi")
movie4 = movie(title="The Shawshank Redemption", release_year=1994, genre="Drama")
movie5 = movie(title="Pulp Fiction", release_year=1994, genre="Crime")
movie6 = movie(title="The Dark Knight", release_year=2008, genre="Action")
movie7 = movie(title="Forrest Gump", release_year=1994, genre="Drama")
movie8 = movie(title="The Godfather", release_year=1972, genre="Crime")
movie9 = movie(title="Avatar", release_year=2009, genre="Sci-Fi")
movie10 = movie(title="Titanic", release_year=1997, genre="Romance")

series1 = series(title = "Sopranos", release_year=2000, genre="crime", episode_no=15, season_no = 8)
series2 = series(title="Stranger Things", release_year=2016, genre="Sci-Fi", episode_no=8, season_no=4)
series3 = series(title="Game of Thrones", release_year=2011, genre="Fantasy", episode_no=10, season_no=8)
series4 = series(title="The Crown", release_year=2016, genre="Drama", episode_no=10, season_no=5)
series5 = series(title="Black Mirror", release_year=2011, genre="Sci-Fi", episode_no=6, season_no=6)
series6 = series(title="The Witcher", release_year=2019, genre="Fantasy", episode_no=8, season_no=2)
series7 = series(title="Breaking Bad", release_year=2008, genre="Crime", episode_no=13, season_no=5)
series8 = series(title="Friends", release_year=1994, genre="Comedy", episode_no=24, season_no=10)
series9 = series(title="The Mandalorian", release_year=2019, genre="Sci-Fi", episode_no=8, season_no=2)
series10 = series(title="Sherlock", release_year=2010, genre="Mystery", episode_no=4, season_no=4)

library_list = []
library_list.extend([movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, series1, series2, series3, series4, series5, series6, series7, series8, series9, series10])

def get_movies():
    movie_list = []
    for i in library_list:
        if isinstance(i, movie):
            movie_list.append(i)
    sorted_movie_list = sorted(movie_list, key=lambda movie: movie.title)       
    return sorted_movie_list      

def get_series():
    series_list = []
    for i in library_list:
        if isinstance(i, series):
            series_list.append(i)
    sorted_series_list = sorted(series_list, key=lambda series: series.title)       
    return sorted_series_list

def search(title):
    for i in library_list:
        if i.title == title:
            return(i.title)
       
def generate_views():
    i = random.choice(library_list)
    i.play(random.randint(1,100))

def generate_views_10times():
    for i in range(10):
        generate_views()

def top_titles(n, content_type=None):
    if content_type == "movie":
        items = get_movies()
    elif content_type == "series":
        items = get_series()
    else:
        items = library_list

    sorted_items = sorted(items, key=lambda item: item.view_count, reverse=True)

    print(f"Top {n} Titles ({content_type or 'all'}):")
    for i, item in enumerate(sorted_items[:n], 1):
        print(f"{i}. {item}")

generate_views()
generate_views_10times()
top_titles(5)
top_titles(6, "movie")
top_titles(7, "series")
