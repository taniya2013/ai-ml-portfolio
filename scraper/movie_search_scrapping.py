import requests

API_KEY = "your_omdb_api_key_here"

def search_movie(movie_name):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={movie_name}"

    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        movies = data["Search"]

        for movie in movies:
            print("Title:", movie["Title"])
            print("Year :", movie["Year"])
            print("Type :", movie["Type"])
            print("IMDB ID:", movie["imdbID"])
            print("-" * 40)
    else:
        print("No results found:", data.get("Error"))


if __name__ == "__main__":
    name = input("Enter movie name: ")
    search_movie(name)