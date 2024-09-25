
movies = {
    'kung fu panda': {
        'Munarbek': 9,
        'Adilet': 8,
    },
    'karate kid': {
        'Munarbek': 10,
        'Adilet': 10,
        'Aman': 9,
    },
    'rush hour': {
        'Munarbek': 9,
        'Adilet': 9,
    },
}

def rate_and_add_movie(movies):
    movie = input("Enter movie name:")
    while True:
        action = int(input('Select what do you want to do:\n'
                           ' 1 - add movie,\n'
                           ' 2 - rate movie,\n'
                           ' 3 - average rating\n'
                           ' 4 - see all movies\n'
                           ' 5 - exit\n'
                           ': '))
        if action == 1:
            if movie in movies:
                print("This movie already exists")
            else:
                movies[movie] = {}
                print("Movie added")
        elif action == 2:
            if movie not in movies:
                print("This movie does not exist")
            else:
                name = input("Enter your name:").title()
                if name in movies[movie]:
                    print("You have already rated this movie")
                else:
                    rating = int(input("Enter rating(from 0 to 10):"))
                    if 0 <= rating <= 10:
                        movies[movie][name] = rating
        elif action == 3:
            if movie not in movies:
                print("This movie does not exist")
            else:
                ratings = movies[movie].values()
                average = sum(ratings) / len(ratings)
                print(f"Average rating of {movie} is {average}")
        elif action == 4:
            for movie, ratings in movies.items():
                print(f"{movie}: {ratings}")
        elif action == 5:
            break
        else:
            print("Invalid input")


rate_and_add_movie(movies)


