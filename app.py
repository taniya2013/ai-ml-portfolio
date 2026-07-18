import requests
from flask import Flask, render_template, request
from scraper.Amazon_scrapping import Amazon
from scraper.goodreads_scrapping import goodreads
from scraper.spotify_scrapping import spotify
from scraper.hackernews_scrapping import hackernews
from scraper.books_scrapping import books
from scraper.flipkart_scrapping import flipkart
from scraper.quotes_scrapping import scrape_quotes
from scraper.youtube_vedios_scrapping import youtube_trending
from scraper.zomato_scrapping import zomato_scraper
from scraper.live_hackernews_scrapping import hackernews_scraper
from scraper.weather_scrapping import weather
from scraper.news_scrapping import news
from scraper.currency_converter_scrapping import currency_converter as convert_currency

app = Flask(__name__)
API_KEY = "63c1bb2b"
# Home page route
@app.route('/')
@app.route('/home.html')
def home():
    return render_template('home.html')

# About page route (Consolidated)
@app.route('/about.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/learnmore")
def learn_more():
    return render_template("Learn_more.html")

@app.route("/scrapping")
def scrapping():
    return render_template("scrapping.html")

@app.route("/static_scraping")
def staticscraping():
    return render_template("static_scraping.html")

@app.route("/dynamicscraping")
def dynamicscraping():
    return render_template("dynamic_scrapping.html")

@app.route("/powerbi")
def powerbi():
    return render_template("powerbi.html")

@app.route("/api")
def apiscrapping():
    return render_template("api_scrapping.html")

@app.route("/university")
def university():
    return render_template("university.html")

@app.route("/sales")
def sales():
    return render_template("sales.html")

@app.route("/hr")
def hr():
    return render_template("hr.html")

@app.route("/goodreads")
def goodreads_page():
    data = goodreads()
    return render_template("goodreads.html", quotes=data)

@app.route("/amazon")
def amazon_page():
    data = Amazon()
    return render_template("amazon.html", products=data)

@app.route("/spotify")
def spotify_page():
    data = spotify()
    return render_template("spotify.html", songs=data)

@app.route("/hackernews")
def hackernews_page():
    data = hackernews()
    return render_template("hackernews.html", news=data)

@app.route("/books")
def books_page():
    data = books()
    return render_template("books.html", books=data)

@app.route("/flipkart")
def flipkart_page():
    data = flipkart()
    return render_template("flipkart.html", products=data)

@app.route("/quotes")
def quotes_page():
    data = scrape_quotes()
    return render_template("quotes.html", quotes=data)

@app.route("/youtube")
def youtube_page():
    data = youtube_trending()
    return render_template("youtube.html", videos=data)

@app.route("/zomato")
def zomato_page():
    data = zomato_scraper()
    return render_template("zomato.html", data=data)

@app.route("/livehackernews")
def live_hackernews_page():
    data = hackernews_scraper()
    return render_template("live_hackernews.html", news=data)

@app.route("/movie_search", methods=["GET", "POST"])
def movie_search():
    movies = []
    if request.method == "POST":
        movie_name = request.form["movie"]
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={movie_name}"
        response = requests.get(url)
        data = response.json()
        if data.get("Response") == "True":
            movies = data["Search"]
    return render_template("movie_search.html", movies=movies)

@app.route("/weather", methods=["GET", "POST"])
def weather_page():
    data = None
    if request.method == "POST":
        city = request.form["city"]
        data = weather(city)
    return render_template("weather.html", weather=data)

@app.route("/news")
def news_page():
    data = news()
    return render_template("news.html", data=data)

@app.route("/currency_converter", methods=["GET", "POST"])
def currency_converter():
    data = None
    if request.method == "POST":
        from_currency = request.form["from_currency"].upper()
        to_currency = request.form["to_currency"].upper()
        amount = float(request.form["amount"])
        data = convert_currency(from_currency, to_currency, amount)
    return render_template("currency.html", data=data)

@app.route("/country_information")
def country_information():
    url = "https://countriesnow.space/api/v0.1/countries"
    response = requests.get(url)
    countries = []
    if response.status_code == 200:
        json_data = response.json()
        if not json_data.get("error"):
            countries = json_data.get("data", [])
    return render_template("country_information.html", countries=countries)

@app.route("/internship")
def internship():
    return render_template("internship.html")

@app.route("/capstone")
def capstone():
    return render_template("capstone.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

@app.route("/usecases")
def usecases():
    return render_template("usecases.html")
# Blog page route
@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)