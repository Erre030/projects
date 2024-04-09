--ists actors who were part of toy-story
SELECT name
FROM movies
    JOIN stars on movies.id = stars.movie_id
    JOIN people on stars.person_id = people.id
WHERE title IS 'Toy Story';
