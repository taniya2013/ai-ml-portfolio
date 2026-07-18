import requests
url= 'https://www.goodreads.com/quotes'
def goodreads():

    response = requests.get(url)
    response.status_code
    header= {
    'user-Agent': 'Mozilla/5.0(window NT 10.0;Win4;X64) Applewebkit/537.36(KHTML.like Gecko) chrome/91.0.4472.124 Safari/537.36 '
    }
    response= requests.get(url,headers=header)

    from bs4 import BeautifulSoup   
    soup= BeautifulSoup(response.text,'html.parser')
    soup.title
    books = soup.find_all('div', class_='quote')
    quotes_data = []
    quotes_data = []

    for quote in books:

        quote_text = quote.find('div', class_='quoteText').get_text(strip=True)

        author = quote.find('span', class_='authorOrTitle').get_text(strip=True)

        img_tag = quote.find('img')
        image_url = img_tag['src'] if img_tag else ""

        tag_div = quote.find('div', class_='greyText smallText left')
        tags = [a.get_text(strip=True) for a in tag_div.find_all('a')] if tag_div else []

        quotes_data.append({
        'quote': quote_text,
        'author': author,
        'image_url': image_url,
        'tags': ', '.join(tags)
    })
    return quotes_data