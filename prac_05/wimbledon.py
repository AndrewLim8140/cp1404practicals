"""
Read file
get champs and times
get winning country
sort
print
"""
champions_dic = {}
countries_dic = {}
winning_countries = ''
Header_removed = False

with open('wimbledon.csv', 'r', encoding='utf-8-sig') as in_file:
    for data in in_file:
        if Header_removed == True:
            data = data.split(',')

            # obtain champs
            champion = data[2]

            try:
                count_champions = champions_dic[champion]
                count_champions += 1
                champions_dic[champion] = count_champions

            except KeyError:
                champions_dic[champion] = 1

            # obtain country
            country = data[1]

            try:
                count_country = countries_dic[country]
                count_country += 1
                countries_dic[country] = count_country

            except KeyError:
                countries_dic[country] = 1

        if Header_removed == False:
            Header_removed = True

    print('Wimbledon Champions :')
    for champion in champions_dic:
        count = champions_dic[champion]
        print(f'{champion}  {count}')

    print("")
    print(f'These {len(countries_dic)} countries have won Wimbledon :')
    countries = list(countries_dic.keys())
    for country in countries:
        winning_countries = winning_countries + country + ", "
    print(f'{winning_countries}')

