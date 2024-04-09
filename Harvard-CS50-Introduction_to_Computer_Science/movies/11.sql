--list of the five highest rated movies where chadwick boseman was an actor, starting with highest rating
SELECT title
    FROM movies
        JOIN ratings ON movies.id = ratings.movie_id
        JOIN stars on movies.id = stars.movie_id
        JOIN people on stars.person_id = people.id
    WHERE name = 'Chadwick Boseman'
    ORDER BY rating DESC LIMIT 5;
