import random

class Library:
   
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        # Variables
        self.view_count = 0 

    def play(self, step = 1):
        self.view_count += step
    
class Movie(Library):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.release_year})'
   
class Series(Library):
   
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

Library_list = [

    Movie(title = "Matrix", release_year=1999, genre="scifi"),
    Movie(title = "Fight Club", release_year=1999, genre="drama"),
    Movie(title="Inception", release_year=2010, genre="Sci-Fi"),
    Movie(title="The Shawshank Redemption", release_year=1994, genre="Drama"),
    Movie(title="Pulp Fiction", release_year=1994, genre="Crime"),
    Movie(title="The Dark Knight", release_year=2008, genre="Action"),
    Movie(title="Forrest Gump", release_year=1994, genre="Drama"),
    Movie(title="The Godfather", release_year=1972, genre="Crime"),
    Movie(title="Avatar", release_year=2009, genre="Sci-Fi"),
    Movie(title="Titanic", release_year=1997, genre="Romance"),

    Series(title = "Sopranos", release_year=2000, genre="crime", episode_no=15, season_no = 8),
    Series(title="Stranger Things", release_year=2016, genre="Sci-Fi", episode_no=8, season_no=4),
    Series(title="Game of Thrones", release_year=2011, genre="Fantasy", episode_no=10, season_no=8),
    Series(title="The Crown", release_year=2016, genre="Drama", episode_no=10, season_no=5),
    Series(title="Black Mirror", release_year=2011, genre="Sci-Fi", episode_no=6, season_no=6),
    Series(title="The Witcher", release_year=2019, genre="Fantasy", episode_no=8, season_no=2),
    Series(title="Breaking Bad", release_year=2008, genre="Crime", episode_no=13, season_no=5),
    Series(title="Friends", release_year=1994, genre="Comedy", episode_no=24, season_no=10),
    Series(title="The Mandalorian", release_year=2019, genre="Sci-Fi", episode_no=8, season_no=2),
    Series(title="Sherlock", release_year=2010, genre="Mystery", episode_no=4, season_no=4)
]

def get_movies():
    movie_list = []
    for i in Library_list:
        if isinstance(i, Movie):
            movie_list.append(i)
    sorted_movie_list = sorted(movie_list, key=lambda Movie: Movie.title)       
    return sorted_movie_list      

def get_series():
    Series_list = []
    for i in Library_list:
        if isinstance(i, Series):
            Series_list.append(i)
    sorted_Series_list = sorted(Series_list, key=lambda Series: Series.title)       
    return sorted_Series_list

def search(title):
    for i in Library_list:
        if i.title == title:
            return(i)
       
def generate_views():
    i = random.choice(Library_list)
    i.play(random.randint(1,100))

def generate_views_10times():
    for i in range(10):
        generate_views()

def top_titles(n, content_type=None):
    if content_type == "Movie":
        items = get_movies()
    elif content_type == "Series":
        items = get_series()
    else:
        items = Library_list

    sorted_items = sorted(items, key=lambda item: item.view_count, reverse=True)

    print(f"Top {n} Titles ({content_type or 'all'}):")
    for i, item in enumerate(sorted_items[:n], 1):
        print(f"{i}. {item}")

generate_views()
generate_views_10times()
top_titles(5)
top_titles(6, "Movie")
top_titles(7, "Series")
