from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def youtube_trending():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://www.youtube.com/results?search_query=trending+videos")

    time.sleep(6)

    videos = []

    # better scrolling
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)

    # better selector (more stable than #video-title)
    elements = driver.find_elements(By.XPATH, "//a[@href]")

    print("FOUND:", len(elements))

    count = 0

    for e in elements:
        try:
            title = e.get_attribute("title")
            link = e.get_attribute("href")

            if title and link and "watch?v=" in link:
                videos.append({
                    "title": title,
                    "link": link
                })

                count += 1

            if count == 20:   # limit safely
                break

        except:
            pass

    driver.quit()
    return videos