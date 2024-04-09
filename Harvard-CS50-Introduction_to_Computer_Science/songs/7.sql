--average energy from the songs of drake
SELECT AVG(energy)
FROM songs
WHERE artist_id IS
    (SELECT id FROM artists WHERE name IS 'Drake');
