--list of all songs from post malone
SELECT name
FROM songs
WHERE artist_id IS
    (SELECT id FROM artists WHERE name IS 'Post Malone');

--"IS" and "=" have the same function in SQL
