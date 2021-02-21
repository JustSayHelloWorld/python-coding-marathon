"""As input data you have list of strings with information about some location:

"id,name,poppulation,is_capital",
"3024,eu_kyiv,24834,y",
"3025,eu_volynia,20231,n",
"3026,eu_galych,23745,n",
"4892,me_medina,18038,n",
"4401,af_cairo,18946,y",
"4700,me_tabriz,13421,n",
"4899,me_bagdad,22723,y",
"6600,af_zulu,09720,n"

Using regular expression write method max_population()
for parsing strings and get info about location with highest population
"""

import re

strict_data = []
city_info = ""
pop: int
max_pop_city_index: int


def max_population(data):
    for each in data:

        city_info = re.findall(r"(\w+_\w+).+\d{5,},[yn]", each, flags=0)
        pop = re.findall(r"\w+_\w+.+(\d{5,}),[yn]", each, flags=0)

        if len(city_info) > 0:
            strict_data.append((city_info[0], int(pop[0])))

    return max(strict_data, key=lambda x: x[1])