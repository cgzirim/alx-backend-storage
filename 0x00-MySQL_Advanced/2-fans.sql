-- Ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, fans AS nb_fans from holberton.metal_bands ORDER BY nb_fans DESC;
