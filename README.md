## Дипломная работа. Доска объявлений.
#### Приложение для продажи товаров. Каждый пользователь может размещать товары, оставлять комментарии.

## Установка:

1. Клонируйте репозиторий на свой компьютер:

   ```bash
   git clone https://github.com/Kusto7/notice_board
   ```
2. Создайте файл `.env` в корне приложения, используя образец из `.env_example`.
3. Используйте Docker для запуска frontend части приложения:
    ```bash
   docker build -t frontent:latest . 
   docker run -p 3000:3000 frontent:latest
    ```
4. Подключите backend часть:
    ```bash
   python skymarket\manage.py runserver 
    ```
5. Откройте браузер и перейдите по адресу: http://127.0.0.1:3000/
#### Enjoy!