--lists titles and years of release of all Harry Potter films in chronological order
SELECT title, year
FROM movies
WHERE title LIKE 'Harry Potter%'
ORDER BY year ASC;
