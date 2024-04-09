--show number of movies with a rating of 10.0
SELECT COUNT(title)
FROM movies
    JOIN ratings ON movies.id = movie_id
WHERE ratings.rating = '10.0';

--If using JOIN, first the new table to be added to the selection and then the column to be joined.
--selection of different rows of the different tables by  "tablename.row".
