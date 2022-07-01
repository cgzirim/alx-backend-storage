-- Ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, fans from holberton.metal_bands ORDER BY fans DESC;
