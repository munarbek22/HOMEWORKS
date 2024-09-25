
country_flags = {'kgz': {'red', 'yellow'},
                 'kaz': {'blue', 'yellow'},
                 'pal': {'black', 'white', 'green', 'red'},
                 'esp': {'red', 'yellow'},
                 'eng': {'white', 'red'}}
while True:
    countries = []
    color = input("Enter the color or colours (with space between): ")
    if color.lower() == 'exit' or color.lower() == 'выход' or color.lower() == 'q':
        print('exit...')
        break
    color = set(color.split())
    for key, value in country_flags.items():
        if color.issubset(value):
            countries.append(key)
    if len(countries) == 0:
        print('There is no country with this colour in flag...')
    else:
        for i in countries:
            print(i)