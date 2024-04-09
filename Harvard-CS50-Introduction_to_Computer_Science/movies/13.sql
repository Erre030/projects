--Actors who have starred in a movie with Kevin Bacon. Only select Kevin Bacon born in 1958. Kevin Bacon himself should not appear in the list.
SELECT name
FROM people
    JOIN stars ON people.id = stars.person_id
    JOIN movies ON stars.movie_id = movies.id
WHERE movies.id IN (
    SELECT movies.id FROM movies
        JOIN stars ON movies.id = stars.movie_id
        JOIN people ON stars.person_id = people.id
    WHERE name = 'Kevin Bacon' AND birth = '1958')
AND name IS NOT 'Kevin Bacon';

--You can also pack SELECT commands into conditions. You can probably put everything that is used for searching in WHERE conditions.

--Procedure: First you define output and join the tables.
--the movies.id is searched for, where kevin bacon with birth year 1958 is in --> all films with kevin bacon /1958.
--to exclude kevin bacon just address column where kevin bacon is in (name) and exclude him with IS NOT.
--(Actor IDs are linked to respective movie-ids, which is why you can filter out all actors using the special movie-id in the WHERE condition (-> always depends on the structure of the database))
