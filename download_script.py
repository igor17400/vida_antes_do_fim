import json
from urllib.request import urlopen

# Download the GeoJSON file
with urlopen('https://raw.githubusercontent.com/fea-dev-usp/IBGE/master/geojson_2022.json') as response:
	geo_json = json.load(response)

	# Inspect the first feature to ensure data is loaded correctly
	print(geo_json["features"][0])

	# Save the GeoJSON data to a local file
	with open("./data/brazil_geo_2022.json", "w", encoding='utf-8') as file:
		json.dump(geo_json, file, ensure_ascii=False, indent=4)

