from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def hackernews_scraper():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://news.ycombinator.com/")

    time.sleep(6)

    news_data = []

    rows = driver.find_elements(By.CSS_SELECTOR, "tr.athing")

    print("FOUND POSTS:", len(rows))

    for row in rows:
        try:
            title_tag = row.find_element(By.CSS_SELECTOR, "span.titleline a")

            title = title_tag.text
            link = title_tag.get_attribute("href")

            points = "0 points"

            try:
                subtext = row.find_element(By.XPATH, "following-sibling::tr[1]")
                score = subtext.find_elements(By.CSS_SELECTOR, "span.score")

                if len(score) > 0:
                    points = score[0].text

            except:
                points = "0 points"

            news_data.append({
                "title": title,
                "points": points,
                "link": link
            })

        except:
            pass

    driver.quit()
    return news_data


# test
if __name__ == "__main__":
    data = hackernews_scraper()

    for i, d in enumerate(data):
        print(i + 1, d)