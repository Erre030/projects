--lists actors which played in movies of 2004 , ordered by birth year (double entries filtered out)
SELECT DISTINCT name
FROM movies
    JOIN stars on movies.id = stars.movie_id
    JOIN people on stars.person_id = people.id
WHERE year = '2004'
ORDER BY birth
