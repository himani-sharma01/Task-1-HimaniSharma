movies = {
    "action": ["Avengers", "John Wick", "Batman"],
    "comedy": ["3 Idiots", "Dhamaal", "Hera Pheri"],
    "romance": ["DDLJ", "Jab We Met", "Titanic"]
}

choice = input("Enter genre: ").lower()

if choice in movies:
    print("Recommended movies:")
    
    for movie in movies[choice]:
        print(movie)
else:
    print("Genre not available")
