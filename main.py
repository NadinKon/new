from page2 import UseSelenium


def main():
    # URL начальной страницы смартфонов с высоким рейтингом на Ozon
    url = 'https://www.ozon.ru/category/smartfony-15502/?sorting=rating'

    # Ограничим парсинг первыми 3 страницами
    max_page = 3
    i = 1
    while i <= max_page:
        # Создаем имя файла для сохранения HTML-содержимого каждой страницы
        filename = f'page_' + str(i) + '.html'

        # Если это первая страница, сохраняем ее содержимое без параметра page в URL
        if i == 1:
            UseSelenium(url, filename).save_page()
        # Для последующих страниц добавляем параметр page в URL и сохраняем их содержимое
        else:
            url_param = f"https://www.ozon.ru/category/smartfony-15502/?page={str(i)}&sorting=rating"
            UseSelenium(url_param, filename).save_page()
        # Увеличиваем счетчик для перехода к следующей странице
        i += 1


if __name__ == '__main__':
    main()
