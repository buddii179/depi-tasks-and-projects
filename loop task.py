from countries import countries
from countries_details_dat import countries_data

countries_with_land = []

for country in countries:
    if 'land' in country:
        countries_with_land.append(country)

# Printing the extracted countries
print("Countries containing 'land':")
print(countries_with_land)