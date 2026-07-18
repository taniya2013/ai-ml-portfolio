from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def flipkart():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.flipkart.com/search?q=laptop")

    time.sleep(8)

    products = driver.find_elements(By.XPATH, "//div[@data-id]")

    print("Products Found:", len(products))

    data = []

    for product in products:

        # Title
        try:
            title = product.find_element(By.CLASS_NAME, "RG5Slk").text
        except:
            title = "N/A"

        # Price
        try:
            price = product.find_element(By.CLASS_NAME, "hZ3P6w").text
        except:
            price = "N/A"

        # Image
        try:
            image = product.find_element(By.CLASS_NAME, "UCc1lI").get_attribute("src")
        except:
            image = ""

        data.append({
            "Title": title,
            "Price": price,
            "Image": image
        })

    driver.quit()
    return data


if __name__ == "__main__":

    products = flipkart()

    for p in products:
        print(p)