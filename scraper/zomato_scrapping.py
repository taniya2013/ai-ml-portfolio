from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re


def zomato_scraper():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://www.zomato.com/ncr/restaurants")

    time.sleep(10)

    # scroll for dynamic loading
    for _ in range(6):
        driver.execute_script("window.scrollBy(0, 3000)")
        time.sleep(2)

    data = []

    cards = driver.find_elements(By.XPATH, "//a[contains(@href,'/ncr/')]")

    print("FOUND:", len(cards))

    for c in cards:
        try:
            link = c.get_attribute("href")
            if not link:
                continue

            text = c.text.strip()
            if not text:
                continue

            lines = text.split("\n")

            name = lines[0] if len(lines) > 0 else "N/A"

            # 🔥 rating fix (regex based)
            rating = "N/A"
            match = re.search(r"\b\d\.\d\b", text)
            if match:
                rating = match.group()

            if name and link:
                data.append({
                    "name": name,
                    "rating": rating,
                    "link": link
                })

        except:
            pass

    driver.quit()
    return data


# test run (optional)
if __name__ == "__main__":
    result = zomato_scraper()

    for i, r in enumerate(result):
        print(i + 1, r)