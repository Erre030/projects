--lists all movies in which jhonny depp and helena bonham carter played in
SELECT title
FROM movies
    JOIN stars ON movies.id = stars.movie_id
    JOIN people ON stars.person_id = people.id
WHERE name IN ('Johnny Depp', 'Helena Bonham Carter')
GROUP BY title
    HAVING COUNT (name) = 2;

--1.IN-Operator = specific COLUMN has value.
--2.GROUP BY = grouped by discret values.HAVING states, which specific value is searched /looked for.
--(In this case: Grouping by title if both names are present, which corresponds to COUNT = 2 // Always use GROUPED BY and HAVING together)
