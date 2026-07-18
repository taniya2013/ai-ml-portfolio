from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_quotes():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    url = "https://quotes.toscrape.com/js/"
    driver.get(url)
    time.sleep(5)

    quotes = []

    # loop pages
    for i in range(3):
        cards = driver.find_elements(By.CLASS_NAME, "quote")

        for c in cards:
            try:
                text = c.find_element(By.CLASS_NAME, "text").text
                author = c.find_element(By.CLASS_NAME, "author").text

                quotes.append({
                    "quote": text,
                    "author": author
                })
            except:
                pass

        # next page button
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, "li.next a")
            next_btn.click()
            time.sleep(3)
        except:
            break

    driver.quit()
    return quotes