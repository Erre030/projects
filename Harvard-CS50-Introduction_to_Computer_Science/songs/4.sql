--song name with danceability, energy, valence over 0.75(address columns individually)
SELECT name
FROM songs
WHERE danceability > 0.75
AND energy > 0.75
AND valence > 0.75;
