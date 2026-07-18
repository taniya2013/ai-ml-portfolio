from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def news():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://www.bbc.com/news")
    time.sleep(5)

    data = []

    headlines = driver.find_elements(By.TAG_NAME, "h2")

    for h in headlines[:15]:
        title = h.text.strip()

        if title:
            data.append({
                "headline": title
            })

    driver.quit()
    return data


if __name__ == "__main__":
    result = news()

    for i in result:
        print(i)