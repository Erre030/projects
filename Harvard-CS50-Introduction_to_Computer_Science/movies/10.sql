--lists all dircetors which have produced films with a rating => 9 (eliminate duplicate entries)
SELECT DISTINCT name
    FROM movies
        JOIN ratings ON movies.id = ratings.movie_id
        JOIN directors on movies.id = directors.movie_id
        JOIN people on directors.person_id = people.id
    WHERE rating >= '9.0';
