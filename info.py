class movie:
    pass

Harry_Potter = movie()
Maleficent = movie()
Doctor_Strange = movie()
The_Hobbit = movie()
Pirates_of_the_Caribbean = movie()
Harry_Potter.title = "Harry Potter and the Philosopher's Stone"
Maleficent.title = "Maleficent"
Doctor_Strange.title = "Doctor Strange"
The_Hobbit.title = "The Hobbit: An Unexpected Journey"
Pirates_of_the_Caribbean.title = "Pirates of the Caribbean: The Curse of the Black Pearl"
Harry_Potter.director = "Chris Columbus"
Maleficent.director = "Robert Stromberg"
Doctor_Strange.director = "Scott Derrickson"
The_Hobbit.director = "Peter Jackson"
Pirates_of_the_Caribbean.director = "Gore Verbinski"
Harry_Potter.year = 2001
Maleficent.year = 2014
Doctor_Strange.year = 2016
The_Hobbit.year = 2012
Pirates_of_the_Caribbean.year = 2003
Harry_Potter.rating = 7.7
Maleficent.rating = 6.9
Doctor_Strange.rating = 7.5
The_Hobbit.rating = 7.8
Pirates_of_the_Caribbean.rating = 8.1


movies = [Harry_Potter, Maleficent, Doctor_Strange, The_Hobbit, Pirates_of_the_Caribbean]

highest_movie = movies[0]

for movie in movies:
    if movie.rating > highest_movie.rating:
        highest_movie = movie

for movie in movies:
    print(f"Title: {movie.title}")
    print(f"Director: {movie.director}")
    print(f"Year: {movie.year}")
    print(f"Rating: {movie.rating}")
    print("/n")
    print("================================")

print(f"Highest Rating Movie: {highest_movie.title} with a rating of {highest_movie.rating}")
    