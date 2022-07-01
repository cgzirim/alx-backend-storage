-- List all bands with 'Glam rock' as their main style, ranked by their longevity.
SELECT band_name, (formed - split) AS lifespan FROM holberton.metal_bands
	WHERE style = 'Glam rock';
