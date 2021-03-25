from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random
import os
from selenium.webdriver.chrome.options import Options


def hc(value):
    head = None
    try:
        time.sleep(random.randint(1, 2))
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument("--headless")
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path=os.environ.get(
            "CHROMEDRIVER_PATH"), options=options)
        url = f'http://www.linkedin.com/company/{value}/'
        driver.get(url)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, "html.parser")
        names = soup.find(
            'a', attrs={'class': 'top-card__right-column-link'}).text
        driver.quit()
        filtered = names.replace(",", "")
        numbers1 = [int(word) for word in filtered.split() if word.isdigit()]
        head = numbers1[0]
        if (head < 20):
            head = 0
        elif (100 > head >= 20):
            head = 0.175
        elif (head >= 100):
            head = 0.35
    except:
        driver.quit()
        head = 0.175

    return head
