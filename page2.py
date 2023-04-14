from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
import time

from fake_useragent import UserAgent


class UseSelenium:
    def __init__(self, url: str, filename: str):
        self.url = url
        self.filename = filename

    def save_page(self):
        # Получаем случайный user-agent
        persona = self.get_headers_proxy()

        # Настраиваем опции для драйвера Chrome
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={persona}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")

        # Опции прокси-сервера
        options_proxy = {
            'proxy': {
                'no_proxy': 'localhost,127.0.0.1:8080'
            }
        }

        # Создаем сервис Chrome с указанным путем к исполняемому файлу chromedriver
        s = Service('C:\\Users\\Nadin\PycharmProjects\Sele\chromedriver.exe')

        # Создаем экземпляр драйвера Chrome с заданными опциями
        driver = webdriver.Chrome(options=options, service=s, seleniumwire_options=options_proxy)

        try:
            # Открываем URL и ждем загрузки страницы
            driver.get(self.url)
            time.sleep(5)

            # Прокручиваем страницу вниз и ждем, чтобы убедиться, что все элементы загрузились
            driver.execute_script("window.scrollTo(5,3000);")
            #driver.execute_script('window.scrollTo({top: 5, left: 4000, behavior: "smooth",});')
            time.sleep(5)

            # Получаем исходный код страницы
            html = driver.page_source

            # Сохраняем исходный код страницы в файл с указанным именем
            with open('pages/' + self.filename, 'w', encoding='utf-8') as f:
                f.write(html)
        except Exception as ex:
            # Выводим ошибку, если возникла проблема при обработке страницы
            print(ex)
        finally:
            # Закрываем драйвер и освобождаем ресурсы
            driver.close()
            driver.quit()

    def get_headers_proxy(self) -> dict:
        try:
            # Получаем случайный user-agent с помощью библиотеки UserAgent
            persona = UserAgent().random
        except ImportError:
            # Если возникла ошибка импорта, используем None в качестве user-agent
            persona = None
        return persona
