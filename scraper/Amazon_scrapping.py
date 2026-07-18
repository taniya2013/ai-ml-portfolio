import requests
def Amazon():

    url='https://www.amazon.in/s?k=laptop&crid=YLH7SZQM1WE6&sprefix=laptop%2Caps%2C610&ref=nb_sb_noss_2'
    response=requests.get(url)
    response.status_code
    header= {
    'user-Agent': 'Mozilla/5.0(window NT 10.0;Win4;X64) Applewebkit/537.36(KHTML.like Gecko) chrome/91.0.4472.124 Safari/537.36 '

    }
    response= requests.get(url,headers=header)
    from bs4 import BeautifulSoup
    soup= BeautifulSoup(response.text,'html.parser')
    soup.title

    products = soup.find_all("div", attrs={"data-component-type": "s-search-result"})
    data=[]
    for product in products:
    
    
        title = product.select_one("h2 span")
        title = title.get_text(strip=True) if title else "N/A"

    
        price = product.find("span", class_="a-price-whole")
        price = price.get_text(strip=True) if price else "N/A"

    
        rating = product.find("span", class_="a-icon-alt")
        rating = rating.get_text(strip=True) if rating else "N/A"

    # Image URL
        img = product.find("img")
        image_url = img.get("src") if img else "N/A"

    # Store data
        data.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Image URL": image_url
    })
    return data
  