from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import random
from selenium.webdriver.chrome.options import Options


def hc(value):
    head = None
    try:
        time.sleep(random.randint(1, 2))
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        url = f'http://www.linkedin.com/company/{value}/'
        driver.maximize_window()
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
