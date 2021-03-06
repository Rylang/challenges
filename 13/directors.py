import csv
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(MOVIE_DATA, encoding='utf8') as file:
        for line in csv.DictReader(file):
            try:
                director = line['director_name']
                title = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            movie = Movie(title, year, score)
            directors[director].append(movie)

    return directors


def get_average_scores(directors):
    """Filter directors with < MIN_MOVIES and calculate average score"""
    filtered_directors = {director: movies for director, movies in directors.items() if len(movies) > MIN_MOVIES}

    # for director, movies in directors.items():
    #     average_score = _calc_mean(movies)
    #     print(average_score)

    return filtered_directors


def _calc_mean(movies):
    """Helper method to calculate mean of list of Movie namedtuples"""
    total_score = sum(movie[2] for movie in movies)
    avg_score = total_score / len(movies)
    return round(avg_score, 1)


def print_results(directors):
    """Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output"""
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    """This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py"""
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
