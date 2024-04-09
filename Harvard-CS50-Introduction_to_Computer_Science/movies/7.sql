--list of all films and corresponding ratings from 2010 in descending order. If films have the same rating, sort them alphabetically. Do not display films without a rating
SELECT rating, title
FROM movies
    JOIN ratings ON movies.id = ratings.movie_id
WHERE year = '2010'
ORDER BY rating DESC, title ASC;
--if you used two ORDER-BY-commands, the most recent is subordinated to the previous ones and doesn't alter the ones before, just adds some functionality.

--JOIN can only be used, if you have choosen a table you want to join.
--Columns that are not yet in the table can be selected by SELECT before JOIN, as long as the respective tables are joined later.
-- -->therefore The COLUMNS from the table later used/previously selected must be addressed.

-- Rating NOT NULL will be fitered out automaticall, no command needed.
