SELECT title, rating FROM ratings, movies WHERE ratings.movie_id = movies.id AND year = 2010 ORDER BY rating DESC, title ASC;